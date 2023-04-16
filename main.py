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
"---"
st.title("ガス物性計算アプリ")
st.text("更新日：2023/4/16")
"---"
### input volume fraction
zero_data = np.zeros(shape=(1,len(COMPOSE_LIST)))
volf = pd.DataFrame(zero_data, columns=COMPOSE_LIST)


with st.sidebar:
    st.text("組成[vol%]を入力")
    for i in COMPOSE_LIST:
        volf[i] = st.number_input(i,format="%f")
    total = volf.sum(axis=1)*100
    st.text(f"Total={total}%")

st.text("ガス組成")
volf
"---"
### setting temperature list
with st.sidebar:
    "---"
    prop_col1, prop_col2 = st.columns(2)
    # with prop_col1:
    temp_min, temp_max = st.slider("温度範囲", min_value=0, max_value=2000, value=(0,2000), step=100)
    # with prop_col2:
    temp_temp = (temp_max-temp_min)/100
    temp_interval = st.slider("出力温度点数", min_value=2, max_value=int(temp_temp)*2+1, value=int(temp_temp+1), step=1)
"---"
temp_list = np.linspace(temp_min, temp_max, temp_interval)
thermophysic_list = pd.DataFrame(temp_list, columns=["Temperature[C]"])
thermophysic_list["Temperature[K]"] = temp_list+273.15

### calc thermophysic
thermophysic_list["Density[kg/m3]"] = thermophysic_list["Temperature[K]"] * 0.001 + 1
thermophysic_list["Thermal Conductivity[W/m-k]"] = thermophysic_list["Temperature[K]"] * 0.002 + 0.1
thermophysic_list["Specific Heat[J/kg-s]"] = thermophysic_list["Temperature[K]"] * 0.1 + 1000
thermophysic_list["Viscosity[Pa-s]"] = thermophysic_list["Temperature[K]"] * 0.0001 + 0.001

thermophysic_list
"---"
