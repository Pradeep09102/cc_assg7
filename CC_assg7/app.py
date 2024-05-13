from flask import Flask, render_template
import requests

app = Flask(__name__)

# Fetch data from API
@app.route('/')
def index():
    api_key = '254b42b4fac144718664aca60b349b51'
    url = "https://api.covidactnow.org/v2/states.json?apiKey={api_key}"
    response = requests.get(url)
    data = response.json()

    # Process data (example: extract cases for each state)
    state_data = {}
    for state in data:
        state_data[state['state']] = {
            'cases': state['actuals']['cases'],
            'deaths': state['actuals']['deaths']
        }

    # Render template with data
    return render_template('dashboard.html', state_data=state_data)

if __name__ == '__main__':
    app.run(debug=True)
    
