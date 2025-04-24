# generate D3 visualizations:
import os
from pathlib import Path


def create_visualizations():
    """
    Create HTML files for D3 visualizations of the haunted places data.
    """
    # Create directory for visualizations if it doesn't exist
    os.makedirs('visualizations', exist_ok=True)

    # Create the main dashboard HTML file
    create_dashboard()

    # Create individual visualization HTML files
    create_choropleth_map()
    create_geo_map()
    create_bar_chart()
    create_pie_chart()
    create_word_cloud()

    print("D3 visualization HTML files have been created in the 'visualizations' directory.")


def create_dashboard():
    """
    Create the main dashboard HTML file that links to all visualizations.
    """
    dashboard_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Haunted Places Data Visualization Dashboard</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/css/bootstrap.min.css">
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            padding: 20px;
            background-color: #f8f9fa;
        }
        .dashboard-header {
            text-align: center;
            margin-bottom: 30px;
            color: #343a40;
        }
        .visualization-card {
            margin-bottom: 30px;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }
        .visualization-card:hover {
            transform: translateY(-5px);
        }
        .card-header {
            background-color: #343a40;
            color: white;
            padding: 15px;
            font-weight: bold;
        }
        iframe {
            width: 100%;
            height: 500px;
            border: none;
        }
        .nav-tabs {
            border-bottom: 2px solid #343a40;
            margin-bottom: 20px;
        }
        .nav-link {
            color: #343a40;
            font-weight: bold;
        }
        .nav-link.active {
            background-color: #343a40;
            color: white;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="dashboard-header">
            <h1>Haunted Places Data Visualization Dashboard</h1>
            <p class="lead">Exploring the geography and characteristics of haunted locations</p>
        </div>

        <ul class="nav nav-tabs" id="visualizationTabs" role="tablist">
            <li class="nav-item" role="presentation">
                <button class="nav-link active" id="maps-tab" data-bs-toggle="tab" data-bs-target="#maps" type="button" role="tab" aria-controls="maps" aria-selected="true">Maps</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="charts-tab" data-bs-toggle="tab" data-bs-target="#charts" type="button" role="tab" aria-controls="charts" aria-selected="false">Charts</button>
            </li>
        </ul>

        <div class="tab-content" id="visualizationTabContent">
            <div class="tab-pane fade show active" id="maps" role="tabpanel" aria-labelledby="maps-tab">
                <div class="row">
                    <div class="col-lg-12">
                        <div class="visualization-card">
                            <div class="card-header">U.S. States Haunted Places Choropleth Map</div>
                            <iframe src="choropleth_map.html"></iframe>
                        </div>
                    </div>
                    <div class="col-lg-12">
                        <div class="visualization-card">
                            <div class="card-header">Interactive Map of Haunted Locations</div>
                            <iframe src="geo_map.html"></iframe>
                        </div>
                    </div>
                </div>
            </div>

            <div class="tab-pane fade" id="charts" role="tabpanel" aria-labelledby="charts-tab">
                <div class="row">
                    <div class="col-lg-6">
                        <div class="visualization-card">
                            <div class="card-header">Top Haunted States</div>
                            <iframe src="bar_chart.html"></iframe>
                        </div>
                    </div>
                    <div class="col-lg-6">
                        <div class="visualization-card">
                            <div class="card-header">Haunted Places by Location Type</div>
                            <iframe src="pie_chart.html"></iframe>
                        </div>
                    </div>
                    <div class="col-lg-12">
                        <div class="visualization-card">
                            <div class="card-header">Most Haunted Cities Word Cloud</div>
                            <iframe src="word_cloud.html"></iframe>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <footer class="text-center mt-4">
            <p>DSCI550 Assignment 3 - Haunted Places Data Visualization</p>
        </footer>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

    with open('visualizations/dashboard.html', 'w') as f:
        f.write(dashboard_html)


def create_choropleth_map():
    """
    Create HTML file for US States choropleth map visualization.
    """
    choropleth_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Haunted Places by State</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <script src="https://d3js.org/topojson.v3.min.js"></script>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f8f9fa;
        }
        h1 {
            text-align: center;
            color: #343a40;
        }
        #map-container {
            display: flex;
            justify-content: center;
        }
        .state {
            fill: #ddd;
            cursor: pointer;
            stroke: #fff;
            stroke-width: 0.5px;
        }
        .state:hover {
            stroke-width: 2px;
        }
        .tooltip {
            position: absolute;
            background-color: #fff;
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 10px;
            pointer-events: none;
            font-size: 14px;
            opacity: 0;
            transition: opacity 0.3s;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .legend {
            background-color: #fff;
            border-radius: 4px;
            padding: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .legend-title {
            font-weight: bold;
            margin-bottom: 5px;
        }
    </style>
</head>
<body>
    <h1>Haunted Places by State</h1>
    <div id="map-container"></div>

    <script>
        // Set dimensions
        const width = 960;
        const height = 600;
        const margin = {top: 20, right: 20, bottom: 20, left: 20};

        // Create SVG container
        const svg = d3.select("#map-container")
            .append("svg")
            .attr("width", width)
            .attr("height", height)
            .attr("viewBox", [0, 0, width, height])
            .attr("style", "max-width: 100%; height: auto;");

        // Create tooltip
        const tooltip = d3.select("body")
            .append("div")
            .attr("class", "tooltip");

        // Load data
        Promise.all([
            d3.json("https://cdn.jsdelivr.net/npm/us-atlas@3/states-10m.json"),
            d3.json("../data/json/state_counts.json")
        ]).then(([us, stateCounts]) => {
            // Create a map of state names to counts
            const countByState = {};
            stateCounts.forEach(d => {
                countByState[d.state] = +d.count;
            });

            // Get the maximum count for color scale
            const maxCount = d3.max(stateCounts, d => d.count);

            // Define color scale
            const colorScale = d3.scaleSequential()
                .domain([0, maxCount])
                .interpolator(d3.interpolateBlues);

            // Draw states
            svg.append("g")
                .selectAll("path")
                .data(topojson.feature(us, us.objects.states).features)
                .enter()
                .append("path")
                .attr("class", "state")
                .attr("d", d3.geoPath())
                .attr("fill", d => {
                    // Get state name from the id
                    const stateName = d.properties.name;
                    return countByState[stateName] ? colorScale(countByState[stateName]) : "#eee";
                })
                .on("mouseover", function(event, d) {
                    // Show tooltip on hover
                    const stateName = d.properties.name;
                    const count = countByState[stateName] || 0;

                    tooltip.style("opacity", 1)
                        .html(`<strong>${stateName}</strong><br>${count} haunted places`)
                        .style("left", (event.pageX + 10) + "px")
                        .style("top", (event.pageY - 28) + "px");
                })
                .on("mouseout", function() {
                    // Hide tooltip
                    tooltip.style("opacity", 0);
                });

            // Add state boundaries
            svg.append("path")
                .datum(topojson.mesh(us, us.objects.states, (a, b) => a !== b))
                .attr("fill", "none")
                .attr("stroke", "white")
                .attr("stroke-width", 0.5)
                .attr("d", d3.geoPath());

            // Add legend
            const legendGroup = svg.append("g")
                .attr("class", "legend")
                .attr("transform", `translate(${width - 150}, ${height - 180})`);

            legendGroup.append("rect")
                .attr("width", 140)
                .attr("height", 160)
                .attr("fill", "white")
                .attr("stroke", "#ddd");

            legendGroup.append("text")
                .attr("class", "legend-title")
                .attr("x", 10)
                .attr("y", 20)
                .text("Haunted Places");

            // Create legend scale
            const legendScale = d3.scaleSequential()
                .domain([0, maxCount])
                .interpolator(d3.interpolateBlues);

            // Create legend items
            const legendItems = 5;
            const legendHeight = 100;
            const itemHeight = legendHeight / legendItems;

            for (let i = 0; i < legendItems; i++) {
                const value = maxCount * (1 - i / (legendItems - 1));
                const y = 40 + i * itemHeight;

                legendGroup.append("rect")
                    .attr("x", 10)
                    .attr("y", y)
                    .attr("width", 20)
                    .attr("height", itemHeight)
                    .attr("fill", legendScale(value));

                legendGroup.append("text")
                    .attr("x", 40)
                    .attr("y", y + itemHeight / 2)
                    .attr("dy", "0.35em")
                    .attr("font-size", 10)
                    .text(Math.round(value));
            }
        }).catch(error => {
            console.error("Error loading data:", error);
        });
    </script>
</body>
</html>
"""

    with open('visualizations/choropleth_map.html', 'w') as f:
        f.write(choropleth_html)


def create_geo_map():
    """
    Create HTML file for interactive map of haunted locations.
    """
    geo_map_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Map of Haunted Locations</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f8f9fa;
        }
        h1 {
            text-align: center;
            color: #343a40;
        }
        #map {
            height: 600px;
            width: 100%;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .info-panel {
            padding: 10px;
            background-color: white;
            border-radius: 4px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            max-width: 300px;
        }
        .filter-container {
            margin-bottom: 20px;
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 10px;
        }
        .filter-btn {
            padding: 8px 16px;
            background-color: #343a40;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .filter-btn:hover {
            background-color: #23272b;
        }
        .filter-btn.active {
            background-color: #007bff;
        }
    </style>
</head>
<body>
    <h1>Interactive Map of Haunted Locations</h1>

    <div class="filter-container" id="filter-buttons">
        <!-- Filter buttons will be added here dynamically -->
    </div>

    <div id="map"></div>

    <script>
        // Initialize the map
        const map = L.map('map').setView([39.8283, -98.5795], 4); // Center on the US

        // Add tile layer (OpenStreetMap)
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        // Load GeoJSON data
        d3.json("../data/json/haunted_places_geo.json").then(data => {
            // Create a layer group for all markers
            const markersLayer = L.layerGroup().addTo(map);

            // Extract unique location types
            const locationTypes = new Set();
            data.features.forEach(feature => {
                if (feature.properties.location_type) {
                    locationTypes.add(feature.properties.location_type);
                }
            });

            // Create filter buttons
            const filterContainer = document.getElementById('filter-buttons');

            // Add 'All' button
            const allButton = document.createElement('button');
            allButton.textContent = 'All';
            allButton.className = 'filter-btn active';
            allButton.onclick = () => filterMarkers('all');
            filterContainer.appendChild(allButton);

            // Add buttons for each location type
            locationTypes.forEach(type => {
                const button = document.createElement('button');
                button.textContent = type.charAt(0).toUpperCase() + type.slice(1);
                button.className = 'filter-btn';
                button.onclick = () => filterMarkers(type);
                filterContainer.appendChild(button);
            });

            // Define marker icons for different location types
            const icons = {
                house: 'https://cdn.jsdelivr.net/npm/leaflet@1.7.1/dist/images/marker-icon.png',
                hospital: 'https://cdn.jsdelivr.net/npm/leaflet@1.7.1/dist/images/marker-icon.png',
                cemetery: 'https://cdn.jsdelivr.net/npm/leaflet@1.7.1/dist/images/marker-icon.png',
                hotel: 'https://cdn.jsdelivr.net/npm/leaflet@1.7.1/dist/images/marker-icon.png',
                school: 'https://cdn.jsdelivr.net/npm/leaflet@1.7.1/dist/images/marker-icon.png',
                default: 'https://cdn.jsdelivr.net/npm/leaflet@1.7.1/dist/images/marker-icon.png'
            };

            // Create markers for each location
            data.features.forEach(feature => {
                const coords = feature.geometry.coordinates;
                const properties = feature.properties;

                // Create marker
                const marker = L.marker([coords[1], coords[0]], {
                    title: properties.location || 'Unknown Location',
                    alt: properties.location_type || 'unknown'
                });

                // Create popup content
                let popupContent = `
                    <div class="info-panel">
                        <h3>${properties.location || 'Unknown Location'}</h3>
                        <p><strong>Location:</strong> ${properties.city || 'Unknown'}, ${properties.state || 'Unknown'}</p>
                `;

                if (properties.description) {
                    popupContent += `<p><strong>Description:</strong> ${properties.description}</p>`;
                }

                if (properties.location_type) {
                    popupContent += `<p><strong>Type:</strong> ${properties.location_type}</p>`;
                }

                if (properties['Event Type']) {
                    popupContent += `<p><strong>Event Type:</strong> ${properties['Event Type']}</p>`;
                }

                if (properties['Time of Day']) {
                    popupContent += `<p><strong>Time of Day:</strong> ${properties['Time of Day']}</p>`;
                }

                popupContent += `</div>`;

                // Bind popup to marker
                marker.bindPopup(popupContent);

                // Add marker to layer
                marker.addTo(markersLayer);
            });

            // Function to filter markers
            function filterMarkers(type) {
                // Update button styles
                document.querySelectorAll('.filter-btn').forEach(btn => {
                    btn.classList.remove('active');
                });
                event.target.classList.add('active');

                // Clear existing markers
                markersLayer.clearLayers();

                // Add filtered markers
                data.features.forEach(feature => {
                    const coords = feature.geometry.coordinates;
                    const properties = feature.properties;

                    if (type === 'all' || properties.location_type === type) {
                        // Create marker
                        const marker = L.marker([coords[1], coords[0]], {
                            title: properties.location || 'Unknown Location',
                            alt: properties.location_type || 'unknown'
                        });

                        // Create popup content (same as above)
                        let popupContent = `
                            <div class="info-panel">
                                <h3>${properties.location || 'Unknown Location'}</h3>
                                <p><strong>Location:</strong> ${properties.city || 'Unknown'}, ${properties.state || 'Unknown'}</p>
                        `;

                        if (properties.description) {
                            popupContent += `<p><strong>Description:</strong> ${properties.description}</p>`;
                        }

                        if (properties.location_type) {
                            popupContent += `<p><strong>Type:</strong> ${properties.location_type}</p>`;
                        }

                        if (properties['Event Type']) {
                            popupContent += `<p><strong>Event Type:</strong> ${properties['Event Type']}</p>`;
                        }

                        if (properties['Time of Day']) {
                            popupContent += `<p><strong>Time of Day:</strong> ${properties['Time of Day']}</p>`;
                        }

                        popupContent += `</div>`;

                        // Bind popup to marker
                        marker.bindPopup(popupContent);

                        // Add marker to layer
                        marker.addTo(markersLayer);
                    }
                });
            }
        }).catch(error => {
            console.error("Error loading GeoJSON data:", error);
        });
    </script>
</body>
</html>
"""

    with open('visualizations/geo_map.html', 'w') as f:
        f.write(geo_map_html)


def create_bar_chart():
    """
    Create HTML file for bar chart visualization of top haunted states.
    """
    bar_chart_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Top Haunted States</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f8f9fa;
        }
        h1 {
            text-align: center;
            color: #343a40;
        }
        #chart-container {
            display: flex;
            justify-content: center;
        }
        .bar {
            fill: #