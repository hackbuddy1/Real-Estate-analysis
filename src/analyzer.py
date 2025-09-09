import pandas as pd

try:
    df = pd.read_csv('mumbai_properties_cleaned.csv')
    
except FileNotFoundError:
    print("Error: 'mumbai_properties_cleaned.csv' not found.")
    exit()


df['Price_per_SqFt'] = (df['Price'] / df['Area_SqFt']).round(2)

loc_analysis = (df.groupby('Location')['Price_per_SqFt']
.mean()
.round(2)
.sort_values(ascending=False)
.reset_index()
.rename(columns={'Price_per_SqFt': 'Avg_Price_per_SqFt'}))


print("\nTop 10 Most Expensive Locations (by Avg. Price/SqFt):")
print(loc_analysis.head(10))

loc_analysis.to_csv('neighborhood_analysis.csv', index=False)