import pandas as pd

# Read the CSV file with amounts separated
df = pd.read_csv('daily_product_sales_with_amounts.csv')

print("Before cleanup:")
print(f"Columns: {list(df.columns)}")
print(f"Total rows: {len(df)}")
print(f"Unique products: {len(df['product'].unique())}")

# Replace the product column with product_clean
df['product'] = df['product_clean']

# Remove the product_clean column
df = df.drop('product_clean', axis=1)

print("\nAfter cleanup:")
print(f"Columns: {list(df.columns)}")
print(f"Total rows: {len(df)}")
print(f"Unique products: {len(df['product'].unique())}")

# Show sample of the cleaned data
print("\nSample of cleaned data:")
print("=" * 80)
print(df[['date', 'product', 'amount', 'quantity_sold']].head(15).to_string(index=False))

# Save the cleaned data
output_file = 'daily_product_sales_cleaned.csv'
df.to_csv(output_file, index=False)
print(f"\nCleaned data saved to '{output_file}'")

# Show statistics
print(f"\nStatistics:")
print(f"Products with amounts: {(df['amount'].notna()).sum()}")
print(f"Products without amounts: {(df['amount'].isna()).sum()}")
print(f"Total unique products: {len(df['product'].unique())}")

# Show some examples of the final structure
print(f"\nFinal structure examples:")
print("=" * 80)
for i, row in df.head(10).iterrows():
    print(f"{i+1:2d}. Product: {row['product']}")
    print(f"    Amount: {row['amount'] if pd.notna(row['amount']) else 'None'}")
    print(f"    Quantity: {row['quantity_sold']}")
    print("-" * 50) 