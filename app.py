
import re
import streamlit as st
import pandas as pd
import plotly.express as px

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="OutbreakLens AI | Foodborne Surveillance",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# PROFESSIONAL WEBSITE DESIGN
# =========================================================
NAVY = "#14243A"
TEAL = "#0F8278"
MINT = "#DDF4EF"
BG = "#F4F7FA"
TEXT = "#243449"
MUTED = "#64748B"
BORDER = "#DFE7EF"
PALETTE = ["#0F8278", "#4776A8", "#E6A23C", "#8267B1", "#D96C75"]

st.markdown("""
<style>
:root {
    --navy: #14243A;
    --teal: #0F8278;
    --bg: #F4F7FA;
    --text: #243449;
    --muted: #64748B;
    --border: #DFE7EF;
}

/* Overall page */
.stApp {
    background: #F4F7FA;
    color: #243449;
}

[data-testid="stAppViewContainer"] {
    background: #F4F7FA;
}

[data-testid="stHeader"] {
    background: rgba(244,247,250,0.94);
}

/* Remove sidebar */
[data-testid="stSidebar"] {
    display: none;
}

.block-container {
    max-width: 1450px;
    padding: 1.5rem 2.5rem 1rem 2.5rem;
}

/* Typography */
h1, h2, h3, h4 {
    color: #14243A !important;
    letter-spacing: -0.35px;
}

p, li, label, .stMarkdown {
    color: #243449;
}

[data-testid="stCaptionContainer"] p {
    color: #64748B !important;
}

/* Brand header */
.brand-header {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 8px 0 18px 0;
}

.brand-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 48px;
    height: 48px;
    background: #DDF4EF;
    border: 1px solid #B8E5DC;
    border-radius: 14px;
    font-size: 25px;
}

.brand-name {
    color: #14243A;
    font-size: 25px;
    font-weight: 800;
    line-height: 1.2;
}

.brand-tagline {
    color: #64748B;
    font-size: 11px;
    letter-spacing: 1.5px;
    margin-top: 5px;
}

/* Hero */
.hero {
    background: linear-gradient(120deg, #14243A, #1B4854);
    padding: 36px;
    border-radius: 20px;
    margin: 12px 0 24px 0;
    border: 1px solid #315A69;
}

.hero h1 {
    color: #FFFFFF !important;
    font-size: 38px;
    margin: 0 0 12px 0;
}

.hero p {
    color: #DCEAEF !important;
    font-size: 16px;
    max-width: 820px;
    line-height: 1.8;
}

.hero-tag {
    display: inline-block;
    background: rgba(221,244,239,0.13);
    color: #BDF1E5;
    border: 1px solid rgba(189,241,229,0.3);
    border-radius: 30px;
    padding: 6px 12px;
    font-size: 12px;
    margin-bottom: 15px;
}

/* Top navigation */
div[data-testid="stRadio"] {
    background: #FFFFFF;
    border: 1px solid #DFE7EF;
    border-radius: 14px;
    padding: 10px 14px;
    margin: 8px 0 26px 0;
    box-shadow: 0 3px 12px rgba(20,36,58,0.035);
}

div[data-testid="stRadio"] > label {
    display: none;
}

div[data-testid="stRadio"] div[role="radiogroup"] {
    gap: 8px;
    flex-wrap: wrap;
}

div[data-testid="stRadio"] div[role="radiogroup"] label {
    background: #F4F7FA;
    border: 1px solid transparent;
    border-radius: 9px;
    padding: 8px 14px;
    margin: 0;
}

div[data-testid="stRadio"] div[role="radiogroup"] label p {
    color: #42536A !important;
    font-size: 13px;
    font-weight: 600;
}

div[data-testid="stRadio"] div[role="radiogroup"] label:has(input:checked) {
    background: #DDF4EF;
    border-color: #9BD9CD;
}

div[data-testid="stRadio"] div[role="radiogroup"] label:has(input:checked) p {
    color: #11665F !important;
}

/* Metric cards */
div[data-testid="stMetric"] {
    background: #FFFFFF;
    border: 1px solid #DFE7EF;
    border-radius: 15px;
    padding: 18px 20px;
    box-shadow: 0 3px 12px rgba(20,36,58,0.035);
}

div[data-testid="stMetricLabel"] p {
    color: #64748B !important;
    font-size: 13px;
    font-weight: 600;
}

div[data-testid="stMetricValue"] {
    color: #14243A !important;
    font-weight: 750;
}

/* Buttons */
.stButton > button,
.stDownloadButton > button {
    border-radius: 10px;
    min-height: 42px;
    font-weight: 600;
    border: 1px solid #D3DFE8;
    background: #FFFFFF;
    color: #14243A;
    transition: all 0.2s ease;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    border-color: #0F8278;
    color: #0F8278;
}

/* Primary buttons */
.stButton > button[kind="primary"] {
    background: #0F8278;
    color: #FFFFFF;
    border: 1px solid #0F8278;
}

.stButton > button[kind="primary"]:hover {
    background: #11665F;
    color: #FFFFFF;
}

/* Inputs */
input, textarea {
    border-radius: 9px !important;
}

div[data-baseweb="select"] > div {
    border-radius: 9px;
    border-color: #D3DFE8;
}

/* Tables */
[data-testid="stDataFrame"] {
    background: #FFFFFF;
    border: 1px solid #DFE7EF;
    border-radius: 12px;
    overflow: hidden;
}

/* Expanders */
details {
    background: #FFFFFF;
    border: 1px solid #DFE7EF !important;
    border-radius: 12px !important;
    margin-bottom: 10px;
}

details summary {
    font-weight: 600;
    color: #14243A;
}

/* Alerts */
[data-testid="stAlert"] {
    border-radius: 12px;
}

/* Section divider */
.section-rule {
    height: 1px;
    background: #DFE7EF;
    margin: 25px 0;
}

/* Footer */
.site-footer {
    margin-top: 48px;
    padding: 24px 10px 12px 10px;
    border-top: 1px solid #DFE7EF;
    color: #64748B;
    font-size: 12px;
    line-height: 1.9;
    text-align: center;
}

.site-footer strong {
    color: #14243A;
    font-size: 15px;
}

/* Responsive */
@media (max-width: 768px) {
    .block-container {
        padding: 1rem 1rem 1rem 1rem;
    }
    .hero {
        padding: 23px;
    }
    .hero h1 {
        font-size: 29px;
    }
    .brand-name {
        font-size: 21px;
    }
}

/* ===== Premium Table Styling ===== */

/* Table container */
[data-testid="stDataFrame"],
[data-testid="stTable"] {
    background: #F0F4F8 !important;
    border: 1px solid #D4DFE9 !important;
    border-radius: 12px !important;
    overflow: hidden !important;
}

/* Data grid background and text */
[data-testid="stDataFrame"] canvas {
    background-color: #F0F4F8 !important;
}

/* Table header and grid styling */
[data-testid="stDataFrame"] [role="columnheader"] {
    background-color: #DCE8F1 !important;
    color: #14243A !important;
    font-weight: 700 !important;
    border-bottom: 2px solid #0F8278 !important;
}

/* Table cells */
[data-testid="stDataFrame"] [role="gridcell"] {
    color: #243449 !important;
    border-bottom: 1px solid #DCE5ED !important;
}

/* Standard Streamlit tables */
[data-testid="stTable"] table {
    background-color: #F0F4F8 !important;
    border-collapse: collapse !important;
}

[data-testid="stTable"] thead tr th {
    background-color: #DCE8F1 !important;
    color: #14243A !important;
    font-weight: 700 !important;
    border-bottom: 2px solid #0F8278 !important;
    padding: 12px !important;
}

[data-testid="stTable"] tbody tr td {
    color: #243449 !important;
    border-bottom: 1px solid #DCE5ED !important;
    padding: 10px 12px !important;
}

/* Hover feedback */
[data-testid="stTable"] tbody tr:hover td {
    background-color: #DDF4EF !important;
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# DATA HELPERS
# =========================================================
def normalise_name(value):
    return "".join(ch.lower() for ch in str(value) if ch.isalnum())


def detect_columns(data):
    lookup = {normalise_name(c): c for c in data.columns}

    def exact(*names):
        for name in names:
            key = normalise_name(name)
            if key in lookup:
                return lookup[key]
        return None

    return {
        "year": exact("Year", "Report Year", "Outbreak Year"),
        "month": exact("Month"),
        "state": exact("State", "Reporting State", "State Name"),
        "etiology": exact(
            "Etiology", "Pathogen", "Causative Agent", "Etiologic Agent"
        ),
        "food_vehicle": exact("Food Vehicle", "Food Vehicle Name"),
        "ifsac": exact("IFSAC Category", "IFSAC Food Category"),
        "illnesses": exact(
            "Illnesses", "Number Ill", "Number of Illnesses"
        ),
        "hospitalizations": exact(
            "Hospitalizations", "Number Hospitalized"
        ),
        "deaths": exact("Deaths", "Number of Deaths"),
        "setting": exact("Setting"),
        "mode": exact("Primary Mode"),
    }


def make_demo_data():
    # Illustrative records only. These are not CDC observations.
    return pd.DataFrame({
        "Year": [2020, 2020, 2021, 2021, 2022, 2022, 2023, 2023],
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"],
        "State": ["Demo A", "Demo B", "Demo A", "Demo C",
                  "Demo B", "Demo C", "Demo A", "Demo B"],
        "Etiology": ["Salmonella", "Norovirus", "Norovirus",
                     "Salmonella", "Campylobacter", "Salmonella",
                     "Norovirus", "Campylobacter"],
        "IFSAC Category": ["Poultry", "Leafy vegetables", "Fruits",
                           "Poultry", "Dairy", "Poultry",
                           "Leafy vegetables", "Dairy"],
        "Food Vehicle": ["Illustrative poultry dish", "Illustrative salad",
                         "Illustrative fruit", "Illustrative poultry dish",
                         "Illustrative dairy product",
                         "Illustrative poultry dish", "Illustrative salad",
                         "Illustrative dairy product"],
        "Illnesses": [24, 17, 35, 19, 11, 28, 22, 14],
        "Hospitalizations": [3, 1, 2, 4, 1, 2, 0, 1],
        "Deaths": [0, 0, 0, 0, 0, 0, 0, 0],
        "Setting": ["Restaurant", "Caterer", "Unknown", "Restaurant",
                    "Private home", "Restaurant", "Caterer", "Unknown"],
        "Primary Mode": ["Food"] * 8,
    })


def fmt(value):
    try:
        if pd.isna(value):
            return "N/A"
        return f"{int(value):,}"
    except (ValueError, TypeError, OverflowError):
        return "N/A"


def outcome_sum(data, col):
    if not col or col not in data.columns:
        return None
    return pd.to_numeric(data[col], errors="coerce").sum(min_count=1)


def missingness_table(data):
    result = pd.DataFrame({
        "Column": data.columns,
        "Missing cells": data.isna().sum().values,
        "Missing (%)": (data.isna().mean().values * 100).round(2),
        "Distinct values": [
            data[c].nunique(dropna=True) for c in data.columns
        ],
    })
    return result.sort_values(
        "Missing (%)", ascending=False
    ).reset_index(drop=True)


def top_counts(data, col, n=10):
    if not col or col not in data.columns:
        return pd.DataFrame(columns=["Category", "Records"])

    values = data[col].astype("string")
    values = values.fillna("Not reported")
    values = values.replace(r"^\s*$", "Not reported", regex=True)

    return (
        values.value_counts()
        .head(n)
        .rename_axis("Category")
        .reset_index(name="Records")
    )


def chart_theme(fig):
    fig.update_layout(
        template="plotly_white",
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        font=dict(
            family="Arial, sans-serif",
            color=TEXT,
            size=12,
        ),
        title=dict(
            font=dict(size=17, color=NAVY),
            x=0.02,
            xanchor="left",
        ),
        margin=dict(l=12, r=18, t=65, b=18),
        colorway=PALETTE,
        legend=dict(
            bgcolor="rgba(255,255,255,0)",
            font=dict(color=TEXT),
        ),
        xaxis=dict(
            showgrid=True,
            gridcolor="#E9EEF4",
            zerolinecolor="#DCE5ED",
        ),
        yaxis=dict(
            showgrid=False,
            zerolinecolor="#DCE5ED",
        ),
    )
    return fig


def apply_text_filter(data, col, term):
    if col and term and term.strip():
        mask = data[col].astype("string").str.contains(
            term.strip(), case=False, na=False, regex=False
        )
        return data.loc[mask].copy()
    return data.copy()


def column_picker(label, suggested, key, columns):
    options = ["(Not selected)"] + list(columns)
    expected = suggested if suggested in columns else "(Not selected)"

    if key not in st.session_state:
        st.session_state[key] = expected
    elif st.session_state[key] not in options:
        st.session_state[key] = expected

    selected = st.selectbox(label, options, key=key)
    return None if selected == "(Not selected)" else selected


def reset_dataset_widget_state():
    keys = [
        "map_year", "map_state", "map_etiology", "map_food",
        "map_ifsac", "map_illnesses", "map_hospitalizations",
        "map_deaths", "filter_years", "filter_states",
        "global_search", "etiology_text_filter", "food_text_filter",
        "state_text_filter", "research_question",
    ]
    for key in keys:
        st.session_state.pop(key, None)


def navigate_to(page_name):
    st.session_state.top_navigation = page_name


def render_footer():
    st.markdown("""
    <div class="site-footer">
        <strong>🔬 OutbreakLens AI</strong><br>
        Foodborne Surveillance Explorer<br>
        Data source: CDC National Outbreak Reporting System (NORS)<br>
        Exploratory research prototype · Descriptive analysis only ·
        Not intended for clinical or operational decision-making
    </div>
    """, unsafe_allow_html=True)


def render_brand():
    st.markdown("""
    <div class="brand-header">
        <div class="brand-icon">🔬</div>
        <div>
            <div class="brand-name">OutbreakLens AI</div>
            <div class="brand-tagline">
                FOODBORNЕ SURVEILLANCE EXPLORER
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# ASK RESEARCH AI
# =========================================================
def answer_research_question(question, data):
    q = question.lower().strip()
    columns = detect_columns(data)
    subset = data.copy()

    pathogens = [
        "campylobacter", "salmonella", "norovirus", "listeria",
        "escherichia coli", "e. coli", "shigella", "vibrio",
        "clostridium", "hepatitis a", "cyclospora",
        "cryptosporidium", "yersinia", "bacillus cereus",
        "staphylococcus",
    ]

    pathogen = next((p for p in pathogens if p in q), None)
    pathogen_col = columns["etiology"]

    if pathogen:
        if not pathogen_col:
            st.error("Could not identify the Etiology column.")
            return

        subset = apply_text_filter(subset, pathogen_col, pathogen)

        st.markdown("#### Applied pathogen filter")
        st.write(f"Filtering `{pathogen_col}` for **{pathogen.title()}**.")
        st.metric("Matching records", fmt(len(subset)))

        if subset.empty:
            st.warning(
                f"No records matched '{pathogen}'. Check source values "
                "and spelling."
            )
            return

    year_col = columns["year"]
    year_match = re.search(r"\b(?:19|20)\d{2}\b", q)

    if year_match and year_col:
        target_year = int(year_match.group(0))
        numeric_year = pd.to_numeric(subset[year_col], errors="coerce")
        subset = subset[numeric_year == target_year].copy()

        st.write(f"Additional filter: **Year = {target_year}**")
        st.metric("Records after year filter", fmt(len(subset)))

        if subset.empty:
            st.warning("No records match the selected pathogen and year.")
            return

    asks_year = any(term in q for term in [
        "year", "yearly", "annual", "annually", "trend", "over time",
        "changed by year", "change by year", "highest number of records",
        "most records", "records by year", "by year",
    ])

    asks_setting = any(term in q for term in [
        "setting", "settings", "location type",
        "where did outbreaks occur", "outbreak locations",
    ])

    asks_ifsac = any(term in q for term in [
        "ifsac", "food category", "food categories",
    ])

    asks_vehicle = any(term in q for term in [
        "food vehicle", "food vehicles", "vehicle", "food source",
        "food sources", "food type", "food types", "poultry",
        "chicken", "beef", "seafood", "fish", "meat",
    ])

    asks_food = asks_ifsac or asks_vehicle

    asks_outcome = any(term in q for term in [
        "illness", "illnesses", "hospitalization", "hospitalizations",
        "hospitalized", "death", "deaths", "health outcome",
        "health outcomes",
    ])

    asks_missing = any(term in q for term in [
        "missing", "missingness", "data quality", "incomplete",
        "completeness",
    ])

    asks_state = any(term in q for term in [
        "state", "states", "which state", "by state",
    ])

    # Yearly records
    if asks_year:
        st.markdown("### Outbreak records by year")

        if not year_col:
            st.warning("A Year column was not detected.")
        else:
            year_values = pd.to_numeric(
                subset[year_col], errors="coerce"
            )
            valid_years = year_values.dropna()
            valid_years = valid_years[
                valid_years.between(1900, 2100)
            ]

            yearly = (
                valid_years.astype(int)
                .value_counts()
                .sort_index()
                .rename_axis("Year")
                .reset_index(name="Records")
            )

            if yearly.empty:
                st.info("No usable year values were found.")
            else:
                fig = px.line(
                    yearly,
                    x="Year",
                    y="Records",
                    markers=True,
                    title="Records by reported year",
                    color_discrete_sequence=[TEAL],
                )
                fig.update_traces(line=dict(width=3))
                st.plotly_chart(
                    chart_theme(fig), use_container_width=True
                )

                st.dataframe(
                    yearly, use_container_width=True, hide_index=True
                )

                highest = yearly.sort_values(
                    "Records", ascending=False
                ).head(10)

                st.markdown("**Years with the highest record counts**")
                st.dataframe(
                    highest, use_container_width=True, hide_index=True
                )

                top = highest.iloc[0]
                st.write(
                    f"Highest count in this selected dataset: "
                    f"**{int(top['Year'])}** "
                    f"({int(top['Records']):,} records)."
                )

                st.caption(
                    "Counts represent dataset rows grouped by year, not "
                    "necessarily unique outbreaks or population incidence. "
                    "Reporting practices and dataset coverage may influence "
                    "observed trends."
                )

    # Setting analysis
    if asks_setting:
        setting_col = columns["setting"]
        st.markdown("### Most frequently reported settings")

        if not setting_col:
            st.warning("A Setting column was not detected.")
        else:
            settings = top_counts(subset, setting_col, 10)
            fig = px.bar(
                settings.sort_values("Records"),
                x="Records",
                y="Category",
                orientation="h",
                title="Reported settings",
                labels={"Records": "Records", "Category": "Setting"},
                color_discrete_sequence=[TEAL],
            )
            st.plotly_chart(
                chart_theme(fig), use_container_width=True
            )
            st.dataframe(
                settings.rename(columns={"Category": "Setting"}),
                use_container_width=True,
                hide_index=True,
            )
            st.caption(
                "'Not reported' means the field was blank or whitespace. "
                "Counts refer to rows in the selected subset."
            )

    # Food analysis
    if asks_food:
        if asks_ifsac:
            food_col = columns["ifsac"] or columns["food_vehicle"]
        else:
            food_col = columns["food_vehicle"] or columns["ifsac"]

        st.markdown("### Food-related record summaries")

        if not food_col:
            st.warning(
                "Neither Food Vehicle nor IFSAC Category was detected."
            )
        else:
            counts = top_counts(subset, food_col, 10)
            fig = px.bar(
                counts.sort_values("Records"),
                x="Records",
                y="Category",
                orientation="h",
                title=f"Most frequent values in {food_col}",
                labels={"Records": "Records", "Category": food_col},
                color_discrete_sequence=[TEAL],
            )
            st.plotly_chart(
                chart_theme(fig), use_container_width=True
            )
            st.dataframe(
                counts, use_container_width=True, hide_index=True
            )

            st.caption(
                f"Counts use the {len(subset):,} records in the selected "
                "subset. Frequency does not by itself establish that a food "
                "caused an outbreak."
            )

    # Health outcomes
    if asks_outcome:
        st.markdown("### Reported health outcomes")
        rows = []

        for label, key in [
            ("Illnesses", "illnesses"),
            ("Hospitalizations", "hospitalizations"),
            ("Deaths", "deaths"),
        ]:
            col = columns[key]
            if col:
                total = outcome_sum(subset, col)
                rows.append({
                    "Outcome": label,
                    "Source column": col,
                    "Sum of reported values": (
                        int(total) if pd.notna(total) else None
                    ),
                })

        if rows:
            st.dataframe(
                pd.DataFrame(rows),
                use_container_width=True,
                hide_index=True,
            )
            st.caption(
                "These are sums of reported values, not deduplicated "
                "patient counts."
            )
        else:
            st.warning("No health outcome columns were detected.")

    # State analysis
    if asks_state:
        state_col = columns["state"]
        st.markdown("### Records by state")

        if not state_col:
            st.warning("A State column was not detected.")
        else:
            state_counts = top_counts(subset, state_col, 10)
            st.dataframe(
                state_counts.rename(columns={"Category": "State"}),
                use_container_width=True,
                hide_index=True,
            )

    # Missingness
    if asks_missing:
        st.markdown("### Data completeness")
        st.metric(
            "Missing cells in selected rows",
            fmt(subset.isna().sum().sum()),
        )
        st.dataframe(
            missingness_table(subset).head(15),
            use_container_width=True,
            hide_index=True,
        )

    if not any([
        asks_year, asks_setting, asks_food, asks_outcome,
        asks_missing, asks_state,
    ]):
        st.info(
            "Try asking about yearly trends, outbreak settings, food "
            "vehicles, IFSAC categories, health outcomes, states, "
            "or missing data."
        )

    st.info(
        "This is rule-based descriptive analysis, not a generative AI "
        "system or trained prediction model. Findings do not establish "
        "causation."
    )


# =========================================================
# SESSION STATE
# =========================================================
if "data" not in st.session_state:
    st.session_state.data = make_demo_data()
    st.session_state.is_demo = True
    st.session_state.source_name = "Illustrative demo data"
    st.session_state.loaded_file_signature = None

pages = [
    "Home",
    "Outbreak Explorer",
    "Ask Research AI",
    "Research Insights",
    "About & Methodology",
]

if "top_navigation" not in st.session_state:
    st.session_state.top_navigation = "Home"

if st.session_state.top_navigation not in pages:
    st.session_state.top_navigation = "Home"

# =========================================================
# WEBSITE HEADER + TOP NAVIGATION
# =========================================================
render_brand()

page = st.radio(
    "Main navigation",
    pages,
    horizontal=True,
    key="top_navigation",
    label_visibility="collapsed",
)

df = st.session_state.data.copy()

# =========================================================
# HOME
# =========================================================
if page == "Home":
    st.markdown("""
    <div class="hero">
        <span class="hero-tag">EXPLORATORY RESEARCH PROTOTYPE</span>
        <h1>Understand foodborne surveillance data.</h1>
        <p>
            Explore reported outbreak records, compare descriptive patterns,
            examine data completeness, and create transparent summaries
            using the CDC National Outbreak Reporting System dataset.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.is_demo:
        st.info(
            "You are viewing illustrative demo data. Upload the CDC NORS "
            "CSV in Outbreak Explorer to analyze real source records."
        )
    else:
        st.success(
            f"Dataset loaded: {st.session_state.source_name}"
        )

    c1, c2, c3 = st.columns(3)
    c1.metric("Records", fmt(len(df)))
    c2.metric("Source columns", fmt(len(df.columns)))
    c3.metric("Missing cells", fmt(df.isna().sum().sum()))

    st.markdown("## Explore the platform")
    st.caption(
        "Choose a workspace below to start exploring the loaded dataset."
    )

    a, b = st.columns(2)
    with a:
        st.markdown("### 🔎 Outbreak Explorer")
        st.write(
            "Upload your CSV, inspect records, apply filters, review "
            "outcomes, and download a filtered dataset."
        )
        st.button(
            "Open Explorer →",
            key="home_explorer",
            type="primary",
            use_container_width=True,
            on_click=navigate_to,
            args=("Outbreak Explorer",),
        )

    with b:
        st.markdown("### 📊 Research Insights")
        st.write(
            "Review yearly record counts, reported etiologies, food "
            "categories, and patterns of missing data."
        )
        st.button(
            "View Insights →",
            key="home_insights",
            use_container_width=True,
            on_click=navigate_to,
            args=("Research Insights",),
        )

    st.markdown('<div class="section-rule"></div>',
                unsafe_allow_html=True)

    st.markdown("## Dataset preview")
    st.caption(
        "A preview of the first ten rows currently loaded into the app."
    )
    st.dataframe(
        df.head(10), use_container_width=True, hide_index=True
    )

    st.markdown("## Research scope")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("**01 · Explore**")
        st.write("Filter reported records by available source fields.")
    with c2:
        st.markdown("**02 · Summarize**")
        st.write("Compare descriptive counts and reported outcomes.")
    with c3:
        st.markdown("**03 · Assess**")
        st.write("Inspect missing values and limitations in the data.")

    st.caption(
        "Outbreak row counts are not necessarily unique outbreak counts. "
        "Outcome totals are sums of reported values."
    )


# =========================================================
# OUTBREAK EXPLORER
# =========================================================
elif page == "Outbreak Explorer":
    st.title("Outbreak Explorer")
    st.write(
        "Upload, search, filter, and inspect the dataset. "
        "All summaries update using the selected records."
    )

    uploaded = st.file_uploader(
        "Upload the CDC NORS CSV",
        type=["csv"],
        help="Upload a CSV downloaded from the CDC NORS data portal.",
        key="nors_uploader",
    )

    if uploaded is not None:
        signature = (uploaded.name, uploaded.size)

        if st.session_state.loaded_file_signature != signature:
            try:
                uploaded_df = pd.read_csv(
                    uploaded, low_memory=False
                )

                if uploaded_df.empty:
                    st.error("The uploaded CSV has no data rows.")
                else:
                    st.session_state.data = uploaded_df
                    st.session_state.is_demo = False
                    st.session_state.source_name = uploaded.name
                    st.session_state.loaded_file_signature = signature
                    reset_dataset_widget_state()
                    st.rerun()

            except Exception as exc:
                st.error(f"Could not read this CSV: {exc}")

    df = st.session_state.data.copy()
    mapping = detect_columns(df)

    if st.session_state.is_demo:
        st.warning(
            "Illustrative demo data is active. Upload the source CSV "
            "before drawing conclusions about CDC records."
        )
    else:
        st.success(
            f"Loaded {len(df):,} rows and {len(df.columns):,} columns "
            f"from {st.session_state.source_name}."
        )

    st.markdown("### Dataset overview")
    c1, c2, c3 = st.columns(3)
    c1.metric("Rows", fmt(len(df)))
    c2.metric("Columns", fmt(len(df.columns)))
    c3.metric("Missing cells", fmt(df.isna().sum().sum()))

    with st.expander("View source column names"):
        st.write(list(df.columns))

    with st.expander("Review column mappings", expanded=False):
        st.caption(
            "Mappings use exact column names. Confirm field definitions "
            "before interpreting results."
        )
        m1, m2 = st.columns(2)

        with m1:
            year_col = column_picker(
                "Year", mapping["year"], "map_year", df.columns
            )
            etiology_col = column_picker(
                "Etiology / pathogen",
                mapping["etiology"], "map_etiology", df.columns
            )
            food_col = column_picker(
                "Food vehicle",
                mapping["food_vehicle"], "map_food", df.columns
            )
            ifsac_col = column_picker(
                "IFSAC food category",
                mapping["ifsac"], "map_ifsac", df.columns
            )

        with m2:
            state_col = column_picker(
                "State", mapping["state"], "map_state", df.columns
            )
            illness_col = column_picker(
                "Illnesses",
                mapping["illnesses"], "map_illnesses", df.columns
            )
            hospital_col = column_picker(
                "Hospitalizations",
                mapping["hospitalizations"],
                "map_hospitalizations", df.columns
            )
            deaths_col = column_picker(
                "Deaths", mapping["deaths"], "map_deaths", df.columns
            )

    # Default column mappings are still available when mapping panel is closed.
    year_col = st.session_state.get("map_year", mapping["year"])
    state_col = st.session_state.get("map_state", mapping["state"])
    etiology_col = st.session_state.get(
        "map_etiology", mapping["etiology"]
    )
    food_col = st.session_state.get("map_food", mapping["food_vehicle"])
    ifsac_col = st.session_state.get("map_ifsac", mapping["ifsac"])
    illness_col = st.session_state.get(
        "map_illnesses", mapping["illnesses"]
    )
    hospital_col = st.session_state.get(
        "map_hospitalizations", mapping["hospitalizations"]
    )
    deaths_col = st.session_state.get("map_deaths", mapping["deaths"])

    def valid_col(value):
        return value if value in df.columns else None

    year_col = valid_col(year_col)
    state_col = valid_col(state_col)
    etiology_col = valid_col(etiology_col)
    food_col = valid_col(food_col)
    ifsac_col = valid_col(ifsac_col)
    illness_col = valid_col(illness_col)
    hospital_col = valid_col(hospital_col)
    deaths_col = valid_col(deaths_col)

    st.markdown("### Search and filters")

    with st.container(border=True):
        search_term = st.text_input(
            "Search across all columns",
            placeholder="Enter a word or phrase...",
            key="global_search",
        )

        f1, f2 = st.columns(2)

        with f1:
            selected_years = []
            if year_col:
                years = sorted(
                    df[year_col].dropna().astype(str).unique().tolist()
                )
                selected_years = st.multiselect(
                    "Reported year",
                    options=years,
                    default=[],
                    key="filter_years",
                )

        with f2:
            selected_states = []
            if state_col:
                states = sorted(
                    df[state_col].dropna().astype(str).unique().tolist()
                )
                if len(states) <= 100:
                    selected_states = st.multiselect(
                        "State",
                        options=states,
                        default=[],
                        key="filter_states",
                    )

        f3, f4 = st.columns(2)

        with f3:
            etiology_search = ""
            if etiology_col:
                etiology_search = st.text_input(
                    "Etiology / pathogen",
                    placeholder="e.g., Salmonella",
                    key="etiology_text_filter",
                )

        with f4:
            food_search = ""
            selected_food_col = ifsac_col or food_col
            if selected_food_col:
                food_search = st.text_input(
                    "Food category / vehicle",
                    placeholder="e.g., poultry",
                    key="food_text_filter",
                )

        state_search = ""
        if state_col and len(df[state_col].dropna().unique()) > 100:
            state_search = st.text_input(
                "Search state", key="state_text_filter"
            )

    filtered = df.copy()

    if selected_years and year_col:
        filtered = filtered[
            filtered[year_col].astype(str).isin(selected_years)
        ]

    if selected_states and state_col:
        filtered = filtered[
            filtered[state_col].astype(str).isin(selected_states)
        ]

    if state_search and state_col:
        filtered = apply_text_filter(
            filtered, state_col, state_search
        )

    if etiology_search and etiology_col:
        filtered = apply_text_filter(
            filtered, etiology_col, etiology_search
        )

    if food_search and selected_food_col:
        filtered = apply_text_filter(
            filtered, selected_food_col, food_search
        )

    if search_term.strip():
        term = search_term.strip()
        mask = filtered.astype(str).apply(
            lambda col: col.str.contains(
                term, case=False, na=False, regex=False
            )
        ).any(axis=1)
        filtered = filtered.loc[mask]

    st.markdown("### Filtered results")
    c1, c2, c3 = st.columns(3)
    c1.metric("Rows shown", fmt(len(filtered)))
    c2.metric("Columns", fmt(len(filtered.columns)))
    c3.metric("Missing cells", fmt(filtered.isna().sum().sum()))

    if filtered.empty:
        st.info(
            "No records match these filters. Clear one or more filters "
            "and try again."
        )
    else:
        st.dataframe(
            filtered.head(500),
            use_container_width=True,
            hide_index=True,
        )

        if len(filtered) > 500:
            st.caption(
                "Showing the first 500 matching records. Download the CSV "
                "to access all matching records."
            )

        st.download_button(
            "Download filtered records as CSV",
            data=filtered.to_csv(index=False).encode("utf-8"),
            file_name="outbreaklens_filtered_records.csv",
            mime="text/csv",
        )

    st.markdown("### Reported health outcomes")
    outcome_columns = st.columns(3)

    for container, label, col in zip(
        outcome_columns,
        ["Sum of illnesses", "Sum of hospitalizations", "Sum of deaths"],
        [illness_col, hospital_col, deaths_col],
    ):
        value = outcome_sum(filtered, col)
        container.metric(
            label, fmt(value) if value is not None else "Not mapped"
        )

    st.caption(
        "Outcome totals are sums of reported values, not deduplicated "
        "patient counts."
    )

    st.markdown("### Frequently reported food categories or vehicles")
    selected_food_col = ifsac_col or food_col

    if selected_food_col:
        food_counts = top_counts(filtered, selected_food_col, 15)

        if not food_counts.empty:
            fig = px.bar(
                food_counts.sort_values("Records"),
                x="Records",
                y="Category",
                orientation="h",
                title=f"Most frequent values in {selected_food_col}",
                labels={
                    "Records": "Number of records",
                    "Category": selected_food_col,
                },
                color_discrete_sequence=[TEAL],
            )
            st.plotly_chart(
                chart_theme(fig), use_container_width=True
            )
            st.dataframe(
                food_counts, use_container_width=True, hide_index=True
            )
    else:
        st.info("Map a food vehicle or IFSAC category column.")

    st.markdown("### Column-level data quality")
    st.dataframe(
        missingness_table(filtered),
        use_container_width=True,
        hide_index=True,
    )


# =========================================================
# ASK RESEARCH AI
# =========================================================
elif page == "Ask Research AI":
    st.title("Ask Research AI")
    st.write(
        "Ask a question about the loaded dataset. The current question "
        "router produces descriptive summaries using predefined rules."
    )

    st.info(
        "This is not a general-purpose language model, and it does not "
        "train a prediction model."
    )

    with st.container(border=True):
        question = st.text_input(
            "What would you like to explore?",
            placeholder=(
                "Among Salmonella records, which IFSAC food categories "
                "are most frequent?"
            ),
            key="research_question",
        )

        st.caption("Example questions")
        st.markdown("""
- How have reported outbreak records changed by year?
- Among Norovirus outbreaks, which settings are most frequent?
- Among Salmonella outbreaks, which food vehicles are most frequent?
- Which IFSAC food categories are most frequent?
- What are the reported illnesses, hospitalizations, and deaths?
- Which columns have the most missing data?
""")

        analyze = st.button(
            "Analyze question",
            type="primary",
            use_container_width=True,
        )

    if analyze:
        if not question.strip():
            st.warning("Please enter a question.")
        else:
            st.markdown('<div class="section-rule"></div>',
                        unsafe_allow_html=True)
            st.markdown("## Exploratory answer")
            answer_research_question(
                question, st.session_state.data.copy()
            )


# =========================================================
# RESEARCH INSIGHTS
# =========================================================
elif page == "Research Insights":
    st.title("Research Insights")
    st.write(
        "Descriptive overview of the currently loaded dataset. "
        "Patterns should be interpreted in the context of reporting "
        "coverage and data quality."
    )

    data = st.session_state.data.copy()
    m = detect_columns(data)

    c1, c2, c3 = st.columns(3)
    c1.metric("Records", fmt(len(data)))
    c2.metric("Columns", fmt(len(data.columns)))
    c3.metric("Exact duplicate rows", fmt(data.duplicated().sum()))

    if st.session_state.is_demo:
        st.info(
            "These insights currently use illustrative demo records, "
            "not CDC observations."
        )

    year_col = m["year"]
    etiology_col = m["etiology"]
    food_col = m["ifsac"] or m["food_vehicle"]

    if year_col:
        years = pd.to_numeric(data[year_col], errors="coerce")
        valid_years = years.dropna()
        valid_years = valid_years[
            valid_years.between(1900, 2100)
        ]

        year_counts = (
            valid_years.astype(int)
            .value_counts()
            .sort_index()
            .rename_axis("Year")
            .reset_index(name="Records")
        )

        if not year_counts.empty:
            fig = px.line(
                year_counts,
                x="Year",
                y="Records",
                markers=True,
                title="Surveillance records by reported year",
                color_discrete_sequence=[TEAL],
            )
            fig.update_traces(line=dict(width=3))
            st.plotly_chart(
                chart_theme(fig), use_container_width=True
            )
            st.dataframe(
                year_counts, use_container_width=True, hide_index=True
            )

            highest = year_counts.sort_values(
                "Records", ascending=False
            ).head(5)
            st.markdown("### Years with highest record counts")
            st.dataframe(
                highest, use_container_width=True, hide_index=True
            )

    left, right = st.columns(2)

    with left:
        if etiology_col:
            counts = top_counts(data, etiology_col, 12)
            fig = px.bar(
                counts.sort_values("Records"),
                x="Records",
                y="Category",
                orientation="h",
                title="Most frequent reported etiologies",
                color_discrete_sequence=[TEAL],
            )
            st.plotly_chart(
                chart_theme(fig), use_container_width=True
            )
            st.dataframe(
                counts, use_container_width=True, hide_index=True
            )
        else:
            st.info("No etiology column was detected.")

    with right:
        if food_col:
            counts = top_counts(data, food_col, 12)
            fig = px.bar(
                counts.sort_values("Records"),
                x="Records",
                y="Category",
                orientation="h",
                title=f"Most frequent values: {food_col}",
                color_discrete_sequence=["#4776A8"],
            )
            st.plotly_chart(
                chart_theme(fig), use_container_width=True
            )
            st.dataframe(
                counts, use_container_width=True, hide_index=True
            )
        else:
            st.info("No food-related column was detected.")

    st.markdown("### Data completeness")
    quality = missingness_table(data)

    fig = px.bar(
        quality.head(15).sort_values("Missing (%)"),
        x="Missing (%)",
        y="Column",
        orientation="h",
        title="Columns with the highest percentage of missing values",
        color_discrete_sequence=["#D99A36"],
    )
    st.plotly_chart(
        chart_theme(fig), use_container_width=True
    )
    st.dataframe(
        quality, use_container_width=True, hide_index=True
    )

    st.warning(
        "Record frequency can be influenced by reporting practices, "
        "missingness, field definitions, and dataset scope. Exact duplicate "
        "rows should be investigated before removal. These charts do not "
        "establish causation or population-level incidence."
    )


# =========================================================
# ABOUT & METHODOLOGY
# =========================================================
elif page == "About & Methodology":
    st.title("About & Methodology")
    st.write(
        "How OutbreakLens AI works, what it currently supports, "
        "and what its results can and cannot establish."
    )

    st.markdown("## About the project")
    st.markdown("""
OutbreakLens AI is an exploratory research prototype for examining
foodborne outbreak surveillance records. It provides transparent
descriptive summaries, filtering, visualizations, and data-quality checks.
""")

    st.markdown("## Current capabilities")
    st.markdown("""
- Upload and inspect a CSV file.
- Search across records and filter available fields.
- Review missing values and exact duplicate rows.
- Summarize records by year, etiology, food category, vehicle, setting,
  and state.
- Calculate sums of reported illnesses, hospitalizations, and deaths.
- Export filtered records for additional analysis.
- Apply pathogen filters before calculating question-based summaries.
""")

    st.markdown("## Methodology")
    st.markdown("""
1. **Load:** read the uploaded CSV into a pandas DataFrame.
2. **Map:** identify relevant columns using normalized column names;
   users can review mappings in the Explorer.
3. **Filter:** apply the user's selected criteria.
4. **Summarize:** count rows, calculate sums of reported outcome values,
   and tabulate missingness.
5. **Visualize:** use charts to display descriptive distributions.
6. **Interpret:** consider source definitions, reporting coverage,
   missingness, and possible duplicate records before drawing conclusions.
""")

    st.markdown("## Important limitations")
    st.markdown("""
- Demo records are illustrative and are not CDC observations.
- The current question router uses predefined rules; it is not a
  general-purpose generative AI system.
- No trained prediction model is used.
- Dataset rows are not necessarily unique outbreaks or unique patients.
- Outcome sums are sums of reported values and may not represent
  deduplicated counts.
- A reported food vehicle does not, by itself, prove causation.
- Blank fields may indicate unreported information; they do not establish
  why the information is missing.
- Exact duplicate rows are flagged for review, not automatically deleted.
- Record trends may reflect reporting practices and dataset coverage,
  not just changes in outbreak occurrence.
""")

    st.markdown("## Data source")
    st.markdown(
        "CDC National Outbreak Reporting System (NORS): "
        "[Open the official data portal](https://data.cdc.gov/d/5xkq-dg7x)"
    )

    st.markdown("## Future research directions")
    st.markdown("""
- Systematic missing-data and data-quality assessment.
- Clearer analysis of reporting periods and source field definitions.
- Comparison of outbreak attributes across reporting periods.
- Transparent feature engineering and baseline model evaluation.
- Validation against an independently defined reference dataset.
""")

    st.info(
        "Research prototype only. Results should not be used for clinical "
        "or operational decision-making."
    )


# =========================================================
# FOOTER
# =========================================================
render_footer()
