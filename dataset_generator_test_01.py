import itertools
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

# Create a list to hold the results
results = []

# Generate combinations of all possible sizes from safe_list
for r in range(1, len(safe_list) + 1):
    for combination in itertools.combinations(safe_list, r):
        combination = list(combination)
        # Combine with unsafe list to create all possible combinations
        for u in range(0, len(unsafe_list) + 1):
            for unsafe_comb in itertools.combinations(unsafe_list, u):
                combined_ingredients = combination + list(unsafe_comb)
                # Check if there is any unsafe ingredient in the combination
                if any(ingredient in unsafe_list for ingredient in combined_ingredients):
                    classification = "Unsafe"
                else:
                    classification = "Safe"

                # Create a dictionary for the current combination
                results.append({
                    "Ingredients": ", ".join(combined_ingredients),
                    "Classification": classification,
                    "Description": ""
                })

# Create a DataFrame
df = pd.DataFrame(results)

# Display or save the DataFrame
# print(df)
df.to_csv("ingredient_classification.csv", index=False) # Uncomment to save to a CSV file