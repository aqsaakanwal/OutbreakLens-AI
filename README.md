# 🔬 OutbreakLens AI — Foodborne Surveillance Explorer

**Explore foodborne outbreak data through interactive visualizations and descriptive analytics.**

OutbreakLens AI is a Streamlit-based exploratory data analysis application designed to help users investigate foodborne outbreak records, examine trends, explore reported contributing factors, and understand outbreak-related outcomes through interactive charts and tables.

## ✨ Features

- **Interactive Dashboard:** Explore key statistics and summaries from the dataset.
- **Outbreak Explorer:** Filter records by available attributes such as year, state, etiology, setting, and food vehicle.
- **Data Visualizations:** Examine patterns and distributions through interactive charts.
- **Research Insights:** Explore descriptive findings and potential questions for further investigation.
- **Ask Research AI:** Use a rule-based question interface to explore supported descriptive questions.
- **Data Access:** View and download filtered data where supported.
- **Data Quality Review:** Examine missing values and other dataset characteristics.
- **Methodology:** Review the scope, limitations, and intended use of the application.

## 🛠️ Technology Stack

- Python
- Streamlit
- Pandas
- NumPy
- Plotly

## 📊 Dataset

The application is designed to explore foodborne outbreak surveillance records, including variables such as reporting year, location, etiology, setting, food vehicle, illnesses, hospitalizations, and deaths, when available.

The dataset's coverage and completeness may vary. Reported records should not automatically be interpreted as a complete count of all outbreaks or cases.

## 🚀 Run Locally

1. Clone this repository:

   ```bash
   git clone https://github.com/aqsaakanwal/OutbreakLens-AI.git
   cd OutbreakLens-AI
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the application:

   ```bash
   streamlit run app.py
   ```

## ⚠️ Scope and Limitations

OutbreakLens AI is an exploratory data analysis and research-support prototype. Its charts and summaries describe the available records; they do not establish causation, estimate population-level incidence, or predict future outbreaks.

The rule-based research interface is not a trained AI model and does not replace epidemiological investigation, laboratory confirmation, or public health guidance.

## 🎯 Project Goal

To make foodborne outbreak surveillance data easier to explore, interpret, and discuss through an accessible interactive interface.

## 👩‍💻 Author

**Aqsa Kanwal**

Food Science & Technology | Data Analytics | AI for Food Safety

---

*Developed as an exploratory prototype for foodborne surveillance data analysis.*
