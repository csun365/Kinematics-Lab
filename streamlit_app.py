import scipy
import pandas as pd
import streamlit as st
from scipy.optimize import curve_fit
import numpy as np
# import matplotlib.pyplot as plt

def func(x, a, b):
    return a * (1 - np.exp(-b * x))

st.title("Kinematics Lab Exponential Curve Fitter")
st.markdown("This tool accepts files with comma-separated values (CSV). \"Time (s)\" and \"Speed (m/s)\" (excluding quotations and extra spaces) should be existing column names on the file. These column names should be written on the first row of the file.")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

    X = df["Time (s)"]
    Y = df["Speed (m/s)"]

    popt, pcov = curve_fit(func, X, Y)
    str = "v = %f(1 - e$^{%ft}$)" % (popt[0], popt[1])
    st.write(str)
    # fig, ax = plt.subplots()
    # ax.scatter(X, Y, label="Data Collected", c="tab:orange")
    # ax.plot(np.arange(0,10,1), func(np.arange(0,10,1), popt[0], popt[1]))
    # ax.set_xlabel("Time (s)")
    # ax.set_ylabel("Speed (m/s)")
    # ax.legend()
    # st.pyplot(fig)
