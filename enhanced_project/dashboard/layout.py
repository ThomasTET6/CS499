"""
Dashboard layout.

This module contains only the user interface components.

Future enhancements:
- Improve dashboard functionality with additional user interactions.
- Add enhanced filtering and data visualization features.
- Expand database-driven components to support additional operations.
"""

from dash import dcc, html, dash_table


def create_layout():

    return html.Div([

        ################################
        # Header Section
        ################################

        html.Center(
            html.B(
                html.H1(
                    'CS-340 Dashboard'
                )
            )
        ),


        ################################
        # Logo
        ################################

        html.Img(
            src="/assets/Grazioso Salvare Logo.png",
            style={
                'width': '200px',
                'display': 'block',
                'margin': 'auto'
            }
        ),


        html.Hr(),


        ################################
        # Filter Controls
        ################################

        html.Div([

            html.Label(
                "Rescue Type Filter"
            ),


            dcc.RadioItems(

                id='filter-type',

                options=[

                    {
                        'label': 'Water Rescue',
                        'value': 'WATER'
                    },

                    {
                        'label': 'Mountain/Wilderness Rescue',
                        'value': 'MOUNTAIN'
                    },

                    {
                        'label': 'Disaster/Individual Tracking',
                        'value': 'DISASTER'
                    },

                    {
                        'label': 'Reset',
                        'value': 'RESET'
                    }

                ],

                value='RESET',

                inline=True
            )

        ]),


        html.Hr(),


        ################################
        # Data Table
        ################################

        dash_table.DataTable(

            id='datatable-id',

            columns=[],

            data=[],


            row_selectable="single",

            selected_rows=[0],

            page_size=10,

            sort_action="native",

            filter_action="native",

            style_table={
                'overflowX': 'auto'
            }

        ),


        html.Br(),

        html.Hr(),



        ################################
        # Graph + Map Area
        ################################

        html.Div(

            className='row',

            style={
                'display': 'flex'
            },


            children=[


                html.Div(

                    id='graph-id',

                    className='col s12 m6'

                ),


                html.Div(

                    id='map-id',

                    className='col s12 m6'

                )

            ]

        )

    ])