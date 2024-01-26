from flask import Flask, render_template,  jsonify, send_from_directory
import pandas as pd
app = Flask(__name__)

# Load the FHIR data
fhir_data = pd.read_json('static/fhir_bundle.json')

# Convert the FHIR bundle into a more usable format
# This transformation depends on the structure of your FHIR data
def transform_fhir_data(fhir_data):
    transformed_data = []
    for entry in fhir_data['entry']:
        resource = entry['resource']
        country = resource['subject']['reference'].split('/')[-1]
        date = resource['effectiveDateTime']
        cases = resource['valueQuantity']['value']
        deaths = resource['component'][0]['valueQuantity']['value']
        transformed_data.append({
            'country': country,
            'date': date,
            'cases': cases,
            'deaths': deaths
        })
    return transformed_data

usable_data = transform_fhir_data(fhir_data)

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(usable_data)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
