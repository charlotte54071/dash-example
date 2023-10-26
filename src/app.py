from dash import Dash,html,dash_table,dcc,callback,Output,Input
import pandas as pd
import plotly.express as px

#import the data
df=pd.read_excel('dash_visu_export.xlsx',sheet_name='Sheet1')

#components,
app=Dash(__name__)
server = app.server


#layout
app.layout=html.Div([
    html.Div(children='my first App with Data'),
    html.Hr(),
    dcc.RadioItems(options=['PV-facade-% south','PV Ost-West Fassade [%]'],value='PV Ost-West Fassade [%]',
                   id='control-and-radio-item'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=6),
    dcc.Graph(figure={},id='control-and-graph')
])


#add controls to build the interaction
@callback(
    Output(component_id='control-and-graph',component_property='figure'),
    Input(component_id='control-and-radio-item',component_property='value')
)
def update_grapg(col_chosen):
    fig=px.histogram(df,x='cluster',y=col_chosen,histfunc='avg')
    return fig

#run the app
if __name__=='__main__':
    app.run_server(debug=True)

