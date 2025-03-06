
import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("Streamlit Demo App")
st.write("Explore the capabilities of Streamlit!")

# Slider widget
x = st.slider("Select a value", 0, 100, 50)
st.write(f"You selected: {x}")

# Real-time chart
st.subheader("Live Data Chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.line_chart(chart_data)

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

# Progress bar
st.subheader("Progress Simulation")
progress_bar = st.progress(0)
for i in range(100):
    time.sleep(0.02)
    progress_bar.progress(i + 1)

st.success("Demo completed! 🚀")
