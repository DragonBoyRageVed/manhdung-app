import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Excel Data Viewer", layout="centered")

st.title("📊 Interactive Excel Data Explorer")

# Upload Excel File
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

if uploaded_file:
    # Read Excel file
    df = pd.read_excel(uploaded_file)
    st.success("Excel file loaded successfully!")

    if st.checkbox("Show raw data"):
        st.dataframe(df)

    # Get numeric columns
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()

    if len(numeric_cols) >= 2:
        # Select columns for plotting
        x_col = st.selectbox("Choose X-axis", numeric_cols)
        y_col = st.selectbox("Choose Y-axis", numeric_cols, index=1)

        # Create interactive Plotly chart
        fig = px.line(df, x=x_col, y=y_col, title=f"{y_col} over {x_col}")
        st.plotly_chart(fig)
    else:
        st.warning("The uploaded file must contain at least two numeric columns.")
else:
    st.info("Please upload a valid Excel file to begin.")






 