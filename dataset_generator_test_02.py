import random
import pandas as pd

# Define the lists
safe_list = [
    "AQUA (WATER)", "CAPRYLIC/CAPRIC TRIGLYCERIDE", "CETYL ALCOHOL", "PROPANEDIOL",
    "STEARYL ALCOHOL", "GLYCERIN", "SODIUM HYALURONATE", "ARGININE", "ASPARTIC ACID",
    "GLYCINE", "ALANINE", "SERINE", "VALINE", "ISOLEUCINE", "PROLINE", "THREONINE",
    "HISTIDINE", "PHENYLALANINE", "GLUCOSE", "MALTOSE", "FRUCTOSE", "TREHALOSE",
    "SODIUM PCA", "PCA", "SODIUM LACTATE", "UREA", "ALLANTOIN", "LINOLEIC ACID",
    "OLEIC ACID", "PHYTOSTERYL CANOLA GLYCERIDES", "PALMITIC ACID", "Petrolatum",
    "Mineral Oil", "Paraffin", "Water", "Glycerin", "Stearic Acid", "Isopropyl Myristate",
    "Coconut Oil", "Shea Butter", "Jojoba Oil", "Aloe Vera", "Vitamin E", "Chamomile Extract",
    "Dimethicone", "Benzyl Alcohol", "Phenoxyethanol", "Ethylhexylglycerin", "Retinol",
    "Retinyl Palmitate", "Ascorbic Acid", "Niacinamide", "Titanium Dioxide", "Zinc Oxide",
    "Tea Tree Oil", "Lavender Oil", "Eucalyptus Oil", "Panthenol (Vitamin B5)",
    "Niacinamide (Vitamin B3)", "Lactic Acid", "Citric Acid", "Salicylic Acid",
    "Green Tea Extract", "Beeswax", "Glycerin;Panthenol;Allantoin",
    "Aloe Vera;Glycerin;Vitamin E", "Water;Sodium PCA;Lactic Acid",
    "Coconut Oil;Aloe Vera;Shea Butter", "Petrolatum;Glycerin;Cetearyl Alcohol",
    "Cetearyl Alcohol;Sodium Hyaluronate;Allantoin", "Water;Glycerin;Niacinamide",
    "Water;Aloe Vera;Allantoin", "Glycerin;Panthenol;Niacinamide",
    "Aloe Vera;Vitamin E;Allantoin", "Coconut Oil;Shea Butter;Vitamin E",
    "Water;Glycerin;Sodium Hyaluronate", "Water;Cetearyl Alcohol;Aloe Vera",
    "Water;Niacinamide;Lactic Acid", "Petrolatum;Mineral Oil;Aloe Vera",
    "Water;Glycerin;Dimethicone", "Coconut Oil;Shea Butter;Allantoin",
    "Water;Niacinamide;Vitamin E", "Aloe Vera;Panthenol;Allantoin",
    "Water;Glycerin;Chamomile Extract", "Water;Sodium Hyaluronate;Niacinamide",
    "Cetearyl Alcohol;Dimethicone;Allantoin", "Glycerin;Panthenol;Aloe Vera",
    "Water;Cetearyl Alcohol;Shea Butter", "Water;Glycerin;Shea Butter",
    "Coconut Oil;Aloe Vera;Vitamin E", "Water;Glycerin;Panthenol",
    "Water;Niacinamide;Allantoin", "Aloe Vera;Chamomile Extract;Vitamin E",
    "Water;Sodium Hyaluronate;Chamomile Extract", "Cetearyl Alcohol;Glycerin;Dimethicone",
    "Water;Cetearyl Alcohol;Panthenol", "Water;Shea Butter;Allantoin",
    "Petrolatum;Mineral Oil;Dimethicone", "Coconut Oil;Aloe Vera;Niacinamide",
    "Water;Niacinamide;Chamomile Extract", "Aloe Vera;Glycerin;Vitamin E",
    "Cetearyl Alcohol;Glycerin;Allantoin", "Water;Sodium Hyaluronate;Panthenol",
    "Coconut Oil;Avocado Oil", "Keratin;Collagen", "Soybean Oil;Sweet Almond Oil",
    "Sodium Benzoate", "Witch Hazel;Rose Water", "Isopropyl Myristate",
    "Mica;Iron Oxides", "Sodium Chloride;Magnesium Sulfate",
    "Cetearyl Alcohol;Stearyl Alcohol", "Green Tea Extract;White Tea Extract",
    "Calendula Extract;Chamomile Extract", "Grapefruit Seed Extract",
    "Cocoa Butter;Shea Butter", "Squalane;Squalene", "Aloe Vera;Cucumber Extract",
    "Hyaluronic Acid;Glycerin", "Peptides;Ceramides", "Silica;Dimethicone",
    "Cocamidopropyl Betaine"
]
unsafe_list = [
    "Sodium Lauryl Sulfate", "Cocamidopropyl Betaine", "Parfum", "Limonene",
    "Linalool", "Oxybenzone", "Octinoxate", "Homosalate", "Triclosan",
    "Triclocarban", "Formaldehyde", "DMDM Hydantoin", "Quaternium-15",
    "Lead", "Mercury", "Cadmium", "Parabens", "Methylparaben",
    "Propylparaben", "Polyethylene Glycol (PEG)", "Stearate", "Laurate",
    "BHT", "BHA", "Sodium Laureth Sulfate (SLES)", "Cocamide DEA",
    "Butylparaben", "Dibutyl phthalate (DBP)", "Diethyl phthalate (DEP)",
    "Imidazolidinyl urea", "Toluene", "Arsenic", "Hydroquinone",
    "Synthetic musks", "p-phenylenediamine (PPD)", "Coal Tar",
    "Benzene", "Sulfites", "Metabisulfites", "Petroleum Distillates",
    "Aluminum Chlorohydrate", "Fragrance", "Resorcinol",
    "DEA (Diethanolamine)", "Triclosan", "Methylisothiazolinone",
    "Methylchloroisothiazolinone", "Polyethylene Glycol (PEG) Compounds",
    "Diethanolamine (DEA)", "Triethanolamine (TEA)", "Talc",
    "Ammonium Persulfate", "Phenol", "Sodium Hydroxymethylglycinate",
    "Benzalkonium Chloride", "Mercury Compounds", "Mineral Oil",
    "Paraffin", "Hexyl Cinnamal", "Formaldehyde", "Isobutane", "Propane",
    "Nitrosamines"
]


# Function to classify combinations
def classify_combination(combination):
    if any(item in unsafe_list for item in combination):
        return 'Unsafe'
    return 'Safe'


# Generate random unique combinations
def generate_combinations(safe_list, unsafe_list, num_combinations):
    all_ingredients = safe_list + unsafe_list
    combinations_set = set()

    while len(combinations_set) < num_combinations:
        combination = tuple(sorted(random.sample(all_ingredients, 6)))
        combinations_set.add(combination)

    return list(combinations_set)


# Generate 1000 unique combinations
num_combinations = 9000
combinations = generate_combinations(safe_list, unsafe_list, num_combinations)

# Prepare dataset
dataset = []
for combination in combinations:
    classification = classify_combination(combination)
    ingredients = ', '.join(combination)
    dataset.append([ingredients, classification, ''])

# Write to CSV
df = pd.DataFrame(dataset, columns=['Ingredients', 'Classification', 'Description'])
df.to_csv('ingredients_dataset.csv', index=False)