import pandas as pd
import folium
from geopy.geocoders import Nominatim
import time
from tqdm import tqdm  


INPUT_FILE = 'neighborhood_analysis.csv'
OUTPUT_MAP = 'mumbai_real_estate_map.html'
USER_AGENT = 'mumbai_geo_script_v1' 


print(f"Loading data from {INPUT_FILE}...")
try:
    df = pd.read_csv(INPUT_FILE)
except FileNotFoundError:
    print(f"Error: {INPUT_FILE} not found. Please run the analysis script first.")
    exit()


df['Location'] = df['Location'].apply(
    lambda loc: loc.split(' in ')[-1].strip() if len(loc) > 30 else loc
)


df = df.groupby('Location')['Avg_Price_per_SqFt'].mean().sort_values(ascending=False).reset_index()


def get_coordinates(address, geolocator):
    """
    Function to find lat/lon for a given address, with a retry mechanism and timeout.
    """
    retries = 3
    for attempt in range(retries):
        try:
           
            time.sleep(1) 
            location_data = geolocator.geocode(f"{address}, Mumbai, India", timeout=15)
            if location_data:
                return location_data.latitude, location_data.longitude
            
            return None, None
        except Exception as e:
            if attempt < retries - 1:
                print(f"Warning for {address}: {e}. Retrying in 5 seconds...")
                time.sleep(5) 
            else:
                print(f"Final error for {address}: {e}. Giving up.")
                return None, None
    return None, None


geolocator = Nominatim(user_agent=USER_AGENT)
coords = [get_coordinates(loc, geolocator) for loc in tqdm(df['Location'], desc="Geocoding Locations")]


df[['Latitude', 'Longitude']] = pd.DataFrame(coords, index=df.index)
df.dropna(subset=['Latitude', 'Longitude'], inplace=True)

print(f"Successfully geocoded {len(df)} locations.")


mumbai_map = folium.Map(location=[19.0760, 72.8777], zoom_start=11)

def get_color(price):
    """Assigns color based on price tier."""
    if price < 20000: return 'green' 
    if price < 45000: return 'orange'
    return 'red' 


for _, row in df.iterrows():
    folium.Circle(
        location=[row['Latitude'], row['Longitude']],
        radius=400,
        popup=f"<b>{row['Location']}</b><br>Avg. Price/SqFt: ₹{row['Avg_Price_per_SqFt']}",
        color=get_color(row['Avg_Price_per_SqFt']),
        fill=True,
        fill_opacity=0.6
    ).add_to(mumbai_map)

mumbai_map.save(OUTPUT_MAP)
print(f"\nMap generation complete. Output saved to '{OUTPUT_MAP}'")