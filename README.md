# dsci550-assignment3




# 3_ApacheSolr-ElasticSearch

## Overview
This folder contains the files related to the ingestion and querying of Haunted Places data using **Apache Solr** for DSCI 550 Assignment 3.

We created a Solr core named `assignment3`, uploaded the processed JSON dataset into it, and exported the core as a `.tgz` archive for submission.  
Additionally, we built a simple D3.js web page to live-fetch and display Haunted Places records from the Solr server.

---

## Files
- `assignment3.tgz`  
  A compressed archive of the Solr `assignment3` core, containing indexed Haunted Places data.

- `convert_tsv_to_json_array.ipynb`  
  Python notebook script used to convert the original TSV file into a Solr-ingestable **JSON array**.

- `final_haunted_places_array.json`  
  The processed JSON array file containing Haunted Places records, ready for Solr ingestion.

- `test_solr_d3.html`  
  A sample HTML page that uses D3.js to fetch and display Haunted Places data directly from the Solr core.

- `d3.js`  
  A copy of D3.js v5 (optional; can alternatively link to CDN).

---

## Instructions

### To Restore the Solr Core:

1. Launch a Solr Docker container (or a local Solr server).
2. Copy `assignment3.tgz` into the container or Solr server.
3. Extract the `.tgz` archive inside the Solr `data/` directory.
4. Restart Solr if needed. The core will be available under the name `assignment3`.

Example Docker commands:
```bash
docker cp 3_ApacheSolr-ElasticSearch/assignment3.tgz solr-container:/var/solr/data/
docker exec -it solr-container bash
cd /var/solr/data/
tar -xzf assignment3.tgz
exit
docker restart solr-container

