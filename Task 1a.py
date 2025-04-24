
import pandas as pd
import json
import os
import matplotlib.pyplot as plt
import seaborn as sns
def main():
    # Read the TSV data
    print("Loading data...")
    df = pd.read_csv('final_haunted_places.tsv', sep='\t')

import pandas as pd
import json
import os
import matplotlib.pyplot as plt
from pathlib import Path

def main():
    """
    Main function to process the haunted places dataset and convert it to JSON
    for D3 visualizations.
    """
    # Read the TSV data
    print("Loading data...")
    df = pd.read_csv('final_haunted_places.tsv', sep='\t')

    # Display basic information about the dataset
    print(f"Loaded {len(df)} haunted place records")
    print(f"Columns available: {', '.join(df.columns)}")

    # Create output directories if they don't exist
    os.makedirs('data/json', exist_ok=True)
    os.makedirs('visualizations', exist_ok=True)

    # Clean and prepare the data
    df = clean_data(df)

    # Generate JSON files for D3 visualizations
    generate_json_files(df)

    print("Data processing complete. JSON files have been created in the 'data/json' directory.")


def clean_data(df):
    """
    Clean and prepare the dataset for visualization.

    Args:
        df (pandas.DataFrame): The raw haunted places dataset

    Returns:
        pandas.DataFrame: The cleaned dataset
    """
    # Fill missing values with appropriate defaults
    if 'latitude' in df.columns and 'longitude' in df.columns:
        # Only keep rows with valid coordinates for map visualizations
        df_geo = df.dropna(subset=['latitude', 'longitude'])
        print(f"Rows with valid geo coordinates: {len(df_geo)} out of {len(df)}")

    # Convert latitude and longitude to numeric
    if 'latitude' in df.columns and 'longitude' in df.columns:
        df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
        df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')

    # Extract location type from description if not available
    if 'location_type' not in df.columns and 'description' in df.columns:
        # Common location types to look for in descriptions
        location_types = ['house', 'hospital', 'cemetery', 'hotel', 'school',
                          'church', 'bridge', 'road', 'forest', 'theater', 'prison']

        # Function to extract location type from description
        def extract_location_type(desc):
            if not isinstance(desc, str):
                return 'unknown'
            desc = desc.lower()
            for loc_type in location_types:
                if loc_type in desc:
                    return loc_type
            return 'other'

        df['location_type'] = df['description'].apply(extract_location_type)

    # Clean city names if present
    if 'city' in df.columns:
        df['city'] = df['city'].str.strip().str.title()

    # Clean state names if present
    if 'state' in df.columns:
        df['state'] = df['state'].str.strip().str.title()

    return df


def generate_json_files(df):
    """
    Generate JSON files for D3 visualizations.

    Args:
        df (pandas.DataFrame): The cleaned haunted places dataset
    """
    # 1. Full dataset for reference
    df.to_json('data/json/haunted_places_full.json', orient='records')

    # 2. Geographic data for map visualization
    if 'latitude' in df.columns and 'longitude' in df.columns:
        geo_data = create_geo_json(df)
        with open('data/json/haunted_places_geo.json', 'w') as f:
            json.dump(geo_data, f)
        # 3. State counts for choropleth or bar chart
    if 'state' in df.columns:
        state_counts = df['state'].value_counts().reset_index()
        state_counts.columns = ['state', 'count']
        state_counts.to_json('data/json/state_counts.json', orient='records')

        # 4. City counts for word cloud
    if 'city' in df.columns:
        city_counts = df['city'].value_counts().head(100).reset_index()
        city_counts.columns = ['city', 'count']
        city_counts.to_json('data/json/city_counts.json', orient='records')

        # 5. Location type distribution for pie chart
    if 'location_type' in df.columns:
        location_counts = df['location_type'].value_counts().reset_index()
        location_counts.columns = ['location_type', 'count']
        location_counts.to_json('data/json/location_type_counts.json', orient='records')

        # 6. Evidence type distribution for bar chart
        if 'Audio Evidence' in df.columns and 'Image/Video/Visual Evidence' in df.columns:
            # Create a summary of evidence types
            evidence_summary = {
                'Audio Only': ((df['Audio Evidence'] == 'TRUE') & (df['Image/Video/Visual Evidence'] == 'FALSE')).sum(),
                'Visual Only': (
                            (df['Audio Evidence'] == 'FALSE') & (df['Image/Video/Visual Evidence'] == 'TRUE')).sum(),
                'Both Audio and Visual': (
                            (df['Audio Evidence'] == 'TRUE') & (df['Image/Video/Visual Evidence'] == 'TRUE')).sum(),
                'No Evidence': (
                            (df['Audio Evidence'] == 'FALSE') & (df['Image/Video/Visual Evidence'] == 'FALSE')).sum()
            }

            evidence_df = pd.DataFrame([
                {'evidence_type': k, 'count': v} for k, v in evidence_summary.items()
            ])
            evidence_df.to_json('data/json/evidence_counts.json', orient='records')

        # 7. Event types counts if available
        if 'Event Type' in df.columns:
            event_counts = df['Event Type'].value_counts().reset_index()
            event_counts.columns = ['event_type', 'count']
            event_counts.to_json('data/json/event_type_counts.json', orient='records')

            # 8. Time-based data (Time of Day)
            if 'Time of Day' in df.columns:
                time_counts = df['Time of Day'].value_counts().reset_index()
                time_counts.columns = ['time_of_day', 'count']
                time_counts.to_json('data/json/time_of_day_counts.json', orient='records')

    def create_geo_json(df):
            """
            Create a GeoJSON object from the dataset for map visualizations.

            Args:
                df (pandas.DataFrame): The haunted places dataset with coordinates

            Returns:
                dict: A GeoJSON object
            """
            # Filter out entries without valid coordinates
            geo_df = df.dropna(subset=['latitude', 'longitude']).copy()

            # Create GeoJSON structure

    geo_json = {
        "type": "FeatureCollection",
        "features": []
    }

    for _, row in geo_df.iterrows():
        # Create feature properties based on available columns
        properties = {col: row[col] for col in row.index if col not in ['latitude', 'longitude'] and pd.notna(row[col])}

        # Ensure key fields have default values if missing
        if 'city' not in properties:
            properties['city'] = 'Unknown'
        if 'state' not in properties:
            properties['state'] = 'Unknown'
        if 'location' not in properties:
            properties['location'] = 'Unknown Location'
            # Create the GeoJSON feature
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [float(row['longitude']), float(row['latitude'])]
                },
                "properties": properties
            }

            geo_json["features"].append(feature)

        return geo_json

    if __name__ == "__main__":
        main()