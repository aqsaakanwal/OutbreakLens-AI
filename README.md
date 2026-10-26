# 🔬 OutbreakLens AI
### Foodborne Surveillance Explorer | Interactive Analytics for Public Health Research

<p align="center">
  <strong>Turning foodborne outbreak records into accessible, interactive insights.</strong>
</p>

<p align="center">
  An exploratory data analysis platform for investigating foodborne outbreak surveillance data through interactive dashboards, descriptive analytics, and research-oriented data exploration.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-Interactive%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly">
</p>

---

## 📌 Overview

Foodborne illness surveillance data can help researchers explore reported outbreaks, implicated food vehicles, etiological agents, settings, and associated health outcomes. However, working directly with large tabular datasets can make exploratory analysis less accessible to users without programming experience.

**OutbreakLens AI** addresses this usability challenge through an interactive, web-based environment for exploring foodborne outbreak records.

Built with Python and Streamlit, the application combines data filtering, visual exploration, descriptive summaries, and research-oriented question exploration in a unified interface.

Rather than presenting data as static tables alone, OutbreakLens AI helps users investigate patterns, compare available categories, identify data-quality concerns, and formulate questions for further research.

> **Project principle:** Make surveillance data easier to explore while keeping interpretation transparent and acknowledging the limitations of reported records.

## 🎯 Objectives

- Make foodborne outbreak data accessible through an intuitive interface.
- Explore temporal, geographic, etiological, and food-vehicle patterns in available records.
- Summarize reported illnesses, hospitalizations, and deaths where data are available.
- Support descriptive research questions without requiring users to write code.
- Highlight missing information and limitations that matter when interpreting surveillance data.
- Encourage evidence-aware exploration rather than unsupported causal or predictive claims.

## ✨ Key Features

### 🏠 1. Interactive Overview Dashboard

A centralized starting point for understanding the selected dataset.

- Summary metrics based on available records.
- High-level views of reported outbreak characteristics.
- Interactive visualizations for initial exploration.
- A consistent interface for navigating analytical sections.

### 🔎 2. Outbreak Explorer

Investigate records using available dataset attributes.

- Filter by reporting year and geographic location.
- Explore etiology and outbreak settings.
- Examine associated food vehicles and food categories.
- Review selected records in tabular form.
- Inspect filtered subsets and download data where supported.

*The filters and results depend on the columns available in the loaded dataset.*

### 📊 3. Interactive Data Visualizations

Use charts to investigate distributions and relationships within the available records.

Potential analytical perspectives include:

- Reported records across years.
- Geographic distribution of records.
- Frequently reported etiological agents.
- Food vehicles and food categories.
- Outbreak settings.
- Reported illnesses, hospitalizations, and deaths.

Interactive charts can help users compare categories and identify patterns that merit closer investigation.

### 💬 4. Ask Research AI

A research-question interface for supported descriptive queries.

The interface uses rule-based logic to route
