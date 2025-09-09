import pandas as pd
import numpy as np


try:
    df = pd.read_csv('mumbai_properties_raw_data.csv')
    
except FileNotFoundError:
    print("Error: Input file not found.")
    exit()


def parse_price(p):
    if not isinstance(p, str):
        return np.nan
    
    p = p.lower().replace('₹', '').replace(',', '').strip()
    
    try:
        if 'cr' in p:
            # 1e7 is a common shorthand for 10,000,000
            return float(p.replace('cr', '')) * 1e7 
        elif 'lac' in p:
            return float(p.replace('lac', '')) * 1e5
        else:
            return float(p)
    except ValueError:
        return np.nan

df['Price'] = df['Price'].apply(parse_price)


df['Area_SqFt'] = pd.to_numeric(df['Area_SqFt'].str.replace(' sqft', '').str.strip(), errors='coerce')
df['BHK'] = pd.to_numeric(df['BHK'].str.replace(' BHK', '').str.strip(), errors='coerce')



df.dropna(inplace=True)




df.to_csv('mumbai_properties_cleaned.csv', index=False)
