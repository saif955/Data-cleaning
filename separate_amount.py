import pandas as pd
import re

def extract_amount_and_product(product_name):
    """
    Extract amount/size from product name and return cleaned product name and amount
    """
    # Common patterns for amounts/sizes
    amount_patterns = [
        r'\b(\d+(?:\.\d+)?)\s*(ml|g|gram|gm|kg|mls?|grams?|kgs?)\b',  # 50ml, 20g, 100ml, etc.
        r'\b(\d+)\s*(tk|taka)\b',  # 250tk, 60tk, etc.
        r'\b(\d+)\s*(pack|packs)\b',  # 50g pack, etc.
        r'\b(\d+)\s*(bar|bars)\b',  # 20g bar, etc.
    ]
    
    # Try to find amount patterns
    amount_found = None
    cleaned_product = product_name
    
    for pattern in amount_patterns:
        match = re.search(pattern, product_name, re.IGNORECASE)
        if match:
            amount_found = match.group(0)  # Full match (e.g., "50ml", "20g")
            # Remove the amount from product name
            cleaned_product = re.sub(pattern, '', product_name, flags=re.IGNORECASE).strip()
            # Clean up extra spaces and punctuation
            cleaned_product = re.sub(r'\s+', ' ', cleaned_product)
            cleaned_product = re.sub(r'[,\s-]+$', '', cleaned_product)  # Remove trailing commas, spaces, dashes
            cleaned_product = re.sub(r'^[,\s-]+', '', cleaned_product)  # Remove leading commas, spaces, dashes
            break
    
    return cleaned_product, amount_found

def main():
    # Read the corrected CSV file
    try:
        df = pd.read_csv('daily_product_sales_corrected.csv')
        print("Using corrected CSV file")
    except FileNotFoundError:
        df = pd.read_csv('daily_product_sales.csv')
        print("Using original CSV file")
    
    print(f"Processing {len(df)} rows...")
    
    # Apply the separation function
    results = df['product'].apply(extract_amount_and_product)
    
    # Create new columns
    df['product_clean'] = [result[0] for result in results]
    df['amount'] = [result[1] for result in results]
    
    # Show some examples
    print("\nSample separations:")
    print("=" * 80)
    for i, (original, clean, amount) in enumerate(zip(df['product'].head(20), df['product_clean'].head(20), df['amount'].head(20))):
        print(f"{i+1:2d}. Original: {original}")
        print(f"    Clean:   {clean}")
        print(f"    Amount:  {amount if amount else 'None'}")
        print("-" * 80)
    
    # Statistics
    products_with_amount = df['amount'].notna().sum()
    print(f"\nStatistics:")
    print(f"Total products: {len(df)}")
    print(f"Products with amount: {products_with_amount}")
    print(f"Products without amount: {len(df) - products_with_amount}")
    
    # Show unique amounts found
    unique_amounts = df['amount'].dropna().unique()
    print(f"\nUnique amounts found ({len(unique_amounts)}):")
    for amount in sorted(unique_amounts):
        count = (df['amount'] == amount).sum()
        print(f"  {amount}: {count} times")
    
    # Save the result
    output_file = 'daily_product_sales_with_amounts.csv'
    df.to_csv(output_file, index=False)
    print(f"\nData saved to '{output_file}'")
    
    # Show the new structure
    print(f"\nNew CSV structure:")
    print(df[['date', 'product', 'product_clean', 'amount', 'quantity_sold']].head(10).to_string(index=False))

if __name__ == "__main__":
    main() 