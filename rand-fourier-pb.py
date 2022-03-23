import streamlit as st
import pandas as pd
import numpy as np

t = np.arange(0.00, 10*np.pi, 0.05)
data = pd.DataFrame({
  "sin+rand": np.random.uniform(-1,1, [1, len(t)])[0] + (4 / np.pi) * (np.sin(t) + np.sin(3*t)/3 + np.sin(5*t)/5),
  "sin": (4 / np.pi) * (np.sin(t) + np.sin(3*t)/3 + np.sin(5*t)/5),
  "rand": np.random.uniform(-1,1, [1, len(t)])[0] - 5,
  "t": t
})
data = data.set_index('t')
st.dataframe(data)
st.line_chart(data)
