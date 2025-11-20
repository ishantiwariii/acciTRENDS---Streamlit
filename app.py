import numpy as np 
import pandas as pd 
import plotly.express as px 
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="acciTRENDS", layout="wide")

# sidebar options x
st.sidebar.markdown(
    "<h1 style='text-align: center;'>acciTRENDS</h1>",
    unsafe_allow_html=True
)
st.sidebar.image(r"D:\acciTRENDS\logo.png")
st.sidebar.caption('Analyses road accident counts in India for the years 2018 — 2022')
option = st.sidebar.selectbox('Select one' ,['Overall Analysis' ,'Safer states & Union Territory','Dangerous States & Union Territory', 'State Comparison','Union Territories comparison' ])

# function for loading data and saving into cache
@st.cache_data
def load_data():
    df_states = pd.read_csv(r"D:\acciTRENDS\datasets\states_dataset.csv", index_col=0)
    df_ut = pd.read_csv(r"D:\acciTRENDS\datasets\ut_dataset.csv", index_col=0)
    return df_states, df_ut

df_states, df_ut = load_data()

# option selection 
if option == 'Overall Analysis':
    st.title("Overall Accident Analysis (2018–2022)")
    st.markdown("""
    ## 🗂️ Dataset Information

    - **Years Covered:** 2018 — 2022  
    - **Regions:** 28 States & 8 Union Territories  
    - **Source:** *Ministry of Road Transport & Highways (MoRTH)*  
    - **Columns:**  
        - State/UT  
        - Accident Count (Year-wise)  
        - Total accidents over 5 years   
    - **Data Type:** Cleaned numerical dataset  
    """)

    sde_option = st.sidebar.selectbox('Select one' ,['State Analysis', 'Union Terr. Analysis'])
    if sde_option == 'State Analysis':
      st.subheader("📈 State Accident Trend Comparison")
      opt = st.selectbox('Select the suitable graph',['Line-graph', 'Heatmap','Bar-Graph'])
      if opt == 'Line-graph':
        st.subheader("-- By using Line graph")
        fig = px.line(df_states.reset_index(), x='State', y=['2018','2019','2020','2021','2022'], markers=True,)
        st.plotly_chart(fig, use_container_width=True)

      elif opt == 'Heatmap':
        # heatmap 
        st.subheader("-- By using heatmap")
        fig2, ax = plt.subplots(figsize=(12, 6))
        fig = sns.heatmap(df_states, cmap='Reds', ax=ax)
        st.pyplot(fig2)
      
      elif opt == 'Bar-Graph':
         st.subheader('-- Bar Graph')
         fig = px.bar(df_states.reset_index(), x='State', y=['2018','2019','2020','2021','2022'],color='State', log_y=True)
         st.plotly_chart(fig, use_container_width=True)

      st.subheader("📊 Preview of States Dataset")
      st.dataframe(df_states)



    elif sde_option == "Union Terr. Analysis":
      st.subheader("📈 Union Terriotory Trend Comparison")
      opt = st.selectbox('Select the suitable graph',['Line-graph', 'Heatmap','Bar-Graph'])
      if opt == 'Line-graph' :
        # line graph 
        st.subheader("-- By using Line graph")
        fig = px.line(df_ut.reset_index(),
                      x='UTs', y=['2018','2019','2020','2021','2022'], markers=True,)
        st.plotly_chart(fig, use_container_width=True)

      elif opt == 'Heatmap':
        # heatmap 
        st.subheader("-- By using heatmap")
        fig2, ax = plt.subplots(figsize=(12, 6))
        fig = sns.heatmap(df_ut, cmap='Reds', ax=ax)
        st.pyplot(fig2)

      elif opt == 'Bar-Graph':
        st.subheader('--Bar Graph')
        fig = px.bar(df_ut.reset_index(), x='UTs', y=['2018','2019','2020','2021','2022'],color='UTs', log_y=True)
        st.plotly_chart(fig, use_container_width=True)
      
      st.subheader("📊 Preview of Union terr. Dataset")
      st.dataframe(df_ut)
        
    st.markdown("""
    ### 🗂️ Dataset Source  
    The accident dataset used in this dashboard is sourced from **Data.gov.in**,  
    the official open data portal of the Government of India.  

    👉 **Source:** https://www.data.gov.in/  
    👉 **Department:** Ministry of Road Transport & Highways (MoRTH)  
    """)


