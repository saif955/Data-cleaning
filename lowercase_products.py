import pandas as pd

# Read the cleaned CSV file
df = pd.read_csv('daily_product_sales_cleaned.csv')

print("Before converting to lowercase:")
print(f"Total rows: {len(df)}")
print(f"Unique products: {len(df['product'].unique())}")

# Show some examples before conversion
print("\nSample products before conversion:")
for i, product in enumerate(df['product'].unique()[:10], 1):
    print(f"{i:2d}. {product}")

# Convert product names to lowercase
df['product'] = df['product'].str.lower()

print("\nAfter converting to lowercase:")
print(f"Total rows: {len(df)}")
print(f"Unique products: {len(df['product'].unique())}")

# Show some examples after conversion
print("\nSample products after conversion:")
for i, product in enumerate(df['product'].unique()[:10], 1):
    print(f"{i:2d}. {product}")

# Show the final structure
print("\nFinal structure:")
print("=" * 80)
print(df[['date', 'product', 'amount', 'quantity_sold']].head(15).to_string(index=False))

# Save the lowercase data
output_file = 'daily_product_sales_lowercase.csv'
df.to_csv(output_file, index=False)
print(f"\nLowercase data saved to '{output_file}'")

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