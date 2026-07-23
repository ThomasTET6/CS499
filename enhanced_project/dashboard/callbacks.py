"""
Dash callback functions.

This module handles interactions between dashboard components,
including table filtering, chart updates, and map updates.

Enhancements completed:
- Replaced repeated filtering logic with a reusable query builder.
- Improved separation between dashboard behavior and query definitions.

Future enhancements:
- Improve database integration and CRUD functionality.
- Add additional validation and error handling for user inputs.
"""

import pandas as pd
import plotly.express as px

import dash_leaflet as dl

from dash import html
from dash.dependencies import Input, Output

from dashboard.database import load_animals
from dashboard.queries import build_query


def register_callbacks(app):

    @app.callback(
    Output("datatable-id", "data"),
    Output("datatable-id", "selected_rows"),
    Input("filter-type", "value")
    )
    def update_dashboard(filter_type):
        """
        Update the dashboard table based on the selected rescue type.

        Uses the query builder from queries.py to dynamically generate
        MongoDB queries instead of relying on repeated conditional logic.
        """

        query = build_query(filter_type)

        # FIXME (Milestone 4):
        # Replace temporary database retrieval with improved database
        # connection handling and enhanced CRUD functionality.

        dff = pd.DataFrame.from_records(db.read(query))

        # Remove MongoDB ObjectID field if present
        dff.drop(columns=["_id"], inplace=True, errors="ignore")

        # Reset table selection after filtering
        return dff.to_dict("records"), [0]


    @app.callback(
        Output('graph-id', 'children'),
        Input('datatable-id', 'derived_virtual_data')
    )
    def update_graphs(viewData):
        """
        Generate a pie chart displaying breed distribution.
        """

        if viewData is None:
            return []

        # Convert dashboard records into a pandas DataFrame for processing.
        dff = pd.DataFrame.from_dict(viewData)

        if dff.empty or 'breed' not in dff.columns:
            return []

        # Count occurrences of each breed.
        breed_counts = dff['breed'].value_counts()

        # Group smaller categories into Other
        if len(breed_counts) > 13:
            top13 = breed_counts.nlargest(13)
            other_count = breed_counts.iloc[13:].sum()
            top13["Other"] = other_count
            final_counts = top13

        else:
            final_counts = breed_counts


        fig = px.pie(
            names=final_counts.index,
            values=final_counts.values,
            title='Breed Distribution'
        )

        return [
            html.Div(
                children=[
                    html.H3("Breed Distribution"),
                    html.Br(),
                    # Dash graph component
                ]
            )
        ]


    @app.callback(
        Output('datatable-id', 'style_data_conditional'),
        Input('datatable-id', 'selected_columns')
    )
    def update_styles(selected_columns):
        """
        Highlight selected columns.
        """

        if selected_columns is None:
            return []

        return [
            {
                'if': {'column_id': column},
                'background_color': '#D2F3FF'
            }
            for column in selected_columns
        ]


    @app.callback(
        Output('map-id', 'children'),
        Input('datatable-id', 'derived_virtual_data'),
        Input('datatable-id', 'derived_virtual_selected_rows')
    )
    def update_map(viewData, index):
        """
        Display map location for selected animal.
        """

        if viewData is None:
            return []

        dff = pd.DataFrame.from_dict(viewData)

        if dff.empty:
            return []

        if index is None or len(index) == 0:
            row = 0

        else:
            row = index[0]


        return [

            dl.Map(
                style={
                    'width': '1000px',
                    'height': '500px'
                },

                center=[
                    30.75,
                    -97.48
                ],

                zoom=10,

                children=[

                    dl.TileLayer(
                        id="base-layer-id"
                    ),

                    dl.Marker(

                        position=[
                            dff.iloc[row, 13],
                            dff.iloc[row, 14]
                        ],

                        children=[

                            dl.Tooltip(
                                dff.iloc[row, 4]
                            ),

                            dl.Popup(
                                [
                                    html.H1("Animal Name"),
                                    html.P(
                                        dff.iloc[row, 9]
                                    )
                                ]
                            )
                        ]
                    )
                ]
            )
        ]