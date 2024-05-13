from flask import Flask, render_template, jsonify
import requests
import plotly.graph_objs as go

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/data')
def get_data():
    # Fetch data from the API
    api_url = "https://api.covidactnow.org/v2/states.json?apiKey=254b42b4fac144718664aca60b349b51"
    response = requests.get(api_url)
    
    # Parse JSON response
    if response.status_code == 200:
        data = response.json()
    else:
        return jsonify({"error": "Failed to fetch data from the API"}), 500

    # Process data and create graphs using Plotly
    states = [state['state'] for state in data]
    cases = [state['actuals']['cases'] for state in data]
    deaths = [state['actuals']['deaths'] for state in data]

    # Create a bar chart for cases
    cases_chart = go.Bar(x=states, y=cases, name='Cases')

    # Create a bar chart for deaths
    deaths_chart = go.Bar(x=states, y=deaths, name='Deaths')

    # Create a figure with both charts
    fig = go.Figure(data=[cases_chart, deaths_chart])

    # Convert the figure to JSON and return
    graph_json = fig.to_json()

    return graph_json

if __name__ == '__main__':
    app.run(debug=True)

