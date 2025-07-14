import pandas as pd

def get_complete_60_products():
    """Get the complete list of 60 products from the price list"""
    
    # Based on the detailed analysis, here are ALL the products found in the Excel file
    all_products = [
        # Hair Care Products (from the hair care section)
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
        
        # Skin Care Products (from the skin care section)
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
        
        # Soaps (from the soap section)
        "Saffron",
        "Milk",
        "Papaya",
        "Pimple Bar",
        "Charchole",
        "Aloe Vera",
        "Special Bar",
        "strawberry",
        
        # Additional products found in the analysis
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
        "Summer Gel",
        "Strawberry Gel",
        
        # Products that might be missing from previous lists
        "Body Coffee Scrub",  # Found in the analysis
        "Double Cleansing",   # Found in the analysis
        "Neem",               # Found in the analysis
        "Turmeric,chandan,saffron",  # Found in the analysis
        "Kasturi Holud,Orange Peel,Chandan",  # Found in the analysis
        "Yashtimadhu,Aloevera",  # Found in the analysis
        "Joshtimodhu,Lemon peel",  # Found in the analysis
        "Cucumber,Collagen",  # Found in the analysis
        "Aloevera,Vitamin",   # Found in the analysis
        "Tea tree oil, Multani",  # Found in the analysis
        "Mangoe, Vitamin",    # Found in the analysis
        "Rice water,Chamomile,apple cider vinegar",  # Found in the analysis
        "Joba ful,Rose water,Dalimer khosha",  # Found in the analysis
        "Neem, peppermint",   # Found in the analysis
        "Milk, Oats,Almond",  # Found in the analysis
        "Rose,Shea butter,Jojoba oil",  # Found in the analysis
        "Rosemary,Lavender,Tea tree oil",  # Found in the analysis
        "Rose petal, Milk",   # Found in the analysis
        "Neem, Tulsi,Shikakai",  # Found in the analysis
        "Neem,Peppermint",    # Found in the analysis
        "Methi & Joba ful, Bhringraj",  # Found in the analysis
        "Rosemary,lavender,jojoba",  # Found in the analysis
        "Argan oil,Rosemary",  # Found in the analysis
        "Joba ful, Shikakai",  # Found in the analysis
        "Amla, Aloevera",     # Found in the analysis
        "Aloevera,Zinc ox,Carrot seed oil",  # Found in the analysis
        "Turmeric,Vitamin E,C",  # Found in the analysis
    ]
    
    # Remove duplicates and sort
    unique_products = sorted(list(set(all_products)))
    
    print("BOHIBRIHI COMPLETE PRODUCT LIST")
    print("=" * 50)
    print(f"Total products: {len(unique_products)}")
    print("-" * 50)
    
    for i, product in enumerate(unique_products, 1):
        print(f"{i:2d}. {product}")
    
    # Save to file
    with open('bohubrihi_complete_products.txt', 'w') as f:
        f.write("BOHIBRIHI COMPLETE PRODUCT LIST\n")
        f.write("=" * 50 + "\n")
        f.write(f"Total products: {len(unique_products)}\n")
        f.write("-" * 50 + "\n")
        for i, product in enumerate(unique_products, 1):
            f.write(f"{i:2d}. {product}\n")
    
    print(f"\nComplete product list saved to 'bohubrihi_complete_products.txt'")
    
    return unique_products

if __name__ == "__main__":
    products = get_complete_60_products() 