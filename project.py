import pandas as pd
import geopandas as gpd
import folium
from folium.plugins import MarkerCluster, HeatMap
import ipywidgets as widgets
from ipywidgets import interactive

# Load COVID-19 dataset
covid_url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
covid_data = pd.read_csv(covid_url, parse_dates=['date'])

# Keep only Three West Europe countries.
west_europe_countries = ['France', 'Belgium', 'Germany']

# Select relevant columns for the analysis
selected_columns = ['location', 'total_cases', 'total_deaths', 'people_fully_vaccinated_per_hundred', 'population']
west_europe_data = covid_data[covid_data['location'].isin(west_europe_countries)][selected_columns]

# Keep only the last row for each country to get a 'total' result
west_europe_data = west_europe_data.groupby('location').last().reset_index()

# Load GeoJSON file
geojson_url = "fgb-countries.geojson"
world = gpd.read_file(geojson_url)

# Merge COVID-19 data with GeoJSON data using ISO_A3 codes
merged_data = world.merge(west_europe_data, left_on='ADMIN', right_on='location', how='left')


# Calculate the centroid of Germany
germany_centroid = merged_data.loc[merged_data['location'] == 'Germany', 'geometry'].centroid
map_center = [germany_centroid.y.values[0], germany_centroid.x.values[0]]

# Create Folium map centered on Germany
m = folium.Map(location=map_center, zoom_start=5)

# Create MarkerClusters for better performance
marker_cluster = MarkerCluster().add_to(m)

# Add GeoJSON layer with COVID data and tooltips
folium.GeoJson(
    merged_data,
    name='Covid Data',
    tooltip=folium.GeoJsonTooltip(
        fields=['location', 'total_cases'],
        aliases=['Region', 'Covid Cases'],
        localize=True
    ),
).add_to(marker_cluster)

# Function to update GeoJSON layer based on the filter
def update_map(cases_threshold):
    filtered_data = merged_data[merged_data['total_cases'] >= cases_threshold]

    # Remove previous Choropleth layer
    for layer in m._children.values():
        if isinstance(layer, folium.Choropleth):
            m.remove_layer(layer)

    # Add a new Choropleth layer with the filtered data
    folium.Choropleth(
        geo_data=filtered_data,
        name='Filtered Covid Data',
        data=filtered_data,
        columns=['location', 'total_deaths'],
        key_on='feature.properties.location',
        fill_color='YlOrRd',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Deaths',
        highlight=True,
    ).add_to(m)

# Create an interactive slider for filtering COVID cases
cases_slider = widgets.FloatSlider(value=0, min=0, max=500000, step=10000, description='Min COVID Cases:')
widget = interactive(update_map, cases_threshold=cases_slider)
widget.children[-1].layout.height = 'auto'  # Adjusting the height for better visibility
display(widget)


# Read HTML content from files
with open('legend.html', "r") as legend_file:
    legend_html = legend_file.read()

with open('popup.html', "r") as popup_file:
    popup_html_template = popup_file.read()


for idx, row in merged_data.iterrows():
    # Choose marker color based on Covid Cases
    marker_color = 'green' if row['total_cases'] < 5000000 else ('blue' if 5000001 <= row['total_cases'] < 25000000 else 'red')

    # Populate the popup template with data
    popup_html = popup_html_template.format(
        location=row['location'],
        population=row['population'],
        vaccination_rate=row['people_fully_vaccinated_per_hundred'],
        total_cases=row['total_cases'],
        total_deaths=row['total_deaths']
    )

    # Use the better formatted popup
    folium.Marker(
        location=[row.geometry.centroid.y, row.geometry.centroid.x],
        popup=folium.Popup(popup_html, max_width=300),
        icon=folium.Icon(color=marker_color),
    ).add_to(marker_cluster)



m.get_root().html.add_child(folium.Element(legend_html))

# Create a HeatMap layer using the location coordinates and intensity (e.g., COVID cases)
heat_data = [[point.xy[1][0], point.xy[0][0]] for idx, row in merged_data.iterrows() for point in [row.geometry.centroid]]
print(heat_data)
HeatMap(heat_data, name='Heatmap', radius=25, blur=20, gradient={0.4: '#FFD700', 0.65: '#FF4500', 1: '#8B0000'}).add_to(m)

# Add Layer Control to toggle layers
folium.LayerControl().add_to(m)

# Save the map as an HTML file
m.save('fgb-countries-covid-map.html')

