import statistics as st
import pandas as pd
import plotly.express as pe
import plotly.figure_factory as pf
import numpy as np

data = pd.read_csv("college.csv")
englishscore = data["TOEFL Score"].tolist()
chanceofadmit = data["Chance of Admit "].tolist()
graph = pe.scatter(x=englishscore,y=chanceofadmit)
graph.show()
arrayenglish = np.array(englishscore)
admit= np.array(chanceofadmit)

m,c = np.polyfit(englishscore, chanceofadmit, 1)
y=[]

for x in arrayenglish:
    newy=m*x+c
    y.append(newy)
graph1 = pe.scatter(x=arrayenglish, y=admit)
graph1.update_layout(shapes=[dict(type="line", y0=min(y), y1=max(y), x0=min(englishscore), x1=max(englishscore))])
graph1.show()
