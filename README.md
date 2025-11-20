# 🚀 acciTRENDS — Road Accident Analytics (2018–2022)

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white"/>
  <img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-Interactive-red?logo=streamlit&logoColor=white"/>
  <img alt="Plotly" src="https://img.shields.io/badge/Plotly-Visualizations-6f42c1?logo=plotly&logoColor=white"/>
  <img alt="Pandas" src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white"/>
  <img alt="Status" src="https://img.shields.io/badge/Status-Active-brightgreen"/>
</p>

---

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