## safe states and union territories
elif option == 'Safer states & Union Territory':
  opt =st.sidebar.selectbox("Select here: ",['States', 'union territory'])
  if opt == 'States':
    st.title("States with least accident(10) : ")
    top_state = df_states['Total_5yr'].sort_values(ascending=True).head(10).reset_index()
    top_state = top_state.rename(columns={'index':'state'}) 
    fig =px.bar(top_state, x='State', y='Total_5yr', color='State', log_y=True) 
    st.plotly_chart(fig, use_container_width=True)

  elif opt == 'union territory':
      st.title("Union terr. with least accidents ")
      top_ut = df_ut['Total_5yr'].sort_values(ascending=True).reset_index()
      top_ut = top_ut.rename(columns={'index':'UT'}) 
      fig =px.bar(top_ut, x='UTs', y='Total_5yr', color='UTs', log_y=True) 
      st.plotly_chart(fig, use_container_width=True)
  
  st.markdown("""
  ### 🛡️ About the Safest States & Union Territories
  The regions listed here have recorded the **lowest number of road accidents** from **2018 to 2022**.  
  These low accident counts are generally influenced by factors such as:

  - Smaller population size  
  - Lower vehicle density  
  - Fewer highways and major roads  
  - Better compliance with traffic rules  
  - Limited commercial or heavy-vehicle movement

  Safe Union Territories (like **Lakshadweep**, **Daman & Diu**, **Andaman & Nicobar Islands**)  
  are especially low-risk due to their size and controlled transportation systems.

  These places represent the **lowest accident-prone regions** in India based on the dataset.
  """)


## Dangerous states and union terr.
elif option == 'Dangerous States & Union Territory':
  opt_2 =st.sidebar.selectbox('here:', ['States', 'union territory'])
  # for state
  if opt_2 == 'States':
    st.title("States with most accidents(10) : ")
    least_state = df_states['Total_5yr'].sort_values(ascending=False).head(10).reset_index()
    least_state = least_state.rename(columns={'index':'state'}) 
    fig =px.bar(least_state, x='State', y='Total_5yr', color='State', log_y=True) 
    st.plotly_chart(fig, use_container_width=True)

  # for union territory 
  elif opt_2 == 'union territory':
      st.title("Union terr. with most accidents ")
      least = df_ut['Total_5yr'].sort_values(ascending=False).reset_index()
      least = least.rename(columns={'index':'UT'}) 
      fig =px.bar(least, x='UTs', y='Total_5yr', color='UTs', log_y=True) 
      st.plotly_chart(fig, use_container_width=True)
  
  st.markdown("""
  ## ⚠️ Dangerous States & Union Territories (2018–2022)

  Some regions in India consistently report **high accident numbers**, making them statistically
  more **accident-prone** during the 5-year period from **2018 to 2022**.

  ---

  ### 🔥 What Makes a State or UT ‘Dangerous’?
  Areas with high accident counts generally have:

  - Large & dense populations  
  - Heavy commercial vehicle traffic  
  - Multiple national highways & expressways  
  - Fast urbanization  
  - High registered vehicle volume  
  - Congested road networks  

  These factors significantly increase the probability of road accidents.

  ---

  ### 🚨 Dangerous States
  States that frequently appear at the **top of accident statistics** include:

  - Tamil Nadu  
  - Karnataka  
  - Madhya Pradesh  
  - Maharashtra  
  - Uttar Pradesh  

  These states have high mobility, dense traffic flow, industrial zones, and urban hubs —  
  leading to **high accident risk**.

  ---

  ### 🚨 Dangerous Union Territories
  Some UTs such as:

  - **Delhi**  
  - **Jammu & Kashmir**  
  - **Ladakh**  

  report a higher number of accidents compared to other UTs.

  This is due to:

  - Urban congestion (Delhi)  
  - Mountainous terrain (J&K, Ladakh)  
  - Tourism pressure  
  - Busy interstate transport routes  

  """)


