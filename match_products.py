import pandas as pd

def match_products():
    """Match price list products with sales data"""
    
    # Read the latest sales CSV (lowercase version)
    try:
        sales_df = pd.read_csv('daily_product_sales_lowercase.csv')
        print("Using lowercase sales data")
    except FileNotFoundError:
        try:
            sales_df = pd.read_csv('daily_product_sales_cleaned.csv')
            print("Using cleaned sales data")
        except FileNotFoundError:
            sales_df = pd.read_csv('daily_product_sales.csv')
            print("Using original sales data")
    
    # Get unique products from sales data
    sales_products = set(sales_df['product'].unique())
    
    # Get products from price list (from the detailed analysis)
    price_list_products = [
        # Hair Care Products
        "Talc Pack", "BHOHUBRHI Shampoo", "BHOHUBRHI conditioner", "Silk Serum",
        "Comb Hair Oil", "Repair Serum", "Anti Dandraff Oil", "Anti Dandraff Shampoo",
        "Frizz Fighter", "Hair Mask", "Hair Mist",
        
        # Skin Care Products  
        "BHOHUBRHI Sunscreen", "Shimmering Cream", "Glow Slik Cream(Mango Flavour)",
        "Ultra Hydrating Day Cream", "Ultra Hydrating Night Cream", "Brightening Boost Pack",
        "Mesta out Cream", "Bliss Cream", "Mite Cream", "Cream Face Pack", "Eye Gel",
        "Bliss Gel", "Golden Pack", "Pore Minimizing Toner", "Neem Toner", "Luminous Scrub",
        "Silk Lotion", "Foot Revive", "Cheek Serum",
        
        # Soaps
        "Saffron", "Milk", "Papaya", "Pimple Bar", "Charchole", "Aloe Vera", "Special Bar", "strawberry",
        
        # Additional products
        "Shimmering Body Pack(CSN)", "Lip Scrub", "Lip Soother", "De-Tan Mask (powder)",
        "Pure Glow Face Powder", "Purely Clean Facewash (Mango)", "Charcoal Mask", "Charcoal Scrub",
        "Hand cream", "Foot cream", "Packaing Box:", "Soap", "Shimmering", "Soothing",
        "Summer Gel", "Strawberry Gel", "Body Coffee Scrub", "Double Cleansing", "Neem",
        "Turmeric,chandan,saffron", "Kasturi Holud,Orange Peel,Chandan", "Yashtimadhu,Aloevera",
        "Joshtimodhu,Lemon peel", "Cucumber,Collagen", "Aloevera,Vitamin", "Tea tree oil, Multani",
        "Mangoe, Vitamin", "Rice water,Chamomile,apple cider vinegar", "Joba ful,Rose water,Dalimer khosha",
        "Neem, peppermint", "Milk, Oats,Almond", "Rose,Shea butter,Jojoba oil",
        "Rosemary,Lavender,Tea tree oil", "Rose petal, Milk", "Neem, Tulsi,Shikakai",
        "Neem,Peppermint", "Methi & Joba ful, Bhringraj", "Rosemary,lavender,jojoba",
        "Argan oil,Rosemary", "Joba ful, Shikakai", "Amla, Aloevera",
        "Aloevera,Zinc ox,Carrot seed oil", "Turmeric,Vitamin E,C"
    ]
    
    # Convert price list products to lowercase for comparison
    price_list_lower = {product.lower() for product in price_list_products}
    
    print("PRODUCT MATCHING ANALYSIS")
    print("=" * 60)
    print(f"Total products in price list: {len(price_list_products)}")
    print(f"Total products in sales data: {len(sales_products)}")
    
    # Find matching products
    matching_products = sales_products.intersection(price_list_lower)
    
    # Find products in sales but not in price list
    sales_only = sales_products - price_list_lower
    
    # Find products in price list but not in sales
    price_only = price_list_lower - sales_products
    
    print(f"\nMatching products: {len(matching_products)}")
    print(f"Products in sales only: {len(sales_only)}")
    print(f"Products in price list only: {len(price_only)}")
    
    # Show matching products
    print(f"\nMATCHING PRODUCTS ({len(matching_products)}):")
    print("-" * 60)
    for i, product in enumerate(sorted(matching_products), 1):
        print(f"{i:2d}. {product}")
    
    # Show products in sales but not in price list
    print(f"\nPRODUCTS IN SALES BUT NOT IN PRICE LIST ({len(sales_only)}):")
    print("-" * 60)
    for i, product in enumerate(sorted(sales_only), 1):
        print(f"{i:2d}. {product}")
    
    # Show products in price list but not in sales
    print(f"\nPRODUCTS IN PRICE LIST BUT NOT IN SALES ({len(price_only)}):")
    print("-" * 60)
    for i, product in enumerate(sorted(price_only), 1):
        print(f"{i:2d}. {product}")
    
    # Create a summary report
    print(f"\nSUMMARY REPORT")
    print("=" * 60)
    print(f"Price List Products: {len(price_list_products)}")
    print(f"Sales Products: {len(sales_products)}")
    print(f"Matching: {len(matching_products)}")
    print(f"Sales Only: {len(sales_only)}")
    print(f"Price List Only: {len(price_only)}")
    print(f"Match Rate: {len(matching_products)/len(sales_products)*100:.1f}%")
    
    # Save detailed report
    with open('product_matching_report.txt', 'w') as f:
        f.write("PRODUCT MATCHING REPORT\n")
        f.write("=" * 60 + "\n")
        f.write(f"Price List Products: {len(price_list_products)}\n")
        f.write(f"Sales Products: {len(sales_products)}\n")
        f.write(f"Matching: {len(matching_products)}\n")
        f.write(f"Sales Only: {len(sales_only)}\n")
        f.write(f"Price List Only: {len(price_only)}\n")
        f.write(f"Match Rate: {len(matching_products)/len(sales_products)*100:.1f}%\n\n")
        
        f.write("MATCHING PRODUCTS:\n")
        f.write("-" * 30 + "\n")
        for product in sorted(matching_products):
            f.write(f"- {product}\n")
        
        f.write(f"\nSALES ONLY PRODUCTS:\n")
        f.write("-" * 30 + "\n")
        for product in sorted(sales_only):
            f.write(f"- {product}\n")
        
        f.write(f"\nPRICE LIST ONLY PRODUCTS:\n")
        f.write("-" * 30 + "\n")
        for product in sorted(price_only):
            f.write(f"- {product}\n")
    
    print(f"\nDetailed report saved to 'product_matching_report.txt'")
    
    return matching_products, sales_only, price_only

if __name__ == "__main__":
    matching, sales_only, price_only = match_products() 