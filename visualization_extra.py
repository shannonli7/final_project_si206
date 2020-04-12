import json
import os
import plotly.graph_objects as go
import numpy as np
#visualization for the audio analysis for A Change of Heart By The 1975

try:
    dir = os.path.dirname(__file__)
    full_path = os.path.join(dir,"audio_analysis.json")
    in_file = open(full_path, 'r')
    data = in_file.read()
    lst_of_dictionary = json.loads(data)
    in_file.close()
except:
    print("Problem reading the input file")
    lst_of_dictionary = {}

lst_of_keys = []
confidence = []
duration = []
for dictionary in lst_of_dictionary:
    lst_of_keys.append(dictionary.keys())

for dictionary in lst_of_dictionary:
    confidence = dictionary["confidence"]
    duration = dictionary["duration"]

#print(confidence)
#interval of duration of A Change of Heart By The 1975 in terms of seconds (4:43 minute equivalent))
interval = []
total = 0
for num in range(110):
    total += 2.57
    interval.append(round(total,2))

x_rev = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=interval, y=confidence, name="Duration",
    line_color='rgb(231,107,243)',
    fill='tozeroy'
))

fig.update_layout(title='Audio Analysis of Loudness Level through A Change of Heart By The 1975',
                   xaxis_title='Duration of Song (in seconds (4.43 minute))',
                   yaxis_title='Loudness Level')
fig.update_layout(title={'y':0.9,'x':0.5,'xanchor': 'center','yanchor': 'top'})

fig.update_yaxes(tick0=0.25, dtick=0.5)
fig.update_traces(mode='lines')

fig.show()



