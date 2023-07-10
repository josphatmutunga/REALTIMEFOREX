import streamlit as st
import requests

github_url="https://raw.githubusercontent.com/JOSPHATT/REALTIMEFOREX.py/main/realtimeforex.json"
import json
p = requests.get(github_url)
p.text
github_jsonforex_dictionary=json.loads(p.text)
Total_entries=print(len(github_jsonforex_dictionary.values()))github_url="https://raw.githubusercontent.com/JOSPHATT/REALTIMEFOREX.py/main/realtimeforex.json"
import json
p = requests.get(github_url)
p.text
github_jsonforex_dictionary=json.loads(p.text)
#Total_entries=print(len(github_jsonforex_dictionary.values()))

import pandas as pd
from pandas import json_normalize
column_names=[i for i in github_jsonforex_dictionary.keys()]
df = pd.DataFrame(github_jsonforex_dictionary.values())
Timeseries=pd.DataFrame(github_jsonforex_dictionary.keys())
times=Timeseries.values.tolist()
#print(times)
Tyms=[]
for tym in times:
    s=tym[0]
    p=[' '.join(s.split())]
    n_p=p[0].split()
    r=n_p[3].split(":")
    f=r[0]+r[1]+r[2]
    d=n_p[2]+f
    Tyms.append(int(d))
#print(Tyms)
Timestamps=pd.DataFrame(Tyms)
#print(Timestamps)
DF=df.T
DF.columns=column_names
DF=DF.rename_axis(['currency_pair']).reset_index()
