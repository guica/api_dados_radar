# -*- coding: utf-8 -*-
# standard library
import os

# dash libs
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.figure_factory as ff
import plotly.graph_objs as go

# pydata stack
import pandas as pd
from sqlalchemy import create_engine

# set params
# conn = create_engine('sqlite:///db.sqlite3')
MAPBOX_KEY = 'pk.eyJ1IjoiY2hyaWRkeXAiLCJhIjoiY2ozcGI1MTZ3MDBpcTJ3cXR4b3owdDQwaCJ9.8jpMunbKjdq1anXwU5gxIw'
SAO_PAULO_LAT = -23.5505
SAO_PAULO_LON = -46.6333

df = pd.read_csv('data/base_radares_processed.csv')
contagens = pd.read_csv('data/contagens_201911091242.csv')
contagens['data_e_hora'] = pd.to_datetime(contagens['data_e_hora'])
contagens['hora'] = contagens['data_e_hora'].dt.hour

lote_options = list(df['lote'].sort_values(ascending=True).unique())
equipamento_options = list(df['tipo_equip'].sort_values(ascending=True).unique())
qtde_fxs = list(df['qtde_fxs_f'].sort_values(ascending=True).unique())
velocidade  = list(df['velocidade'].sort_values(ascending=True).unique())

###########################
# Data Manipulation / Model
###########################

# def fetch_data(q):
#     df = pd.read_sql(
#         sql=q,
#         con=conn
#     )
#     return df

def get_radares_df():
    return pd.read_csv('data/')


def get_radares():

    radares = fetch_data(
        '''
        select 
            lote,
            codigo,
            endereco,
            sentido,
            referencia,
            tipo_equip,
            enquadrame,
            qtde_fxs_f,
            velocidade,
            latitude_l
        from base_radares;
        '''
    )
    return


def radares_map(df):
    
    return {
        'data': [{
            'lat': df['lat'],
            'lon': df['lon'],
            'customdata': df['codigo'],
            'marker': {
                'color': df['lote'],
                'size': 8,
                'opacity': 0.6
            },
            'type': 'scattermapbox'
        }],
        'layout': {

            'mapbox': {
                "accesstoken": MAPBOX_KEY,
                "center": {
                    "lat": SAO_PAULO_LAT,
                    "lon": SAO_PAULO_LON
                },
                "pitch": 0,
                "zoom": 9,
                "style": "dark"
            },
            'hovermode': 'closest',
            'margin': {'l': 35, 'r': 35, 'b': 35, 't': 45},
            'title': 'Cada Ponto e um Radar',
            'height':500,
        }
    }


def graph(df, tipo):

    xy = df[df['tipo'] == tipo][['hora','contagem']]

    x = xy['hora'].values.tolist()

    y = xy['contagem'].values.tolist()

    return go.Bar(name=tipo, x=x, y=y)


def contagem_por_hora_graph(localidade):
    localidade = float(localidade.split('-')[0])
    df_count = contagens[contagens['localidade'] == localidade]
    df_count = df_count[(df_count['data_e_hora'] >= '2018-02-01') & (df_count['data_e_hora'] < '2018-02-02')]

    fig = go.Figure(data=[
            graph(df_count, 0),
            graph(df_count, 1),
            graph(df_count, 2),
            graph(df_count, 3),
        ], layout = go.Layout(title='Contagens de veículos por hora no dia 01/02/2018', barmode='stack')
    )
    
    return fig



#########################
# Dashboard Layout / View
#########################

# Set up Dashboard and create layout
app = dash.Dash()
app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})


app.layout = html.Div([

    # title - Row

    html.Div([

        html.H1(
            'RADARES DE SAO PAULO',
            style={
                'font-family': 'Helvetica',
                'margin-top': '25',
                'margin-bottom': '0'
            },
            className='eight columns'
        ),
        html.Img(
            src="https://retina-vision-images.s3.amazonaws.com/media/admin-interface/logo/logo_horizontal.png",
            className='two columns',
            style={
                'height': '9%',
                'width': '9%',
                'float': 'right',
                'padding-top': 10,
                'padding-right': 0
            },
        ),
        html.P(
            'Dando Acesso aos dados de radares do município de são paulo',
            style={
                'font-family': 'Helvetica',
                'font-size': '120%',
                'width': '80%'
            },
            className='eight columns'
        ),

    ], className='row'),

    # selectors
    html.Div([

        html.Div([
            html.P('Lote:'),
            dcc.Checklist(
                id='lote-filter-id',
                options=[{'label':i,'value':i} for i in lote_options],
                values=[value for value in lote_options],
                labelStyle={'display': 'inline-block'}
            )
        ], className='six columns', style={'margin-top': '10'}),

        html.Div([

            html.P('Quantidade de Faixas'),
            dcc.Dropdown(
                id='qtde_fxs-filter-id',
                options=[{'label':i,'value':i} for i in qtde_fxs],
                value=[value for value in qtde_fxs],
                multi=True
            )

        ], className='two columns', style={'margin-top': '10'}),

        html.Div([

            html.P('Velocidade'),
            dcc.Dropdown(
                id='velocidade-filter-id',
                options=[{'label':i,'value':i} for i in velocidade],
                value=[value for value in velocidade],
                multi=True,
            )

        ], className='two columns', style={'margin-top': '10'})

    ], className='row'),

    ## map + table + hist

    html.Div([

        html.Div([
            html.Div(id='text-content'),
            dcc.Graph(
                id='radar-map',
                style={'margin-top': '20'}
            )
        ], className='six columns'),

        html.Div([
            dcc.Graph(
                id='contagem-graph',
                style={'margin-top': '20'}
            )
        ], className='six columns')


    ], className='row')

], className='ten columns offset-by-one')




#############################################
# Interaction Between Components / Controller
#############################################


@app.callback(
    Output('radar-map','figure'),
    [
        Input('lote-filter-id','values'),
        Input('qtde_fxs-filter-id','value'),
        Input('velocidade-filter-id','value'),
    ]
)
def update_map(lote, qtde_fxs, velocidade):

    print('*** lote: {}, qtde_fxs: {}, velocidade: {}'.format(lote, qtde_fxs, velocidade))

    dff = df[df['lote'].isin(lote) & df['qtde_fxs_f'].isin(qtde_fxs) & df['velocidade'].isin(velocidade)]

    return radares_map(dff)


@app.callback(
    Output('text-content', 'children'),
    [
        Input('radar-map', 'hoverData')
    ]
)
def update_text(hoverData):
    s = df[df['codigo'] == hoverData['points'][0]['customdata']]
    return html.H3(
        'Radar: {} - {} '.format(
            s.iloc[0]['codigo'],
            s.iloc[0]['endereco'],
        )
    )

@app.callback(
    Output('contagem-graph', 'figure'),
    [
        Input('radar-map', 'clickData')
    ]
)
def update_text(clickData):
    return contagem_por_hora_graph(clickData['points'][0]['customdata'])

# @app.callback(
#     Output('')
# )

# start Flask server
if __name__ == '__main__':
    app.run_server(
        debug=True,
        host='0.0.0.0',
        port=8050
    )