import streamlit as st
import pandas as pd
import numpy as np


def upload_data():
    """
    Handles the file upload and download logic in the sidebar.
    """
    # Initialize session state if it doesn't exist. This prevents errors on first run.
    if 'uploaded_df' not in st.session_state:
        st.session_state['uploaded_df'] = None

    uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.session_state['uploaded_df'] = df
            st.sidebar.success("File uploaded successfully!")
        except Exception as e:
            st.sidebar.error(f"Error reading file: {e}")
            st.session_state['uploaded_df'] = None


def main():
    """
    Using streamlit:
    1. upload csv file to read data by the upload button on the left panel
    2. preview the data in the data editor on the right panel
    3. add/remove columns and modify values/rows directly in the data editor panel
    5. generate plots according to chosen columns of the uploaded data
    6. download the modified data as a csv file
    """
    st.set_page_config(layout="wide")
    st.title("Interactive CSV Editor and Plotter")

    upload_data()

    if 'uploaded_df' in st.session_state and st.session_state['uploaded_df'] is not None:
        df = st.session_state['uploaded_df']

        st.header("Edit Your Data")
        st.info("You can edit data, add/remove rows in the table below.")

        edited_df = st.data_editor(df, num_rows="dynamic", key="data_editor")
        st.session_state['uploaded_df'] = edited_df
        st.write("---")

        st.header("Generate a Plot from Data")
        numeric_columns = edited_df.select_dtypes(include=np.number).columns.tolist()
        all_columns = edited_df.columns.tolist()

        if not numeric_columns:
            st.warning("No numeric columns found in the data to plot.")
            return

        plot_type = st.selectbox("Select plot type", ["Line Chart", "Bar Chart", "Scatter Plot", "Area Chart"])

        if plot_type in ["Line Chart", "Bar Chart", "Area Chart"]:
            x_axis = st.selectbox("Choose column for X-axis", options=all_columns, key="xy_x")
            y_axis_options = [col for col in numeric_columns if col != x_axis]
            if y_axis_options:
                y_axis = st.multiselect("Choose column(s) for Y-axis", options=y_axis_options, default=y_axis_options[0] if y_axis_options else [])
                if y_axis:
                    plot_df = edited_df.set_index(x_axis)
                    if plot_type == "Line Chart": st.line_chart(plot_df[y_axis])
                    elif plot_type == "Bar Chart": st.bar_chart(plot_df[y_axis])
                    elif plot_type == "Area Chart": st.area_chart(plot_df[y_axis])
            else:
                st.warning(f"No numeric columns available for Y-axis when X-axis is '{x_axis}'.")

        elif plot_type == "Scatter Plot":
            x_axis = st.selectbox("Choose X-axis (numeric)", options=numeric_columns, key='scatter_x')
            y_options = [col for col in numeric_columns if col != x_axis]
            if y_options:
                y_axis = st.selectbox("Choose Y-axis (numeric)", options=y_options, key='scatter_y')
                st.scatter_chart(edited_df, x=x_axis, y=y_axis)
            else:
                st.warning("Not enough distinct numeric columns for a scatter plot.")
    else:
        st.info("Please upload a CSV file using the sidebar to get started.")

if __name__ == '__main__':
    main()
    