# 🚀 acciTRENDS — Road Accident Analytics (2018–2022)


## 🔍 Project Overview

**acciTRENDS** is a data analytics project that analyses road accident counts in India for the years **2018 — 2022**.  
It provides cleaned datasets for **States** and **Union Territories (UTs)**, performs EDA (trend analysis, top/bottom rankings, growth rates, heatmaps) and exposes interactive visualizations via a **Streamlit dashboard**.

---

## 📚 Dataset

- **Source:** Ministry of Road Transport & Highways (MoRTH), Government of India — *Road Accidents in India (2018–2022)* (data extracted & cleaned for this project).  
- **Format used in repo:** `states_dataset.csv` and `ut_dataset.csv` (cleaned, accident counts by year).
- **Columns:**
  - `States/UTs` (region name) — or used as index
  - `2018`, `2019`, `2020`, `2021`, `2022` (accident counts)
  - Derived columns used: `Total_5yr`, `Growth_%`

---

## 🎯 Objectives

- Clean raw state/UT accident data
- Produce state-wise and UT-wise EDA
- Visualize trends, growth and rankings
- Provide interactive Streamlit dashboard for exploration
- Export cleaned datasets for reuse

---

## 🛠 Tech Stack / Tools

- Python 
- pandas, numpy (data wrangling)  
- plotly.express (interactive charts)  
- matplotlib / seaborn (static visuals, heatmaps)  
- Streamlit (dashboard)  
- Git & GitHub

---

## project live on 
 - https://acci-trends.streamlit.app/