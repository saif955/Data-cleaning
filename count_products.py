import csv

# Read the CSV file and extract unique products
unique_products = set()

with open('daily_product_sales_filtered.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        unique_products.add(row['product'])

# Count unique products
product_count = len(unique_products)

print(f"Total number of unique products: {product_count}")
print("\nList of all unique products:")
print("=" * 50)

# Sort products alphabetically for better readability
sorted_products = sorted(unique_products)

for i, product in enumerate(sorted_products, 1):
    print(f"{i:3d}. {product}")

print(f"\nTotal unique products: {product_count}") 