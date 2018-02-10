import plotly
import pandas as pd


stt1 = open('us_states2.txt', 'r')
state_to_abb = {}
for line in stt1:
    line = line.strip().split("\t")
    stNm = line[0].title()
    state_to_abb[stNm] = line[1]
stt1.close()

file = open("vet_pop_real.txt", 'r')
lin1 = file.readline()
new = open('vet_pop_real2.txt', 'w')
new.write("CODE," + lin1)
new.write('\n')
new.close()
file.readline()
o = ["District of Columbia", "Puerto Rico"]
for line in file:
    new = open('vet_pop_real2.txt', 'a')
    state = (line.split(','))[1]
    line = line.strip()
    if state not in o:
        line = (state_to_abb[state] + "," + line)
        new.write(line)
        new.write('\n')
        new.close()

df = pd.read_csv('vetRpop.csv')
for col in df.columns:
    df[col] = df[col].astype(str)

scl = [[0.0, 'rgb(242,240,247)'], [0.2, 'rgb(218,218,235)'], [0.4, 'rgb(188,189,220)'], \
       [0.6, 'rgb(158,154,200)'], [0.8, 'rgb(117,107,177)'], [1.0, 'rgb(84,39,143)']]

df['text'] = df['state'] + '<br>' + 'Veteran Population: ' + df['total_vet_pop']

data = [dict(
    type='choropleth',
    colorscale=scl,
    autocolorscale=False,
    locations=df['CODE'],
    z=df['total_vet_pop'].astype(float),
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
    title='Veteran Population by State<br>(Hover for State Population)',
    geo=dict(
        scope='usa',
        projection=dict(type='albers usa'),
        showlakes=True,
        lakecolor='rgb(255, 255, 255)'),
)

fig = dict(data=data, layout=layout)
plotly.offline.plot(fig, filename='d3-cloropleth-map')
