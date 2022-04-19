from collections import namedtuple

import math
import pandas as pd
import streamlit as st

import pandas as pd
import requests
from datetime import datetime as dt




st.title("Bitcoin prices")
days=st.slider('No Of days',min_value=1,max_value=365,value=90)

currency=st.radio('Currency', ('cad','usd','inr'))

s='https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency='+currency+'&days='+str(days-1)+'&interval=daily'
r = requests.get(s, auth=('user', 'pass'))
data=r.json()



d=pd.DataFrame(data=data['prices'],columns=['date','Prices'])
d['date']=pd.to_datetime(d['date'],unit='ms')
d['date']=d['date'].apply(lambda x:x.date())
d.set_index('date',inplace=True)

st.line_chart(d)

st.write("Average price during this time was ",d['Prices'].mean()," ",currency)