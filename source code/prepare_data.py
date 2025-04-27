import pandas as pd
import json
import os
from collections import Counter


output_dir = '../data/json'
os.makedirs(output_dir, exist_ok=True)


df = pd.read_csv('/root/dsci 550 assignment 3/dsci550-assignment3/final_haunted_places.tsv', sep='\t')



full_data = df.to_dict(orient='records')
with open(os.path.join(output_dir, 'haunted_places_full.json'), 'w') as f:
    json.dump(full_data, f, indent=2)


city_counts = Counter(df['city'].dropna())
city_data = [{'city': city, 'count': count} for city, count in city_counts.most_common()]
with open(os.path.join(output_dir, 'city_counts.json'), 'w') as f:
    json.dump(city_data, f, indent=2)


state_counts = Counter(df['State'].dropna())
state_data = [{'state': state, 'count': count} for state, count in state_counts.most_common()]
with open(os.path.join(output_dir, 'state_counts.json'), 'w') as f:
    json.dump(state_data, f, indent=2)


event_counts = Counter(df['Event Type'].dropna())
event_data = [{'event': event, 'count': count} for event, count in event_counts.most_common()]
with open(os.path.join(output_dir, 'event_type_counts.json'), 'w') as f:
    json.dump(event_data, f, indent=2)


time_counts = Counter(df['Time of Day'].dropna())
time_data = [{'time': time, 'count': count} for time, count in time_counts.most_common()]
with open(os.path.join(output_dir, 'time_of_day_counts.json'), 'w') as f:
    json.dump(time_data, f, indent=2)

print('✅ All JSON files have been generated successfully!')