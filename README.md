
# COVID-19 Dashboard

## Overview
The COVID-19 Dashboard is a powerful data filtering tool designed to visualize COVID-19 deaths for various European countries. Its primary goal is to provide insights into the impact of the pandemic on different regions and countries. Users, including data analysts, healthcare professionals, and policymakers, can interact with the dashboard to view the data and explore specific regions in detail.

## Key Features
- **Interactive Map**: Displays a bar chart of European countries versus COVID deaths upon opening the dashboard.
- **Search Functionality**: Allows users to search for specific regions or countries and view detailed visualizations.
- **Data Visualization**: Provides clear visualizations that include the number of COVID-19 cases and deaths.
- **Dockerization**: Ensures easy deployment and environment consistency.
- **GitHub Codespaces Compatibility**: Supports development and deployment directly via GitHub.
- **RESTful API Integration**: Supports both POST and GET methods for efficient data handling.
- **FHIR Data Format**: Utilizes FHIR bundle format for medical data representation.

## Data Source
The COVID-19 data for this dashboard is generated from a medical JSON dataset, specifically in FHIR bundle format. Here's a sample structure of the data:

```json
{
  "resourceType": "Bundle",
  "type": "collection",
  "entry": [
    {
      "resource": {
        "resourceType": "Observation",
        "id": "observation-2463",
        "status": "final",
        "code": {
          "coding": [
            {
              "system": "http://loinc.org",
              "code": "94531-1",
              "display": "COVID-19 cases"
            }
          ]
        },
        // More data...
      }
    },
    {
      // Additional entries...
    }
  ]
}
```

## Visualization
The dashboard provides an intuitive visualization of COVID-19 data, including:
- **Number of Cases**: The visualization includes the number of COVID-19 cases for each region or country.
- **Number of Deaths**: Users can easily view the number of COVID-19 deaths for specific regions.

## Key User Groups
The COVID-19 Dashboard caters to the following key user groups:
- **Data Analysts**: Utilize the dashboard for in-depth analysis of COVID-19 data and trends.
- **Healthcare Professionals**: Gain insights into the impact of the pandemic in different regions to support clinical decisions.
- **Policymakers**: Use the data to inform decisions on healthcare policies and strategies.
- **Researchers**: Researchers in epidemiology and public health can access valuable data for their studies.

## User Objectives
Users of the dashboard have specific objectives, including:
- **Understanding Regional Impact**: Users can view COVID-19 data for different European countries to understand the regional impact of the pandemic.
- **Comparing Statistics**: Easily compare the number of cases and deaths across regions.
- **Informed Decision-Making**: Policymakers and healthcare professionals can make informed decisions based on the data.
- **Research and Analysis**: Researchers can analyze the data for epidemiological studies and research.

## Installation and Setup
Ensure Docker is installed on your system before proceeding.

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Eriolasaliu/West-Europe-COVID-19-Analysis
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd West-Europe-COVID-19-Analysis
   ```

3. **Build the Docker Image**:
   ```bash
   docker build -t covid19-dashboard .
   ```

4. **Run the Docker Container**:
   ```bash
   docker run -p 5000:5000 covid19-dashboard
   ```

## Usage
1. **Accessing the Dashboard**: Open your web browser and go to `http://localhost:5000`.
2. **Filter by Country**: Use the dropdown menu to select a specific country or choose "All" to see the overall visualization.
3. **Interact with Visualizations**: Explore the map and view the number of COVID-19 cases and deaths for the selected region.

## Data Structure
The FHIR bundle JSON data is transformed into a more usable format for visualization. It includes information such as the country, date, COVID-19 cases, and deaths.

## Contributing
Interested in contributing? Here's how you can help:

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add some YourFeature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.

## License
This project is released under the [MIT License](LICENSE).

## Contact
- **Name**: [eriola.salihu@stud.th-deg.de](mailto:eriola.salihu@stud.th-deg.de)
- **Project Link**: [https://github.com/Eriolasaliu/West-Europe-COVID-19-Analysis](https://github.com/Eriolasaliu/West-Europe-COVID-19-Analysis)
