import pandas as pd

# Read the CSV file with amounts separated
df = pd.read_csv('daily_product_sales_with_amounts.csv')

print("PRODUCT_CLEAN COLUMN ANALYSIS")
print("=" * 60)

print(f"Total rows: {len(df)}")
print(f"Unique original products: {len(df['product'].unique())}")
print(f"Unique clean products: {len(df['product_clean'].unique())}")

print("\n" + "=" * 60)
print("EXAMPLES OF PRODUCT_CLEAN vs ORIGINAL PRODUCT")
print("=" * 60)

# Show examples where product_clean differs from original product
differences = df[df['product'] != df['product_clean']].head(20)

if len(differences) > 0:
    for i, row in differences.iterrows():
        print(f"Original: {row['product']}")
        print(f"Clean:    {row['product_clean']}")
        print(f"Amount:   {row['amount']}")
        print("-" * 50)
else:
    print("No differences found - all products are the same")

print("\n" + "=" * 60)
print("UNIQUE PRODUCT_CLEAN VALUES")
print("=" * 60)

# Show all unique product_clean values
unique_clean_products = sorted(df['product_clean'].unique())
print(f"Total unique clean products: {len(unique_clean_products)}")

for i, product in enumerate(unique_clean_products, 1):
    count = (df['product_clean'] == product).sum()
    print(f"{i:3d}. {product} ({count} times)")

print("\n" + "=" * 60)
print("PRODUCTS WITH NO AMOUNT (product_clean = product)")
print("=" * 60)

# Show products that have no amount (product_clean equals original product)
no_amount_products = df[df['amount'].isna()]['product_clean'].unique()
print(f"Products without amounts: {len(no_amount_products)}")

for i, product in enumerate(sorted(no_amount_products), 1):
    count = (df['product_clean'] == product).sum()
    print(f"{i:3d}. {product} ({count} times)") 