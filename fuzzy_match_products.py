import pandas as pd
from difflib import SequenceMatcher
import re

def similarity_score(a, b):
    """Calculate similarity score between two strings"""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def normalize_product_name(name):
    """Normalize product name for better matching"""
    # Remove common variations and standardize
    name = name.lower()
    name = re.sub(r'\s+', '', name)  # Remove spaces
    name = re.sub(r'[^\w]', '', name)  # Remove special characters
    return name

def find_best_match(product_name, product_list, threshold=0.6):
    """Find the best matching product from the list"""
    normalized_name = normalize_product_name(product_name)
    
    best_match = None
    best_score = 0
    
    for list_product in product_list:
        normalized_list = normalize_product_name(list_product)
        
        # Calculate similarity scores using different methods
        score1 = similarity_score(normalized_name, normalized_list)
        score2 = similarity_score(product_name.lower(), list_product.lower())
        
        # Check if one string contains the other
        contains_score = 0
        if normalized_list in normalized_name or normalized_name in normalized_list:
            contains_score = 0.8
        
        # Use the highest score
        score = max(score1, score2, contains_score)
        
        if score > best_score and score >= threshold:
            best_score = score
            best_match = list_product
    
    return best_match, best_score

def fuzzy_match_products():
    """Find and match all remotely similar products"""
    
    # Read the files
    product_list_df = pd.read_csv('bohubrihi_product_list.csv')
    sales_df = pd.read_csv('daily_product_sales_cleaned.csv')
    
    product_list = product_list_df['product'].tolist()
    
    print("FUZZY PRODUCT MATCHING")
    print("=" * 60)
    print(f"Products in list: {len(product_list)}")
    print(f"Products in sales: {len(sales_df['product'].unique())}")
    
    # Create mapping dictionary
    product_mapping = {}
    match_details = []
    
    # Process each unique product in sales
    unique_sales_products = sales_df['product'].unique()
    
    for sales_product in unique_sales_products:
        best_match, score = find_best_match(sales_product, product_list)
        
        if best_match:
            product_mapping[sales_product] = best_match
            match_details.append({
                'sales_product': sales_product,
                'matched_to': best_match,
                'similarity_score': score
            })
        else:
            # Keep original if no good match found
            product_mapping[sales_product] = sales_product
    
    # Show matches found
    print(f"\nMATCHES FOUND ({len([m for m in match_details if m['matched_to'] != m['sales_product']])}):")
    print("-" * 60)
    
    for match in sorted(match_details, key=lambda x: x['similarity_score'], reverse=True):
        if match['matched_to'] != match['sales_product']:
            print(f"  {match['sales_product']} → {match['matched_to']} (score: {match['similarity_score']:.2f})")
    
    # Apply the mapping to sales data
    print(f"\nAPPLYING MATCHES TO SALES DATA...")
    
    # Create new column with matched products
    sales_df['product_matched'] = sales_df['product'].map(product_mapping)
    
    # Count changes
    changes_made = (sales_df['product'] != sales_df['product_matched']).sum()
    print(f"Total rows updated: {changes_made}")
    
    # Show some examples of changes
    print(f"\nEXAMPLE CHANGES:")
    print("-" * 60)
    changes = sales_df[sales_df['product'] != sales_df['product_matched']].head(15)
    for _, row in changes.iterrows():
        print(f"  {row['product']} → {row['product_matched']}")
    
    # Replace the product column with matched version
    sales_df['product'] = sales_df['product_matched']
    sales_df = sales_df.drop('product_matched', axis=1)
    
    # Save the updated sales data
    sales_df.to_csv('daily_product_sales_cleaned.csv', index=False)
    print(f"\nUpdated sales data saved to 'daily_product_sales_cleaned.csv'")
    
    # Create detailed matching report
    print(f"\nCREATING DETAILED MATCHING REPORT...")
    
    # Group by matched products and show statistics
    matched_stats = sales_df.groupby('product').agg({
        'quantity_sold': 'sum',
        'date': 'count'
    }).rename(columns={'date': 'transactions'}).sort_values('quantity_sold', ascending=False)
    
    print(f"\nTOP SELLING PRODUCTS (after matching):")
    print("-" * 60)
    print(matched_stats.head(20).to_string())
    
    # Save matching report
    match_report_df = pd.DataFrame(match_details)
    match_report_df.to_csv('fuzzy_matching_report.csv', index=False)
    print(f"\nFuzzy matching report saved to 'fuzzy_matching_report.csv'")
    
    # Show final statistics
    print(f"\nFINAL STATISTICS:")
    print("=" * 60)
    print(f"Total unique products in sales: {len(unique_sales_products)}")
    print(f"Products matched to list: {len([m for m in match_details if m['matched_to'] != m['sales_product']])}")
    print(f"Products unchanged: {len([m for m in match_details if m['matched_to'] == m['sales_product']])}")
    print(f"Total rows updated: {changes_made}")
    print(f"Unique products after matching: {len(sales_df['product'].unique())}")
    
    return sales_df, match_report_df

if __name__ == "__main__":
    sales_df, match_report = fuzzy_match_products() 