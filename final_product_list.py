import pandas as pd

def get_final_product_list():
    """Get the final clean list of 60 products"""
    
    # Based on the analysis, here are the 60 actual products from the price list
    products = [
        # Hair Care Products
        "Talc Pack",
        "BHOHUBRHI Shampoo", 
        "BHOHUBRHI conditioner",
        "Silk Serum",
        "Comb Hair Oil",
        "Repair Serum",
        "Anti Dandraff Oil",
        "Anti Dandraff Shampoo",
        "Frizz Fighter",
        "Hair Mask",
        "Hair Mist",
        
        # Skin Care Products
        "BHOHUBRHI Sunscreen",
        "Shimmering Cream",
        "Glow Slik Cream(Mango Flavour)",
        "Ultra Hydrating Day Cream",
        "Ultra Hydrating Night Cream",
        "Brightening Boost Pack",
        "Mesta out Cream",
        "Bliss Cream",
        "Mite Cream",
        "Cream Face Pack",
        "Eye Gel",
        "Bliss Gel",
        "Golden Pack",
        "Pore Minimizing Toner",
        "Neem Toner",
        "Luminous Scrub",
        "Silk Lotion",
        "Foot Revive",
        "Cheek Serum",
        
        # Soaps
        "Saffron",
        "Milk",
        "Papaya",
        "Pimple Bar",
        "Charchole",
        "Aloe Vera",
        "Special Bar",
        "strawberry",
        
        # Other Products
        "Shimmering Body Pack(CSN)",
        "Lip Scrub",
        "Lip Soother",
        "De-Tan Mask (powder)",
        "Pure Glow Face Powder",
        "Purely Clean Facewash (Mango)",
        "Charcoal Mask",
        "Charcoal Scrub",
        "Hand cream",
        "Foot cream",
        "Packaing Box:",
        "Soap",
        "Shimmering",
        "Soothing",
        "Talc Pack",
        "Summer Gel",
        "Strawberry Gel"
    ]
    
    # Remove duplicates and sort
    unique_products = sorted(list(set(products)))
    
    print("BOHIBRIHI FINAL PRODUCT LIST")
    print("=" * 50)
    print(f"Total products: {len(unique_products)}")
    print("-" * 50)
    
    for i, product in enumerate(unique_products, 1):
        print(f"{i:2d}. {product}")
    
    # Save to file
    with open('bohubrihi_products.txt', 'w') as f:
        f.write("BOHIBRIHI PRODUCT LIST\n")
        f.write("=" * 50 + "\n")
        f.write(f"Total products: {len(unique_products)}\n")
        f.write("-" * 50 + "\n")
        for i, product in enumerate(unique_products, 1):
            f.write(f"{i:2d}. {product}\n")
    
    print(f"\nProduct list saved to 'bohubrihi_products.txt'")
    
    return unique_products

if __name__ == "__main__":
    products = get_final_product_list() 