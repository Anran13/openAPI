import tools.taipei
import streamlit as st
import pandas as pd

st.title("YouBike Real-time Data")

# Use session state to store the data once fetched to avoid re-fetching on every interaction.
if 'data' not in st.session_state:
    st.session_state.data = None

# The button to fetch or refresh the data.
if st.button("Fetch/Refresh YouBike Data"):
    with st.spinner("Fetching data from the server..."):
        try:
            # Fetch data and store it in session state
            st.session_state.data = tools.taipei.get_youbikes()
            st.success("Data fetched successfully!")
        except Exception as e:
            st.error(f"Failed to fetch data: {e}")
            st.session_state.data = None # Clear data on error

# Only display the panels if data has been successfully fetched.
if st.session_state.data:
    # Convert list of dicts to a pandas DataFrame for easier manipulation
    df = pd.DataFrame(st.session_state.data)
    
    # Data cleaning for map: ensure lat/lng are numeric and not null
    df['lat'] = pd.to_numeric(df['lat'], errors='coerce')
    df['lng'] = pd.to_numeric(df['lng'], errors='coerce')
    df.dropna(subset=['lat', 'lng'], inplace=True)

    # --- 1. Left panel: Sidebar for filtering ---
    with st.sidebar:
        st.header("Filter Options")
        # Get unique areas from the 'sarea' column and add an 'All' option
        areas = sorted(df['sarea'].unique())
        areas.insert(0, "All Areas")
        
        selected_area = st.selectbox(
            "Choose a station area:",
            options=areas
        )

    # --- 2. Right panel: Dataframe display ---
    st.header(f"Displaying Stations in: {selected_area}")

    filtered_df = df if selected_area == "All Areas" else df[df['sarea'] == selected_area]

    st.dataframe(filtered_df)

    # --- 3. Bottom panel: Map display ---
    st.header("Station Map")
    
    # st.map requires 'lat' and 'lon' columns. The source data has 'lat' and 'lng'.
    map_df = filtered_df.copy().rename(columns={'lng': 'lon'})
    if not map_df.empty:
        st.map(map_df)
    else:
        st.warning("No data to display on the map for the selected area.")
else:
    st.info("Click the button above to fetch and display YouBike data.")