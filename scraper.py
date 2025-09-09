import requests
from bs4 import BeautifulSoup
import pandas as pd
import time 


base_url = "https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=Mumbai"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


all_properties_data = []


for page_num in range(1, 21):
    
   
    url = f"{base_url}&page={page_num}"
    print(f"\nScraping Page: {page_num}")
    print(f"URL: {url}")

    
    response = requests.get(url, headers=headers)
    
    
    if response.status_code != 200:
        print(f"Failed to fetch page {page_num}. Status code: {response.status_code}. Moving to next page.")
        continue

    soup = BeautifulSoup(response.content, 'html.parser')
    
   
    property_listings = soup.find_all('div', class_='mb-srp__list')

    
    if not property_listings:
       
        break 
    
    for listing in property_listings:
        try:
            price_tag = listing.find('div', class_='mb-srp__card__price--amount')
            price = price_tag.text.strip() if price_tag else 'N/A'

            title_tag = listing.find('h2', class_='mb-srp__card--title')
            if title_tag:
                title_text = title_tag.text.strip()
                bhk = title_text.split(' ')[0] + " BHK"
                try:
                    location = title_text.split(',')[-2].strip()
                except IndexError:
                    location = title_text.split(',')[-1].strip()
            else:
                bhk, location = 'N/A', 'N/A'

            area_item = listing.find('div', attrs={'data-summary': 'carpet-area'})
            if area_item:
                area_tag = area_item.find('div', class_='mb-srp__card__summary--value')
                area_sqft = area_tag.text.strip() if area_tag else 'N/A'
            else:
                area_sqft = 'N/A'

            if 'N/A' not in [price, bhk, area_sqft, location]:
               
                all_properties_data.append({
                    "Price": price,
                    "BHK": bhk,
                    "Area_SqFt": area_sqft,
                    "Location": location
                })
        except Exception as e:
            continue
            
   
    
    time.sleep(2)





df = pd.DataFrame(all_properties_data)

print("\n--- Scraped Data (First 5 Rows) ---")
if not df.empty:
    print(df.head())
else:
    print("No valid property data was extracted.")
print("\n--- End of Data ---")


df.to_csv('mumbai_properties_raw_data.csv', index=False)
