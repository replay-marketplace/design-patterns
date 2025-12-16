import flask
import pandas as pd
import plotly.express as px

app = flask.Flask(__name__)

@app.route('/')
def index():
    # Connect to data sources and create charts here
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)