import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

### Composition
COMPOSE_LIST = ["h2","o2","n2","h2o","ch4","c2h6","c3h8","c4h10"]

### Property
# Density[kg/m3]
# Thermal Conductivity[W/m-k]
# Specific Heat[J/kg-s]
# Viscosity[Pa-s]
PROPERTY_LIST = ["density","thermal_conductivity","specific_heat","viscosity"]

# input volume fraction
zero_data = np.zeros(shape=(1,len(COMPOSE_LIST)))
volf = pd.DataFrame(zero_data, columns=COMPOSE_LIST)

for i in COMPOSE_LIST:
    volf[i] = st.number_input(i)

total = volf.sum(axis=1)*100
st.text(f"Total={total}%")

st.text("ガス組成")
volf

# setting property
col1, col2, col3 = st.columns(3)
with col1:
    temp_min = st.slider("最低温度", min_value=0, max_value=2000, value=0, step=100)
with col2:
    temp_max = st.slider("最高温度", min_value=500, max_value=2000, value=2000, step=100)
with col3:
    temp_interval = st.slider("出力点数", min_value=int((temp_max-temp_min)/100+1), max_value=int((temp_max-temp_min)/100)*2+1, value=int((temp_max-temp_min)/100+1), step=int((temp_max-temp_min)/100+1)-1)

temp_list = np.linspace(temp_min, temp_max, temp_interval)
thermophysic_list = pd.DataFrame(temp_list, columns=["Temperature[C]"])
thermophysic_list["Temperature[K]"] = temp_list+273.15
thermophysic_list

for i in PROPERTY_LIST:
    st.text(f"{i}")
