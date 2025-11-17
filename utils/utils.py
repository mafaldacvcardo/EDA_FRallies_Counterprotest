# Import the needed libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the default characteristics of the canvases for the graphics
sns.set(style="whitegrid")

# Set the default dimensions of the figures
plt.rcParams['figure.figsize'] = (8,5)

# Load the dataset, being able to read special characters and the whole dataset
df = pd.read_csv('data/FARPE-data_1.3.csv', encoding='latin-1', low_memory=False)
print("Dataset loaded successfully! Shape:", df.shape)
df.head()

# Define a function to clean the columns of the dataframe
def clean_col(s):
    return s.astype(str).str.strip(" '\"").replace({'nan': np.nan, 'None': np.nan})

#Apply the created function to clean some columns and rename them
df['countermob'] = clean_col(df['Countermob_string'])
df['issue1'] = clean_col(df['Issue1_string'])
df['event_level'] = clean_col(df['Event_lev_string'])
df['protform'] = clean_col(df['Protform_string'])

print("Cleaned columns created successfully!")
df[['countermob','issue1','event_level','protform']].head()

# Create a new dataframe with the clean columns. Delete rows that don't have data in any of the mentioned columns
df_clean = df[df['countermob'].notna() | df['issue1'].notna() | df['event_level'].notna() | df['protform'].notna()].copy()
print("Rows before:", len(df), "Rows after cleaning:", len(df_clean))

#Hypothesis 1
# Create a new dataframe with two columns. Delete the rows that don't have data in the event_level column
df_h1 = df_clean[['event_level','countermob']].copy().dropna(subset=['event_level'])
# Create a list with the keywords
levels = ['local', 'national', 'supranational']
# Create empty lists for total mobilizations and total verbal counter-mobilizations
total_mobs = []
total_verbal = []
# Count the amount of mobilizations by geographical level
for level in levels:
    mobs = df_h1['event_level'].str.lower().str.contains(level)
    total_mobs.append(mobs.sum())

# Count the amount of verbal counter-mobilizations by geographical level
for level in levels:
    counter_verbal = (df_h1['event_level'].str.lower().str.contains(level)) & (df_h1['countermob'].str.lower() == "verbal")
    total_verbal.append(counter_verbal.sum())

# Calculate the percentage of verbal counter-mobilizations by geographical level    
percent_verbal = [total_verbal[i]*100 / total_mobs[i] for i in range(len(levels))]
# Create an empty dataframe for plotting
plot_df_h1 = pd.DataFrame()
# Add columns to the empty dataframe
plot_df_h1['event_level'] = levels
plot_df_h1['percent_verbal'] = percent_verbal
print("Percentage of verbal counter-mobilization by event level")
print(plot_df_h1)

# Create a bar chart with the information from plot_df_h1
plt.figure()
sns.barplot(x=plot_df_h1['event_level'], y=plot_df_h1['percent_verbal'])
plt.xlabel('Geographical level of mobilizations')
plt.ylabel('Percentage of verbal countermobilizations')
plt.title('Verbal counter-mobilization by event level')
plt.tight_layout()
plt.show()

#Hypothesis 2
#Create a new dataframe with these four columns' copy
df_h2 = df[['Year', 'Issue1_string', 'Issue2_string', 'Issue3_string']].copy()
# Delete the rows without any data in Year column
df_h2 = df_h2.dropna(subset=['Year'])
# Delete the rows if all these three columns are empty
df_h4 = df_h2.dropna(subset=['Issue1_string', 'Issue2_string', 'Issue3_string'], how='all')

# Used to check the list of topics in the three columns, to know which keywords to use
#print(df_h2['Issue1_string'].value_counts())
#print(df_h2['Issue2_string'].value_counts())
#print(df_h2['Issue3_string'].value_counts())

# Create a list with the keywords related to identity-theme
identity_keywords = ['immigration and multiculturalism', 'national identity and culture', 'islam']
# Create a column with True/False values (depending on whether the keyword appears in any of the three columns or not)
for key in identity_keywords:
    df_h2[key] = (df_h2['Issue1_string'].str.lower().str.contains(key)) | (df_h2['Issue2_string'].str.lower().str.contains(key)) | (df_h2['Issue3_string'].str.lower().str.contains(key))
# Create a column with False value by default
df_h2['identity_issues'] = False
# Update the identity_issues column by setting it to True if any identity-theme keyword is present in any of the three Issue columns.
for key in identity_keywords:
    df_h2['identity_issues'] = df_h2['identity_issues'] | df_h2[key]