## State to state comparison
elif option == 'State Comparison':
  st.title("State Comparison")
  states = st.sidebar.multiselect("Select states:", df_states.index)

  if len(states) > 0:
        # select & transpose
        states_df = df_states.loc[states].T
        states_df = states_df.reset_index().rename(columns={'index': 'Year'})

        # melt into long format for plotly
        df_long = states_df.melt(id_vars='Year', var_name='State', value_name='Accidents')

        # plot line chart
        fig = px.line(
            df_long,
            x='Year',
            y='Accidents',
            color='State',
            markers=True,
            title="Accident Trends Across Selected States (2018–2022)", 
            log_y=True
        )

        st.plotly_chart(fig, use_container_width=True)
  else:
        st.warning("Please select at least one state to compare.")
  st.markdown("""
  ## 🔄 State vs State Comparison

  This section allows you to **compare multiple Indian states** based on their  
  year-wise accident trends from **2018 to 2022**.

  You can select any combination of states from the sidebar, and the dashboard will  
  visualize how accident counts have changed over the 5-year period.

  ### 🧩 What This Comparison Helps You Understand
  - How different states perform relative to each other  
  - Which states show continuous growth or decline in accidents  
  - The gap between high-accident and low-accident states  
  - Patterns across years like drops in 2020 (lockdown impact)  
  - Identify similar or contrasting accident trends  

  ### 📊 Visualization
  A dynamic **line chart** is shown where:
  - Each line represents a selected state  
  - The x-axis shows years (2018–2022)  
  - The y-axis shows accident counts  
  - Colors differentiate the states  
  - Hovering reveals exact yearly accident values  

  This makes it easy to compare multiple states at once and study their accident patterns visually.
  """)


## Union territorries to union territories comparison 
elif option == 'Union Territories comparison':
  st.title("Union Territories Comparison")
  union_t = st.sidebar.multiselect("Select states:", df_ut.index)
    
  if len(union_t) > 0:
        # select & transpose
        union_t_df = df_ut.loc[union_t].T
        union_t_df = union_t_df.reset_index().rename(columns={'index': 'Year'})

        # melt into long format for plotly
        df_long = union_t_df.melt(id_vars='Year', var_name='Union Terriotory', value_name='Accidents')

        # plot line chart
        fig = px.line(
            df_long,
            x='Year',
            y='Accidents',
            color='Union Terriotory',
            markers=True,
            title="Accident Trends Across Selected States (2018–2022)",
            log_y=True
        )

        st.plotly_chart(fig, use_container_width=True)

  else:
        st.warning("Please select at least one state to compare.")
  st.markdown("""
  ## 🔄 Union Terr. vs Union Terr Comparison

  This section allows you to **compare multiple Indian Union Terr.** based on their  
  year-wise accident trends from **2018 to 2022**.

  You can select any combination of Union Terr. from the sidebar, and the dashboard will  
  visualize how accident counts have changed over the 5-year period.

  ### 🧩 What This Comparison Helps You Understand
  - How different Union Terr perform relative to each other  
  - Which Union Terr show continuous growth or decline in accidents  
  - The gap between high-accident and low-accident Union Terr.
  - Patterns across years like drops in 2020 (lockdown impact)  
  - Identify similar or contrasting accident trends  

  ### 📊 Visualization
  A dynamic **line chart** is shown where:
  - Each line represents a selected Union Terr.
  - The x-axis shows years (2018–2022)  
  - The y-axis shows accident counts
  - Colors differentiate the Union Terr.
  - Hovering reveals exact yearly accident values  

  This makes it easy to compare multiple Union Terr. at once and study their accident patterns visually.
  """)
