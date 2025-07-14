import pandas as pd
from spellchecker import SpellChecker
from autocorrect import Speller
import re

# Initialize spell checkers
spell = SpellChecker()
autocorrect_speller = Speller()

def clean_product_name(product_name):
    """Clean and standardize product name"""
    # Remove extra spaces and standardize
    cleaned = re.sub(r'\s+', ' ', product_name.strip())
    return cleaned

def fix_spelling_in_product(product_name):
    """Fix spelling in product name while preserving structure"""
    # Split by spaces to handle each word
    words = product_name.split()
    corrected_words = []
    
    for word in words:
        # Skip words with numbers, measurements, or special characters
        if any(char.isdigit() for char in word) or any(char in 'mlgkt-' for char in word.lower()):
            corrected_words.append(word)
            continue
            
        # Check if word needs correction
        if word.lower() in spell:
            corrected_words.append(word)
        else:
            # Try to correct the word
            corrected = autocorrect_speller(word)
            corrected_words.append(corrected)
    
    return ' '.join(corrected_words)

def main():
    # Read the CSV file
    df = pd.read_csv('daily_product_sales.csv')
    
    print("Original unique products count:", len(df['product'].unique()))
    print("\nAnalyzing spelling issues...")
    
    # Get unique products
    unique_products = df['product'].unique()
    
    # Dictionary to store corrections
    corrections = {}
    
    for product in unique_products:
        cleaned = clean_product_name(product)
        corrected = fix_spelling_in_product(cleaned)
        
        if cleaned != corrected:
            corrections[product] = corrected
            print(f"Original: {product}")
            print(f"Corrected: {corrected}")
            print("-" * 50)
    
    print(f"\nTotal corrections found: {len(corrections)}")
    
    # Apply corrections to the dataframe
    if corrections:
        df['product'] = df['product'].replace(corrections)
        
        # Save corrected data
        df.to_csv('daily_product_sales_corrected.csv', index=False)
        print("\nCorrected data saved to 'daily_product_sales_corrected.csv'")
        
        # Show summary
        print(f"Corrected unique products count: {len(df['product'].unique())}")
        
        # Show some examples of corrections
        print("\nSample corrections applied:")
        for original, corrected in list(corrections.items())[:10]:
            print(f"  {original} → {corrected}")
    else:
        print("\nNo spelling corrections needed!")

if __name__ == "__main__":
    main() 