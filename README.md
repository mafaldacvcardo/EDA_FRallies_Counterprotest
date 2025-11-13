# EXPLORATORY DATA ANALYSIS

# **FARPE DATA ANALYSIS: FAR RIGHT RALLIES AND COUNTERPROTEST AS RESISTANCE: CLAIMING THE STREET**

Analysis of far-right mobilization patterns across Europe using the **FARPE (Far-Right Protests in Europe)** dataset.

## **Overview**

This repository contains a Python-based analysis exploring **six key hypotheses** about far-right protest mobilization in Europe.
The project investigates:

* Counter-mobilization dynamics
* Protest characteristics
* Geographical concentration
* Temporal shifts in issue salience
* Relationships between protest forms, violence, and counter-protest

## **Dataset**

* **File:** `data/FARPE-data_1.3.csv`
* **Encoding:** `Latin-1`

The dataset includes information on far-right protest events such as:

* Issues and grievances
* Location and country
* Counter-mobilization characteristics
* Protest form (march, rally, sit-in, violent action, etc.)
* Event level (local, national, supranational)
* Dates and temporal indicators

**Citation:**
Castelli Gattinara Pietro, Froio Caterina, & Pirro Andrea (2022).
*Far-right protest mobilisation in Europe: Grievances, opportunities and resources.*
**European Journal of Political Research, 61(4), 1019–1041.**
[https://doi.org/10.1111/1475-6765.12484](https://doi.org/10.1111/1475-6765.12484)


## **Dependencies**

Required packages:

```
python
pandas
numpy
matplotlib
seaborn
```

Install via pip:

pip install pandas numpy matplotlib seaborn

## **Analysis Structure**

### **1. Data Preparation**

* Loads the FARPE dataset
* Cleans key string columns:

  * Counter-mobilization
  * Issues
  * Event level
  * Protest form
* Removes rows with missing essential variables


### **2. Hypothesis 1 — Counter-Mobilization by Issue**

**Question:** *Which protest issues attract the most counter-mobilization?*

* Computes counter-mobilization rates by issue
* Filters out issue categories with fewer than 30 events
* Produces a bar plot showing counter-mobilization proportions


### **3. Hypothesis 2 — Verbal Counter-Mobilization by Event Level**

**Question:** *Does counter-mobilization type vary by event scale?*

* Categorizes events into:
  **Local**, **National**, **Supranational**
* Examines rates of *verbal* counter-mobilization
* Displays results using a pie chart

### **4. Hypothesis 3 — Violence and Counter-Mobilization**

**Question:** *Is protest violence associated with counter-mobilization patterns?*

* Detects violent events using keyword matching in protest forms
* Compares violence rates between:

  * Contentious counter-mobilization
  * No counter-mobilization
* Visualizes results with a bar plot

### **5. Hypothesis 4 — Identity-Related Issues Over Time**

**Question:** *Have Islam/Immigration/Identity issues increased since 2014?*

* Tracks issue salience over time
* Compares pre-2014 vs. post-2014 periods
* Uses a stacked bar chart to show temporal shifts

### **6. Hypothesis 5 — Geographic Distribution**

**Question:** *Which countries have the most far-right mobilizations?*

* Counts events by country
* Identifies the **top 10 countries**
* Calculates concentration share of the top 5
  (e.g., percentage of all protests occurring in these countries)

### **7. Hypothesis 6 — Welfare/Economic Issues Over Time**

**Question:** *How has the emphasis on welfare/economic issues evolved?*

* Tracks welfare/economic issue mentions by year
* Highlights the **2012–2014 crisis period**
* Identifies peak mobilization year for welfare-related protests

## **Running the Analysis**

1. Ensure the dataset is located at:
   `data/FARPE-data_1.3.csv`
2. Run the script:

```bash
python analysis_script.py
```

The script will automatically generate:

* Statistical summaries (printed to console)
* Visualizations (bar charts, pie chart, stacked bars, line trends)

## **Output**

The analysis produces:

* Statistical tables
* Multiple visualizations
* Key findings for each hypothesis
* Highlights on temporal, spatial, and issue-based trends

## **Notes**

* A minimum threshold of **30 events** is used for reliable issue-level comparisons
* Event level categories are normalized for consistency
* Violence detection is based on keyword matching
* All visualizations use **seaborn’s `whitegrid` style**

