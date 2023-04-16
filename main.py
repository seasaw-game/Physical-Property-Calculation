import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

### composition
# h2
# o2
# n2
# h2o
# ch4
# c2h6
# c3h8
# c4h10

### property
# density[kg/m3]
# Thermal Conductivity[W/m-k]
# specific heat[J/kg-s]
# viscosity[Pa-s]

# volume fraction
volf = []
volf[0] = st.number_input("H2")
volf[1] = st.number_input("O2")
volf[2] = st.number_input("H2O")
volf[3] = st.number_input("CH4")
volf[4] = st.number_input("C2H6")
volf[5] = st.number_input("C3H8")
volf[6] = 100 - volf.sum()
st.text("N2")
st.text(volf[6])
