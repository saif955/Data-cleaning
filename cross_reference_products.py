import pandas as pd

def cross_reference_products():
    """Cross-reference product list with sales data and fix formatting"""
    
    # Read the files
    product_list_df = pd.read_csv('bohubrihi_product_list.csv')
    sales_df = pd.read_csv('daily_product_sales_cleaned.csv')
    
    print("CROSS-REFERENCING PRODUCTS")
    print("=" * 60)
    print(f"Products in list: {len(product_list_df)}")
    print(f"Products in sales: {len(sales_df['product'].unique())}")
    
    # Get product lists
    list_products = set(product_list_df['product'].str.lower().str.replace(' ', ''))
    sales_products = set(sales_df['product'].unique())
    
    print(f"Products in list (no spaces): {len(list_products)}")
    print(f"Products in sales (no spaces): {len(sales_products)}")
    
    # Find matches and mismatches
    matching_products = list_products.intersection(sales_products)
    list_only = list_products - sales_products
    sales_only = sales_products - list_products
    
    print(f"\nMatching products: {len(matching_products)}")
    print(f"List only: {len(list_only)}")
    print(f"Sales only: {len(sales_only)}")
    
    # Show matching products
    print(f"\nMATCHING PRODUCTS ({len(matching_products)}):")
    print("-" * 60)
    for i, product in enumerate(sorted(matching_products), 1):
        print(f"{i:2d}. {product}")
    
    # Show products in list but not in sales
    print(f"\nPRODUCTS IN LIST BUT NOT IN SALES ({len(list_only)}):")
    print("-" * 60)
    for i, product in enumerate(sorted(list_only), 1):
        print(f"{i:2d}. {product}")
    
    # Show products in sales but not in list
    print(f"\nPRODUCTS IN SALES BUT NOT IN LIST ({len(sales_only)}):")
    print("-" * 60)
    for i, product in enumerate(sorted(sales_only), 1):
        print(f"{i:2d}. {product}")
    
    # Create a mapping dictionary for fixing sales data
    product_mapping = {}
    
    # Create mapping from original product names to no-spaces format
    for _, row in product_list_df.iterrows():
        original = row['product']
        no_spaces = original.lower().replace(' ', '')
        product_mapping[no_spaces] = original
    
    # Fix sales data to match product list format
    print(f"\nFIXING SALES DATA FORMAT...")
    
    # Create a new column with corrected product names
    sales_df['product_corrected'] = sales_df['product'].apply(
        lambda x: product_mapping.get(x, x)  # Use mapping if exists, otherwise keep original
    )
    
    # Count how many were corrected
    corrected_count = (sales_df['product'] != sales_df['product_corrected']).sum()
    print(f"Products corrected: {corrected_count}")
    
    # Show some examples of corrections
    print(f"\nEXAMPLE CORRECTIONS:")
    print("-" * 60)
    corrections = sales_df[sales_df['product'] != sales_df['product_corrected']].head(10)
    for _, row in corrections.iterrows():
        print(f"  {row['product']} → {row['product_corrected']}")
    
    # Replace the product column with corrected version
    sales_df['product'] = sales_df['product_corrected']
    sales_df = sales_df.drop('product_corrected', axis=1)
    
    # Save the corrected sales data
    sales_df.to_csv('daily_product_sales_cleaned.csv', index=False)
    print(f"\nCorrected sales data saved to 'daily_product_sales_cleaned.csv'")
    
    # Create a comprehensive product reference file
    print(f"\nCREATING COMPREHENSIVE PRODUCT REFERENCE...")
    
    # Get all unique products from both sources
    all_products = sorted(list(set(list_products) | sales_products))
    
    reference_data = []
    for product in all_products:
        in_list = product in list_products
        in_sales = product in sales_products
        status = "Both" if in_list and in_sales else "List Only" if in_list else "Sales Only"
        
        # Try to find the original formatted name
        original_name = product_mapping.get(product, product)
        
        reference_data.append({
            'product_id': len(reference_data) + 1,
            'product_no_spaces': product,
            'product_formatted': original_name,
            'in_product_list': in_list,
            'in_sales_data': in_sales,
            'status': status
        })
    
    reference_df = pd.DataFrame(reference_data)
    reference_df.to_csv('product_reference.csv', index=False)
    print(f"Product reference saved to 'product_reference.csv'")
    
    # Show final statistics
    print(f"\nFINAL STATISTICS:")
    print("=" * 60)
    print(f"Total unique products: {len(all_products)}")
    print(f"In both list and sales: {len(matching_products)}")
    print(f"List only: {len(list_only)}")
    print(f"Sales only: {len(sales_only)}")
    print(f"Products corrected in sales: {corrected_count}")
    
    return sales_df, reference_df

if __name__ == "__main__":
    sales_df, reference_df = cross_reference_products() 