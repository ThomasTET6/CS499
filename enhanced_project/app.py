"""
Main application entry point.
"""

from dash import Dash

from dashboard.layout import create_layout
from dashboard.callbacks import register_callbacks

app = Dash(__name__)

app.title = "Grazioso Salvare Animal Dashboard"

app.layout = create_layout()

register_callbacks(app)


if __name__ == "__main__": app.run(debug=True)