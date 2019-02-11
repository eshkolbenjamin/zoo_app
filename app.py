import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

############# Make changes here


app = dash.Dash()
server = app.server

app.layout = html.Div(children=[
    html.H1('My changed ID'),
    dcc.Graph(
        id='this_is_an_id',
        figure={
            'data': [
                {'x': ['Thing1', 'Thing2', 'Thing3'], 'y': [8, 2, 3], 'type': 'bar', 'name': 'new label 1'},
                {'x': ['Thing1', 'Thing2', 'Thing3'], 'y': [3, 4, 5], 'type': 'bar', 'name': 'new label 2'},
            ],
            'layout': {
                'title': "Because friends don't let friends use Microsoft Powerpoint",
                'xaxis':{'title':'Choice of data visualization'},
                'yaxis':{'title':'Approval rating by average data scientist'},
            }
        }
    )]
)


###### Don't change anything here



if __name__ == '__main__':
    app.run_server()
