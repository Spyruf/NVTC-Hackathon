import plotly
import pandas as pd
import extract_state_words
import txt_to_csv

extract_state_words.run()
txt_to_csv.run()


df = pd.read_csv('f_heat.csv')
for col in df.columns:
    df[col] = df[col].astype(str)

scl = [[0.0, 'rgb(242,240,247)'], [0.2, 'rgb(218,218,235)'], [0.4, 'rgb(188,189,220)'], \
       [0.6, 'rgb(158,154,200)'], [0.8, 'rgb(117,107,177)'], [1.0, 'rgb(84,39,143)']]

df['text'] = df['STATE'] + '<br>' + 'Veterans Found: ' + df['COUNT'] + " users" + '<br>' + 'Popular Words: ' + '<br>' \
             + df['WORDS']

data = [dict(
    type='choropleth',
    colorscale=scl,
    autocolorscale=False,
    locations=df['CODE'],
    z=df['COUNT'].astype(float),
    locationmode='USA-states',
    text=df['text'],
    marker=dict(
        line=dict(
            color='rgb(255,255,255)',
            width=2
        )),
    colorbar=dict(
        title="Population")
)]

layout = dict(
    title='Twitter Veteran Population by State<br>(Hover for Popular Words)',
    geo=dict(
        scope='usa',
        projection=dict(type='albers usa'),
        showlakes=True,
        lakecolor='rgb(255, 255, 255)'),
)

fig = dict(data=data, layout=layout)
plotly.offline.plot(fig, filename='d3-cloropleth-map.html')
