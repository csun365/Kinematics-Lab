import scipy
import pandas as pd
import streamlit as st
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

def func(x, a, b):
    return a * (1 - np.exp(-b * x))

st.title("Kinematics Lab Exponential Curve Fitter")
st.markdown("This tool accepts numbers pasted directly from your lab on Google Sheets. They should be separated by spaces (which is the default after you paste them in). Please do not add anything after you have pasted in the numbers.")
X_str = st.text_input("Paste in your data from the time column: ").strip()
if len(X_str) != 0:
    X = np.array([float(i) for i in X_str.split(" ")])
    Y_str = st.text_input("Paste in your data from the speed column: ").strip()
    if len(Y_str) != 0:
        Y = np.array([float(i) for i in Y_str.split(" ")])
        if X.shape[0] != Y.shape[0]:
            st.write("Error: Please ensure that your time data and speed data have the same number of elements.")
        else:


# uploaded_file = st.file_uploader("Choose a file")
# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)
#     st.write(df)
#
#     X = df["Time (s)"]
#     Y = df["Speed (m/s)"]

            try:
                popt, pcov = curve_fit(func, X, Y)
                str = "$v = %f(1 - e^{%ft})$" % (popt[0], popt[1])
                st.header("Equation for Velocity:")
                st.write(str)
                fig, ax = plt.subplots()
                ax.scatter(X, Y, label="Data Collected", c="tab:orange")
                ax.plot(np.arange(0,10,1), func(np.arange(0,10,1), popt[0], popt[1]))
                ax.set_xlabel("Time (s)")
                ax.set_ylabel("Speed (m/s)")
                ax.legend()
                st.pyplot(fig)
            except:
                st.write("The curve fitter was unable to find optimal parameters for your data. Please confirm that you inputted data for time and speed.")
