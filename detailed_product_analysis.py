import pandas as pd

def detailed_product_analysis():
    """Detailed analysis to find all 60 products"""
    try:
        # Read the Excel file
        df = pd.read_excel('BOHIBRIHI Price List.xlsx')
        
        print("DETAILED PRODUCT ANALYSIS")
        print("=" * 60)
        
        # Get all non-empty string values
        all_values = []
        for col in df.columns:
            for value in df[col].dropna():
                if isinstance(value, str):
                    all_values.append(value.strip())
        
        # Remove duplicates and sort
        unique_values = sorted(list(set(all_values)))
        
        print(f"Total unique text values: {len(unique_values)}")
        print("\nALL UNIQUE VALUES FOUND:")
        print("=" * 60)
        
        for i, value in enumerate(unique_values, 1):
            print(f"{i:3d}. {value}")
        
        # Now let's identify what might be products
        print(f"\n" + "=" * 60)
        print("POTENTIAL PRODUCTS (filtered):")
        print("=" * 60)
        
        potential_products = []
        skip_keywords = [
            'serial', 'product name', 'trial pack', 'regular pack', 'benefits', 
            'ingredients', 'weight', 'inside dhaka', 'outside dhaka', 'packaging',
            'unit', 'nan', 'hair care products', 'skin care products', '50ml/gm',
            '120ml/gm', '30gm', '75gm', '20gm', '60gm', '100gm', 'trail pack'
        ]
        
        for value in unique_values:
            # Skip if it contains skip keywords
            if not any(skip in value.lower() for skip in skip_keywords):
                # Check if it looks like a product
                if (len(value) > 2 and 
                    any(keyword in value.lower() for keyword in [
                        'shampoo', 'cream', 'oil', 'serum', 'soap', 'pack', 'mask', 
                        'gel', 'toner', 'face', 'hair', 'bar', 'wash', 'powder', 'mist',
                        'saffron', 'milk', 'papaya', 'charcoal', 'pimple', 'neem', 'aloe',
                        'strawberry', 'summer', 'golden', 'brightening', 'shimmering',
                        'ultra', 'hydrating', 'day', 'night', 'foot', 'hand', 'eye',
                        'cheek', 'repair', 'anti', 'dandruff', 'frizz', 'comb', 'silk',
                        'bliss', 'mite', 'mesta', 'pure', 'pore', 'de-tan', 'glow'
                    ])):
                    potential_products.append(value)
        
        print(f"Found {len(potential_products)} potential products:")
        print("-" * 60)
        
        for i, product in enumerate(potential_products, 1):
            print(f"{i:2d}. {product}")
        
        # Let's also look at the data row by row to see what we might be missing
        print(f"\n" + "=" * 60)
        print("ROW-BY-ROW ANALYSIS:")
        print("=" * 60)
        
        for i, row in df.iterrows():
            row_values = []
            for value in row:
                if isinstance(value, str) and len(value.strip()) > 2:
                    row_values.append(value.strip())
            
            if row_values:
                print(f"Row {i+1}: {row_values}")
        
        return potential_products
        
    except Exception as e:
        print(f"Error: {e}")
        return []

if __name__ == "__main__":
    products = detailed_product_analysis() 