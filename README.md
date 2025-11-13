# EXPLORATORY DATA ANALYSIS

FARPE Data Analysis
This repository contains a Python script for analyzing far-right mobilization data from the FARPE (Far-Right Protests in Europe) dataset.

Overview
The analysis explores six key hypotheses about far-right mobilizations across Europe, examining patterns in counter-mobilization, protest characteristics, geographic distribution, and temporal trends.

Dataset
File: data/FARPE-data_1.3.csv
Encoding: Latin-1

The dataset includes information on far-right protest events, including issues, locations, counter-mobilization, protest forms, and temporal data.

Dependencies
python
pandas
numpy
matplotlib
seaborn

Install dependencies using:
pip install pandas numpy matplotlib seaborn

Analysis Structure
Data Preparation
Loads the FARPE dataset
Cleans string columns (counter-mobilization, issues, event level, protest form)
Removes rows with missing key data
Hypothesis 1: Counter-Mobilization by Issue
Question: Which protest issues attract the most counter-mobilization?

Analyses counter-mobilization rates across different protest issues
Filters for issues with at least 30 events
Visualizes proportion of events with counter-mobilization by issue type
Hypothesis 2: Verbal Counter-Mobilization by Event Level
Question: Does the type of counter-mobilization vary by event scale?

Categorizes events into Local, National, and Supranational levels
Examines the proportion of verbal counter-mobilization at each level
Presents results in a pie chart visualization
Hypothesis 3: Violence and Counter-Mobilization Type
Question: Is protest violence related to counter-mobilization presence?

Identifies violent protest forms using keyword detection
Compares violence rates between contentious counter-mobilization and no counter-mobilization
Uses bar plot to show the relationship
Hypothesis 4: Identity-Related Issues Over Time
Question: Have Islam/Immigration/Identity issues become more prominent since 2014?

Tracks mentions of Islam, Immigration, and Identity issues
Compares periods before and after 2014
Displays temporal shift using a stacked bar chart
Hypothesis 5: Geographic Distribution
Question: Which countries have the most far-right mobilizations?

Counts events by country
Identifies top 10 countries with most mobilizations
Calculates concentration (top 5 countries' share)
Hypothesis 6: Welfare/Economic Issues Temporal Trend
Question: How has focus on welfare/economic issues changed over time?

Tracks welfare and economic-related issues by year
Highlights the 2012-2014 crisis period
Identifies peak year for welfare-related mobilizations
Running the Analysis
Ensure the dataset is located at data/FARPE-data_1.3.csv

Run the script:
   python analysis_script.py

The script will generate multiple visualizations and print statistical summaries
Output
The analysis produces:

Statistical tables 
Multiple visualizations (bar plots, pie chart, line plot, stacked bar chart)
Key findings for each hypothesis

Notes
The script uses a minimum threshold of 30 events for certain analyses to ensure statistical reliability
Event levels are normalized into simplified categories for clearer analysis
Violence detection uses keyword matching on protest form descriptions
All visualizations use seaborn's whitegrid style for consistency

Citation
Castelli Gattinara Pietro, Froio Caterina, et Pirro Andrea. (2022) Far‐right protest mobilisation in Europe: Grievances, opportunities and resources. European Journal of Political Research, 61(4), 1019-1041. https://doi.org/10.1111/1475-6765.12484.
