import pandas as pd

def remove_spaces_from_products():
    """Remove all spaces from product names"""
    
    # Read the cleaned CSV file
    df = pd.read_csv('daily_product_sales_cleaned.csv')
    
    print("REMOVING SPACES FROM PRODUCT NAMES")
    print("=" * 50)
    print(f"Total rows: {len(df)}")
    print(f"Unique products before: {len(df['product'].unique())}")
    
    # Show some examples before
    print("\nSample products BEFORE removing spaces:")
    for i, product in enumerate(df['product'].unique()[:10], 1):
        print(f"{i:2d}. {product}")
    
    # Remove all spaces from product names
    df['product'] = df['product'].str.replace(' ', '')
    
    print(f"\nUnique products after: {len(df['product'].unique())}")
    
    # Show some examples after
    print("\nSample products AFTER removing spaces:")
    for i, product in enumerate(df['product'].unique()[:10], 1):
        print(f"{i:2d}. {product}")
    
    # Show the final structure
    print("\nFinal structure:")
    print("=" * 80)
    print(df[['date', 'product', 'amount', 'quantity_sold']].head(15).to_string(index=False))
    
    # Save the updated data
    df.to_csv('daily_product_sales_cleaned.csv', index=False)
    print(f"\nUpdated data saved to 'daily_product_sales_cleaned.csv'")
    
    # Show statistics
    print(f"\nStatistics:")
    print(f"Products with amounts: {(df['amount'].notna()).sum()}")
    print(f"Products without amounts: {(df['amount'].isna()).sum()}")
    print(f"Total unique products: {len(df['product'].unique())}")
    
    # Show some examples of the final structure
    print(f"\nFinal examples:")
    print("=" * 80)
    for i, row in df.head(10).iterrows():
        print(f"{i+1:2d}. Product: {row['product']}")
        print(f"    Amount: {row['amount'] if pd.notna(row['amount']) else 'None'}")
        print(f"    Quantity: {row['quantity_sold']}")
        print("-" * 50)

if __name__ == "__main__":
    remove_spaces_from_products() 