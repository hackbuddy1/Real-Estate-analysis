# Mumbai Real Estate Analysis & Visualization

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)

A comprehensive data analysis project that scrapes real estate data for Mumbai, cleans it, performs analysis to determine property value by neighborhood, and visualizes the results on an interactive map.

![Screenshot of the Map](./output/mumbai_real_estate_map.png)
*(Note: Aapko map ka screenshot lekar 'output' folder mein save karna hoga aur yahan link karna hoga)*

---

## 📋 Table of Contents
- [Project Description](#-project-description)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [How to Run](#-how-to-run)
- [Future Improvements](#-future-improvements)
- [License](#-license)

---

## 📖 Project Description

This project provides an end-to-end workflow for a real estate data analysis task. The primary goal is to identify the most expensive and most affordable neighborhoods in Mumbai based on the average price per square foot.

The project workflow is as follows:
1.  **Scraping:** Data is scraped from a real estate website.
2.  **Cleaning:** The raw data is cleaned and pre-processed to handle inconsistencies, convert data types, and prepare it for analysis.
3.  **Analysis:** A key metric, "Price per Square Foot," is calculated. The data is then aggregated by neighborhood to find the average value.
4.  **Visualization:** The analyzed data is geocoded to get latitude and longitude for each neighborhood and then plotted on an interactive Folium map to visually represent the findings.

---

## ✨ Features

- **Web Scraping:** Dynamically scrapes property listings.
- **Data Cleaning:** Robust functions to handle messy real-world data (e.g., '1.5 Cr', '50 Lac').
- **Geospatial Analysis:** Converts location names into geographical coordinates.
- **Interactive Visualization:** Generates an interactive HTML map with color-coded markers based on property value.
- **Reproducible Workflow:** The project is structured with separate scripts for each phase, making it easy to understand and reproduce.

---

## 💻 Tech Stack

- **Language:** Python 3.9+
- **Data Manipulation:** Pandas, NumPy
- **Web Scraping:** Requests, BeautifulSoup4
- **Geocoding & Mapping:** Geopy, Folium
- **Utilities:** Tqdm

---

## 📂 Project Structure

The project is organized into a clean and scalable structure.
RealEstateAnalysis/
├── .gitignore
├── requirements.txt
|
├── data/
│ ├── raw/
│ │ └── mumbai_properties_raw_data.csv
│ └── processed/
│ ├── mumbai_properties_cleaned.csv
│ └── neighborhood_analysis.csv
|
├── output/
│ └── mumbai_real_estate_map.html
|
├── src/
│ ├── data_scraper.py
│ ├── data_cleaner.py
│ ├── data_analyzer.py
│ └── map_visualizer.py
│
└── venv/


## 🚀 How to Run

Follow these steps to set up and run the project on your local machine.

**1. Clone the Repository**
```
git clone https://github.com/hackbuddy1/Real-Estate-analysis
cd Real-Estate-analysis
```
2. Create and Activate Virtual Environment
Windows:
```
python -m venv venv
.\venv\Scripts\activate
```
macOS / Linux:
```
python3 -m venv venv
source venv/bin/activate
```
4. Install Dependencies
```
pip install -r requirements.txt
```
5. Run the Scripts in Order
Execute the scripts from the root directory of the project in the following sequence:
```
# Step 1: Scrape the raw data (if needed)
python src/data_scraper.py

# Step 2: Clean the raw data
python src/data_cleaner.py

# Step 3: Analyze the cleaned data
python src/data_analyzer.py

# Step 4: Generate the interactive map
python src/map_visualizer.py
```
After running, the cleaned files will be in data/processed/ and the final map will be in the output/ folder.

💡 Future Improvements
Integrate more data sources to enrich the analysis.
Build a simple web interface (e.g., using Streamlit or Flask) to display the map and insights.
Apply machine learning models to predict property prices based on features like location, area, and BHK.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.
