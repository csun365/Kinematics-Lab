import scipy
import pandas as pd
import streamlit as st
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

def func(x, a, b):
    return a * (1 - np.exp(-b * x))

st.title("Kinematics Lab Exponential Curve Fitter")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

    X = df["Time (s)"]
    Y = df["Speed (m/s)"]

    popt, pcov = curve_fit(func, X, Y)
    str = "v = %f(1 - e$^{%ft}$)" % (popt[0], popt[1])
    st.write(str)
