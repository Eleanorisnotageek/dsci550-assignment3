Here is a README.md tailored for your GitHub repository based on the assignment description in the PDF and modeled after the style you provided:

⸻

DSCI550 Large Scale Web Data Visualization: Haunted Places

Repository for DSCI 550 Group 02
Collaborators: Eleanor Bi, Maggie Chang, Jessica Deng, Tarun Jagadish, Aaron Kuo, Hengxiao Zhu

⸻

Project Overview

This project builds upon our earlier assignments involving haunted places by creating a webpage that visualizes multimodal data using the D3.js framework. The goal is to explore and present data insights from haunted place sightings, images, and geolocation information via intuitive visual representations. The project also integrates open-source tools such as MEMEX Image Space and MEMEX GeoParser to enrich the interactive user experience.

⸻

Key Achievements
	•	D3 Visualizations: Designed and deployed 5 unique visualizations based on assignment 1 and 2 insights
	•	Location Analytics: Integrated MEMEX GeoParser to extract and map location mentions from haunted place descriptions
	•	Image Similarity Search: Deployed MEMEX Image Space for interactive exploration of AI-generated haunted location images
	•	Data Aggregation Pipeline: Transformed TSV data to JSON for use in D3, Apache Solr, and Elasticsearch
	•	Web Deployment: Hosted the final website for user interaction via a centralized landing page

⸻

Division of Work
	•	Sidney and Eleanor
Handled TSV-to-JSON conversion and developed all five D3 visualizations to highlight insights from Assignments 1 and 2.
	•	Aaron and Maggie
Installed and configured ImageSpace, Solr, and ImageCat, and attempted integration of SMQTK for visual similarity search.
	•	Jessica and Tarun
Processed unstructured text using GeoTopicParser and SpaCy to extract geographic references. They also led the overall project integration and compiled the final report.

All team members actively contributed to data preparation, debugging, and the final report writing process.

⸻

Technologies Used

Web & Data Visualization
	•	D3.js: Data-driven visualizations
	•	HTML/CSS/JavaScript: Frontend structure
	•	Python: Data preprocessing scripts
	•	Apache Solr / Elasticsearch: Search indexing and querying

Image & Text Analysis
	•	MEMEX Image Space: Image indexing and similarity search
	•	MEMEX GeoParser: Location extraction and mapping
	•	Apache Tika: Text and image metadata extraction
	•	Tika-Python: Used for ingestion scripts

⸻

Visualizations Implemented
	1.	State-Level Bar Chart – Distribution of haunted sightings by U.S. state
	2.	City-Level Bar Chart – City-wise breakdown of haunting entries
	3.	Pie Chart of Event Types – Summarized haunting themes from descriptions
	4.	Donut Chart for Time Analysis – Temporal patterns of sightings
	5.	Treemap – Nested regional breakdown of haunting density

⸻

Getting Started

Prerequisites
	•	Python 3.8+
	•	Node.js (for running local web server if needed)
	•	Docker (for GeoParser and ImageSpace setup)
	•	Apache Solr or Elasticsearch (Docker preferred)

Setup Instructions

# Clone the repository
git clone https://github.com/Eleanorisnotageek/dsci550-assignment3.git

# Install required Python packages
pip install -r requirements.txt

# Start local web server for D3 visualizations (optional)
python3 -m http.server 8000

# Set up GeoParser
# Follow: https://github.com/nasa-jpl-memex/GeoParser

# Set up Image Space
# Follow: https://github.com/nasa-jpl-memex/image_space/wiki/Quick-Start-Guide-with-ImageCat



⸻

Insights and Analysis

Geographic Patterns
	•	Notable clusters of haunted place sightings were seen in cities like Los Angeles, San Antonio, and Columbus.
	•	MEMEX GeoParser revealed unexpected non-U.S. locations in generated data, not present in the original dataset.

Image Similarity
	•	Image Space helped identify visually similar haunted scenes that weren’t obviously related via text.
	•	Visual clusters revealed recurring themes (e.g., abandoned houses, shadowy forests).

Tool Observations
	•	ImageCat/Image Space: Easy setup via Docker; ingestion with Tika required minor preprocessing
	•	GeoParser: Setup was more involved, but visual output provided strong spatial insights

⸻

Conclusion

Our interactive site effectively demonstrates how D3, NLP, and AI-generated images can provide new insight into multimodal haunted place data. Through visual storytelling and advanced search tools, we revealed previously hidden connections and patterns across haunted locations.

⸻
