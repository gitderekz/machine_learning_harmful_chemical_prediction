import random
import pandas as pd
import itertools

# Define the lists
safe_list = ['ALANINE', 'AQUA', 'ARGININE', 'ASPARTIC ACID', 'Allantoin', 'Aloe Vera', 'Ascorbic Acid',
 'Avocado Oil', 'Beeswax', 'Benzyl Alcohol', 'CAPRYLIC/CAPRIC TRIGLYCERIDE', 'CETYL ALCOHOL', 'Calendula Extract',
 'Ceramides', 'Cetearyl Alcohol', 'Chamomile Extract', 'Citric Acid', 'Cocamidopropyl Betaine', 'Cocoa Butter',
 'Coconut Oil', 'Collagen', 'Cucumber Extract', 'Dimethicone', 'Ethylhexylglycerin', 'Eucalyptus Oil', 'FRUCTOSE',
 'GLUCOSE', 'GLYCERIN', 'GLYCINE', 'Glycerin', 'Grapefruit Seed Extract', 'Green Tea Extract', 'HISTIDINE',
 'Hyaluronic Acid', 'ISOLEUCINE', 'Iron Oxides', 'Isopropyl Myristate', 'Jojoba Oil', 'Keratin', 'LINOLEIC ACID',
 'Lactic Acid', 'Lavender Oil', 'MALTOSE', 'Magnesium Sulfate', 'Mica', 'Mineral Oil', 'Niacinamide',
 'Niacinamide (Vitamin B3)', 'OLEIC ACID', 'PALMITIC ACID', 'PCA', 'PHENYLALANINE', 'PHYTOSTERYL CANOLA GLYCERIDES',
 'PROLINE', 'PROPANEDIOL', 'Panthenol', 'Vitamin B5', 'Paraffin', 'Peptides', 'Petrolatum',
 'Phenoxyethanol', 'Retinol', 'Retinyl Palmitate', 'Rose Water', 'SERINE', 'SODIUM LACTATE',
 'Salicylic Acid', 'Shea Butter', 'Silica', 'Sodium Benzoate', 'Sodium Chloride',
 'Sodium Hyaluronate', 'Sodium PCA', 'Soybean Oil', 'Squalane', 'Squalene', 'Stearic Acid', 'Stearyl Alcohol',
 'Sweet Almond Oil', 'THREONINE', 'TREHALOSE', 'Tea Tree Oil', 'Titanium Dioxide', 'UREA', 'VALINE', 'Vitamin E',
 'Water', 'White Tea Extract', 'Witch Hazel', 'Zinc Oxide']
unsafe_list = [
    "Sodium Lauryl Sulfate", "Parfum", "Limonene",
    "Linalool", "Oxybenzone", "Octinoxate", "Homosalate", "Triclosan",
    "Triclocarban", "Formaldehyde", "DMDM Hydantoin", "Quaternium-15",
    "Lead", "Mercury", "Cadmium", "Parabens", "Methylparaben",
    "Propylparaben", "Polyethylene Glycol (PEG)", "Stearate", "Laurate",
    "BHT", "BHA", "Sodium Laureth Sulfate (SLES)", "Cocamide DEA",
    "Butylparaben", "Dibutyl phthalate (DBP)", "Diethyl phthalate (DEP)",
    "Imidazolidinyl urea", "Toluene", "Arsenic", "Hydroquinone",
    "Synthetic musks", "p-phenylenediamine (PPD)", "Coal Tar",
    "Benzene", "Sulfites", "Metabisulfites", "Petroleum Distillates",
    "Aluminum Chlorohydrate", "Fragrance", "Resorcinol", "Methylisothiazolinone",
    "Methylchloroisothiazolinone","Diethanolamine (DEA)", "Triethanolamine (TEA)",
    "Talc","Ammonium Persulfate", "Phenol", "Sodium Hydroxymethylglycinate",
    "Benzalkonium Chloride", "Mercury Compounds",
    "Hexyl Cinnamal", "Isobutane", "Propane","Nitrosamines"
]


# Function to classify combinations
def classify_combination(combination):
    if any(item in unsafe_list for item in combination):
        return 'Unsafe'
    return 'Safe'

# Generate random unique combinations
def generate_combinations(ingredient_list, num_combinations):
    combinations_set = set()
    while len(combinations_set) < num_combinations:
        combination = tuple(sorted(random.sample(ingredient_list, 2)))
        combinations_set.add(combination)
    return list(combinations_set)

# Number of combinations needed
num_safe_combinations = 1000
num_unsafe_combinations = 1000

# Generate safe and unsafe combinations
safe_combinations = generate_combinations(safe_list, num_safe_combinations)
unsafe_combinations = generate_combinations(unsafe_list, num_unsafe_combinations)

# Combine and shuffle
all_combinations = safe_combinations + unsafe_combinations
random.shuffle(all_combinations)

# Prepare dataset
dataset = []
for combination in all_combinations:
    classification = classify_combination(combination)
    ingredients = '; '.join(combination)
    dataset.append([ingredients, classification, 'none'])

# Write to CSV
df = pd.DataFrame(dataset, columns=['Ingredients', 'Classification', 'Description'])
df.to_csv('ingredients_dataset.csv', index=False)