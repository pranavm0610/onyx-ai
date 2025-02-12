import geemap
import ee


# Authenticate Earth Engine
ee.Authenticate()
# Initialize Earth Engine
ee.Initialize()

# Create a map
Map = geemap.Map(center=(20.5937, 78.9629), zoom=5)  # Centered on India

# Define coordinates of the polygon (India's general area for example)
coords = [
    [77.0, 26.0],  # Point 1
    [85.0, 26.0],  # Point 2
    [85.0, 30.0],  # Point 3
    [77.0, 30.0],  # Point 4
    [77.0, 26.0]   # Closing the polygon
]

# Create the polygon
polygon = ee.Geometry.Polygon(coords)

# Create a red color style for the polygon
polygon_style = {
    'color': 'FF0000',  # Red color (hex code)
    'fillColor': 'FF0000',  # Solid red fill
    'width': 2  # Border width
}

# Add polygon to the map with the style
Map.addLayer(polygon, polygon_style, "India Polygon")

# Display the map
Map.show()
