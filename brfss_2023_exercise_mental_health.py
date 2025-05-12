# Lily Gates
# March 30, 2025

# Source: 2023 BRFSS Survey Data and Documentation https://www.cdc.gov/brfss/annual_data/annual_2023.html
# 2023 BRFSS Data (SAS Transport Format) saved as 'brfss_data.xpt'

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import cm
import seaborn as sns
import os
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler


#########################################
#########  FULL PATH FOR FILE #########
#########################################

# Get the current working directory
current_directory = os.path.dirname(os.path.realpath(__file__))

# File name
file_name = "brfss_data.xpt"

# Construct the full file path
file_path = os.path.join(current_directory, file_name)

# Confirm Paths
#print("\n###########################################################\n")
#print(f"CURRENT DIRECTORY: {current_directory}\n")
#print(f"FILE PATH: {file_path}\n")
#print("###########################################################\n")

# Read the SAS transport file (.xpt) into a pandas DataFrame
df = pd.read_sas(file_path)

# Save original raw df to CSV
df.to_csv('brfss_raw.csv')



#########################################
######### DATA: All Relevant Columns #########
#########################################

# List of relevant columns for analysis
relevant_columns = [
    'SEXVAR', '_RACE', 'GENHLTH', 'PHYSHLTH', 'MENTHLTH', 'POORHLTH', 
    'EXERANY2', 'EXRACT12', 'EXEROFT1', 'EXERHMM1', 'EXEROFT2', 'EXERHMM2', 
    'EXRACT22', 'STRENGTH', '_MENT14D', '_PHYS14D'
]

# Filter for the relevant health and demographic columns
df_filtered = df[relevant_columns]


#########################################
######### DATA: Cleaning Data  #########
######### Health Data, NaNs  #########
#########################################
# Define special codes to exclude
special_codes_health = [77, 88, 99]
special_codes_exercise = [777, 888, 999]

# Clean health-related columns (PHYSHLTH, MENTHLTH, POORHLTH)
df_filtered['PHYSHLTH'] = df_filtered['PHYSHLTH'].replace(special_codes_health, float('nan'))
df_filtered['MENTHLTH'] = df_filtered['MENTHLTH'].replace(special_codes_health, float('nan'))
df_filtered['POORHLTH'] = df_filtered['POORHLTH'].replace(special_codes_health, float('nan'))

# Clean exercise-related columns (EXEROFT1, EXEROFT2, STRENGTH)
df_filtered['EXEROFT1'] = df_filtered['EXEROFT1'].replace(special_codes_exercise, float('nan'))
df_filtered['EXEROFT2'] = df_filtered['EXEROFT2'].replace(special_codes_exercise, float('nan'))
df_filtered['STRENGTH'] = df_filtered['STRENGTH'].replace(special_codes_exercise, float('nan'))

# Drop rows with missing values for health or exercise variables
df_filtered_clean = df_filtered.dropna(subset=['PHYSHLTH', 'MENTHLTH', 'POORHLTH', 'EXEROFT1', 'EXEROFT2', 'STRENGTH'])

# Save df_filtered to CSV
df_filtered.to_csv('brfss_filtered.csv')


#########################################
######### DATA: Cleaning Data  #########
######### Relabel Demographics  #########
#########################################

# Label the values for SEXVAR and _RACE columns
# Sex classification: 1 = Male, 2 = Female
df_filtered_clean["SEXVAR"] = df_filtered_clean["SEXVAR"].map({1: "Male", 2: "Female"})

# Race/Ethnicity classification
df_filtered_clean["_RACE"] = df_filtered_clean["_RACE"].map({
    1: "White (non-Hispanic)", 
    2: "Black (non-Hispanic)", 
    3: "American Indian or Alaskan Native (non-Hispanic)", 
    4: "Asian (non-Hispanic)", 
    5: "Native Hawaiian or Pacific Islander (non-Hispanic)", 
    6: "Other race (non-Hispanic)", 
    7: "Multiracial (non-Hispanic)", 
    8: "Hispanic", 
    9: "Don’t know/Refused"
})

# Save df_filtered_clean to CSV
#df_filtered_clean.to_csv('brfss_filtered_clean.csv')


###################################
######### DATA: Cleaning  #########
######### FINAL VERSION  ##########
###################################

# Descriptive statistics for continuous variables
descriptive_stats = df_filtered_clean.describe()

# Show the cleaned and labeled data
#print(df_filtered_clean.head())

# Show the descriptive statistics
#print(descriptive_stats)


########################################
################ GRAPHS ################
########################################

########################################
##### Grouped Averages for Sex/Race ####
########################################
import seaborn as sns
import matplotlib.pyplot as plt

# Calculate mean values of PHYSHLTH and MENTHLTH by SEXVAR and _RACE
mean_values = df_filtered_clean.groupby(['SEXVAR', '_RACE'])[['PHYSHLTH', 'MENTHLTH']].mean().reset_index()

# Set the size of the plot
plt.figure(figsize=(12, 6))

# Create a bar plot for the mean values of PHYSHLTH
sns.barplot(x='SEXVAR', y='PHYSHLTH', hue='_RACE', data=mean_values, palette='muted')

# Customize the plot
plt.title('Average Poor Physical Health by Gender and Race/Ethnicity', fontsize=14)
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Average Poor Physical Health Days', fontsize=12)

# Move the legend below the x-axis
plt.legend(title='_RACE', loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3)

# Show the plot
plt.tight_layout()
plt.show()

# Create a bar plot for the mean values of MENTHLTH
plt.figure(figsize=(12, 6))
sns.barplot(x='SEXVAR', y='MENTHLTH', hue='_RACE', data=mean_values, palette='muted')

# Customize the plot
plt.title('Average Poor Mental Health by Gender and Race/Ethnicity', fontsize=14)
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Average Poor Mental Health Days', fontsize=12)

# Move the legend below the x-axis
plt.legend(title='_RACE', loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3)

# Show the plot
plt.tight_layout()
plt.show()



########################################
##### Correlation Heatmap ###############
########################################

# Normalize the data
scaler = StandardScaler()
normalized_data = scaler.fit_transform(df_filtered_clean[['EXEROFT1', 'EXEROFT2', 'STRENGTH', 'MENTHLTH']])

# Convert the normalized data back to a DataFrame for readability
normalized_df = pd.DataFrame(normalized_data, columns=['EXEROFT1', 'EXEROFT2', 'STRENGTH', 'MENTHLTH'])

# Calculate the correlation matrix for the normalized data
correlation_matrix = normalized_df.corr()

# Plot the correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, fmt='.2f', linewidths=0.5)
plt.title('Normalized Correlation Heatmap: Exercise Frequency vs. Mental Health', fontsize=14)
plt.tight_layout()
plt.show()