# Count the amount of total mobilizations by year
total_mob_year = df_h2.groupby('Year')['Year'].count()
# Count the amount of total identity-theme mobilizations by year
total_identity_theme_year = df_h2.groupby('Year')['identity_issues'].sum()
# Calculate the percentage of identity-theme mobilizations by year
percentage_identity_theme_year = (total_identity_theme_year / total_mob_year)*100
print("Share of Identity-theme-Related Mobilizations by year")
print(percentage_identity_theme_year)
print("Peak percentage of Identity-theme-Related Mobilizations")
print(percentage_identity_theme_year.max())
print("Lowest percentage of Identity-theme-Related Mobilizations")
print(percentage_identity_theme_year.min())


# Create a line chart with the years in x axis and percentage of identity-theme mobilizations in y axis
plt.figure()
sns.lineplot(x=percentage_identity_theme_year.index, y=percentage_identity_theme_year, marker='o')
plt.title('Share of Identity-theme-Related Mobilizations Over Time')
plt.ylabel('Percentage of Events (%)')
plt.xlabel('Year')
# Plot a vertical line in 2014
plt.axvline(x=2014)
plt.show()

#Hypothesis 3
# Create a dataframe with a copy of the Country_string column. Delete the rows without data in that column
df_h3 = df[['Country_string']].copy().dropna()
# Count the amount of mobilizations by country
country_counts = df_h3['Country_string'].value_counts()
# Create a dataframe for plotting. Create a Country_counts column in this new dataframe with the values of country_counts
plot_df_h3 = pd.DataFrame()
plot_df_h3['Country_counts'] = country_counts
print("Amount of Far-Right Mobilizations per Country between 2008-2018")
print(plot_df_h3['Country_counts'])
# Increasing the figure size to reduce overlaps
plt.figure(figsize=(8, 8))
# Create a pie chart with the newly created dataset's column's data and format the percentage's visualization (one decimal and % symbol)
plt.pie(plot_df_h3['Country_counts'],      
    labels=plot_df_h3.index, 
    autopct='%1.1f%%',                   
    startangle=90,
    pctdistance=0.75,    # moving the percentage labels farther from the center
    labeldistance=1.1 # moving the slice labels outward
)
plt.title('Percentage of Far-Right Mobilizations per Country')
# A pie with the same width and height
plt.axis('equal')
plt.tight_layout()
plt.show()

#Hypothesis 4
# Create a new dataframe with these four columns' copy
df_h4 = df[['Year', 'Issue1_string', 'Issue2_string', 'Issue3_string']].copy()
# Delete the rows without any data in Year column
df_h4 = df_h4.dropna(subset=['Year'])
# Delete the rows if all these three columns are empty
df_h4 = df_h4.dropna(subset=['Issue1_string', 'Issue2_string', 'Issue3_string'], how='all')

# Used to check the list of topics in the three columns, to know which keywords to use
#print(df_h4['Issue1_string'].value_counts())
#print(df_h4['Issue2_string'].value_counts())
#print(df_h4['Issue3_string'].value_counts())

# Create a list with the keywords related to welfare
welfare_keywords = ['welfare', 'industry, agriculture, environment', 'economy', 'healthcare']

# Create a column with True/False values (depending on whether the keyword appears in any of the three columns or not)
for key in welfare_keywords:
    df_h4[key] = (df_h4['Issue1_string'].str.lower().str.contains(key)) | (df_h4['Issue2_string'].str.lower().str.contains(key)) | (df_h4['Issue3_string'].str.lower().str.contains(key))
# Create a column with False value by default    
df_h4['welfare_issues'] = False
# Update the identity_issues column by setting it to True if any welfare keyword is present in any of the three Issue columns.
for key in welfare_keywords:
    df_h4['welfare_issues'] = df_h4['welfare_issues'] | df_h4[key]
# Count the amount of total mobilizations by year
total_mob_year = df_h4.groupby('Year')['Year'].count()
# Count the amount of total welfare mobilizations by year
total_welfare_year = df_h4.groupby('Year')['welfare_issues'].sum()
# Calculate the percentage of welfare mobilizations by year
percentage_welfare_year = (total_welfare_year / total_mob_year)*100
print("Share of Welfare/Economic-Related Mobilizations by year")
print(percentage_welfare_year)
print("Peak percentage of Welfare/Economic-Related Mobilizations")
print(percentage_welfare_year.max())
# Create a line chart with the years in x axis and percentage of welfare mobilizations in y axis
plt.figure()
sns.lineplot(x=percentage_welfare_year.index, y=percentage_welfare_year, marker='o')
plt.title('Share of Welfare/Economic-Related Mobilizations Over Time')
plt.ylabel('Percentage of Events (%)')
plt.xlabel('Year')
# Plot an orange area between 2012 and 2014 years
plt.axvspan(2012, 2014, color='orange', alpha=0.2, label='Crisis Years (2012–2014)')
plt.legend()
plt.show()

