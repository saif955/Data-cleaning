import pandas as pd

def filter_products_by_official_list():
    """Filter daily product sales to only include products from the official product list"""
    
    # Read the official product list
    print("Reading official product list...")
    product_list_df = pd.read_csv('bohubrihi_product_list.csv')
    official_products = set(product_list_df['product'].str.lower().str.strip())
    
    print(f"Official product list contains {len(official_products)} products")
    
    # Read the cleaned sales data
    print("Reading cleaned sales data...")
    sales_df = pd.read_csv('daily_product_sales_cleaned.csv')
    
    print(f"Original sales data has {len(sales_df)} rows")
    print(f"Original sales data has {len(sales_df['product'].unique())} unique products")
    
    # Create a copy for filtering
    filtered_df = sales_df.copy()
    
    # Add a column to track if product is in official list
    filtered_df['is_official_product'] = filtered_df['product'].str.lower().str.strip().isin(official_products)
    
    # Show products that are NOT in the official list
    unofficial_products = filtered_df[~filtered_df['is_official_product']]['product'].unique()
    
    print(f"\nProducts NOT in official list ({len(unofficial_products)}):")
    print("=" * 60)
    for i, product in enumerate(sorted(unofficial_products), 1):
        print(f"{i:3d}. {product}")
    
    # Filter to only include official products
    official_sales_df = filtered_df[filtered_df['is_official_product']].copy()
    
    # Remove the tracking column
    official_sales_df = official_sales_df.drop('is_official_product', axis=1)
    
    print(f"\nFiltering results:")
    print(f"Original rows: {len(sales_df)}")
    print(f"Filtered rows: {len(official_sales_df)}")
    print(f"Removed rows: {len(sales_df) - len(official_sales_df)}")
    print(f"Original unique products: {len(sales_df['product'].unique())}")
    print(f"Filtered unique products: {len(official_sales_df['product'].unique())}")
    
    # Save the filtered data
    output_file = 'daily_product_sales_filtered.csv'
    official_sales_df.to_csv(output_file, index=False)
    print(f"\nFiltered data saved to '{output_file}'")
    
    # Show summary of remaining products
    print(f"\nRemaining official products in sales data:")
    print("=" * 60)
    remaining_products = sorted(official_sales_df['product'].unique())
    for i, product in enumerate(remaining_products, 1):
        print(f"{i:2d}. {product}")
    
    # Show some statistics
    print(f"\nSales statistics for official products:")
    print("=" * 60)
    product_stats = official_sales_df.groupby('product').agg({
        'quantity_sold': ['sum', 'count'],
        'amount': 'count'
    }).round(2)
    
    product_stats.columns = ['Total_Quantity', 'Sales_Count', 'Amount_Records']
    product_stats = product_stats.sort_values('Total_Quantity', ascending=False)
    
    print(product_stats.head(15))
    
    return official_sales_df

if __name__ == "__main__":
    filtered_data = filter_products_by_official_list() 