import os
import re
import json
import csv

# Path to the parcel-list directory
PARCEL_LIST_DIR = r"./BOHUBRIHI Slack export Apr 10 2025 - Jun 9 2025/parcel-list"

# Regex to match product lines (e.g., "Soffron goat milk soap 20gm 2pc" or "1.Strawberry Soap 60gm 2ta")
PRODUCT_LINE_REGEX = re.compile(r"^(?:\d+\.)?\s*([A-Za-z0-9 \-]+?)(?:\s+\d{1,3}gm)?\s+(\d+)(?:pc|ta)?$", re.IGNORECASE)

def extract_products(text):
    products = []
    lines = text.splitlines()
    in_product_list = False
    for line in lines:
        if "product list" in line.lower():
            in_product_list = True
            continue
        if in_product_list:
            if not line.strip() or "total" in line.lower() or "due" in line.lower():
                break
            match = PRODUCT_LINE_REGEX.match(line.strip())
            if match:
                product = match.group(1).strip()
                qty = int(match.group(2))
                products.append((product, qty))
    return products

# Collect all results: {date: {product: total_qty}}
results = {}

for filename in os.listdir(PARCEL_LIST_DIR):
    if filename.endswith(".json"):
        date = filename.replace(".json", "")
        results.setdefault(date, {})
        with open(os.path.join(PARCEL_LIST_DIR, filename), "r", encoding="utf-8") as f:
            data = json.load(f)
            for msg in data:
                text = msg.get("text", "")
                for product, qty in extract_products(text):
                    results[date][product] = results[date].get(product, 0) + qty

# Write to CSV
with open("daily_product_sales.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["date", "product", "quantity_sold"])
    for date in sorted(results):
        for product, qty in results[date].items():
            writer.writerow([date, product, qty])

print("CSV file 'daily_product_sales.csv' has been created.") 