import pandas as pd
import json
import os
from pathlib import Path

OUTPUT_DIR = Path("/root/dsci 550 assignment 3/json_outputs")

def main():
    """
    Main function to process the haunted places dataset and convert it to JSON
    for D3 visualizations.
    """
    print("Loading data...")

    df = pd.read_csv('/root/dsci 550 assignment 3/final_haunted_places.tsv', sep='\t')

    print(f"Loaded {len(df)} haunted place records")
    print(f"Columns available: {', '.join(df.columns)}")

    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    
    df = clean_data(df)

 
    generate_json_files(df)

    print(f"Data processing complete. JSON files have been created in '{OUTPUT_DIR}'.")

def clean_data(df):
    """
    Clean and prepare the dataset for visualization.
    """
    if 'latitude' in df.columns and 'longitude' in df.columns:
        df_geo = df.dropna(subset=['latitude', 'longitude'])
        print(f"Rows with valid geo coordinates: {len(df_geo)} out of {len(df)}")

        df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
        df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')

    if 'location_type' not in df.columns and 'description' in df.columns:
        location_types = ['house', 'hospital', 'cemetery', 'hotel', 'school',
                          'church', 'bridge', 'road', 'forest', 'theater', 'prison']

        def extract_location_type(desc):
            if not isinstance(desc, str):
                return 'unknown'
            desc = desc.lower()
            for loc_type in location_types:
                if loc_type in desc:
                    return loc_type
            return 'other'

        df['location_type'] = df['description'].apply(extract_location_type)

    if 'city' in df.columns:
        df['city'] = df['city'].str.strip().str.title()

    if 'state' in df.columns:
        df['state'] = df['state'].str.strip().str.title()

    return df

def generate_json_files(df):
    """
    Generate JSON files for D3 visualizations.
    """
    (OUTPUT_DIR / 'haunted_places_full.json').write_text(df.to_json(orient='records'), encoding='utf-8')

    if 'latitude' in df.columns and 'longitude' in df.columns:
        geo_data = create_geo_json(df)
        with open(OUTPUT_DIR / 'haunted_places_geo.json', 'w', encoding='utf-8') as f:
            json.dump(geo_data, f, ensure_ascii=False, indent=2)

    if 'state' in df.columns:
        state_counts = df['state'].value_counts().reset_index()
        state_counts.columns = ['state', 'count']
        (OUTPUT_DIR / 'state_counts.json').write_text(state_counts.to_json(orient='records'), encoding='utf-8')

    if 'city' in df.columns:
        city_counts = df['city'].value_counts().head(100).reset_index()
        city_counts.columns = ['city', 'count']
        (OUTPUT_DIR / 'city_counts.json').write_text(city_counts.to_json(orient='records'), encoding='utf-8')

    if 'location_type' in df.columns:
        location_counts = df['location_type'].value_counts().reset_index()
        location_counts.columns = ['location_type', 'count']
        (OUTPUT_DIR / 'location_type_counts.json').write_text(location_counts.to_json(orient='records'), encoding='utf-8')

    if 'Audio Evidence' in df.columns and 'Image/Video/Visual Evidence' in df.columns:
        evidence_summary = {
            'Audio Only': ((df['Audio Evidence'] == 'TRUE') & (df['Image/Video/Visual Evidence'] == 'FALSE')).sum(),
            'Visual Only': ((df['Audio Evidence'] == 'FALSE') & (df['Image/Video/Visual Evidence'] == 'TRUE')).sum(),
            'Both Audio and Visual': ((df['Audio Evidence'] == 'TRUE') & (df['Image/Video/Visual Evidence'] == 'TRUE')).sum(),
            'No Evidence': ((df['Audio Evidence'] == 'FALSE') & (df['Image/Video/Visual Evidence'] == 'FALSE')).sum()
        }
        evidence_df = pd.DataFrame([
            {'evidence_type': k, 'count': v} for k, v in evidence_summary.items()
        ])
        (OUTPUT_DIR / 'evidence_counts.json').write_text(evidence_df.to_json(orient='records'), encoding='utf-8')

    if 'Event Type' in df.columns:
        event_counts = df['Event Type'].value_counts().reset_index()
        event_counts.columns = ['event_type', 'count']
        (OUTPUT_DIR / 'event_type_counts.json').write_text(event_counts.to_json(orient='records'), encoding='utf-8')

    if 'Time of Day' in df.columns:
        time_counts = df['Time of Day'].value_counts().reset_index()
        time_counts.columns = ['time_of_day', 'count']
        (OUTPUT_DIR / 'time_of_day_counts.json').write_text(time_counts.to_json(orient='records'), encoding='utf-8')

def create_geo_json(df):
    """
    Create a GeoJSON object from the dataset for map visualizations.
    """
    geo_df = df.dropna(subset=['latitude', 'longitude']).copy()

    geo_json = {
        "type": "FeatureCollection",
        "features": []
    }

    for _, row in geo_df.iterrows():
        properties = {col: row[col] for col in row.index if col not in ['latitude', 'longitude'] and pd.notna(row[col])}
        properties.setdefault('city', 'Unknown')
        properties.setdefault('state', 'Unknown')
        properties.setdefault('location', 'Unknown Location')

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
