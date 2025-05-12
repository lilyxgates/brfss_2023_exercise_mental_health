# BRFSS Data Analysis: Physical Activity and Health Outcomes
*Written by Lily Gates*  
*March 2025*

## Description
This project analyzes the relationship between physical activity and health outcomes—specifically mental and physical health—using data from the 2023 Behavioral Risk Factor Surveillance System (BRFSS). The dataset includes self-reported survey responses from adults across the United States. The analysis focuses on differences by sex and race/ethnicity, and explores correlations between exercise frequency and poor mental health days.

### Key components include:
* Data cleaning and filtering for relevant health and demographic variables
* Recoding categorical variables for clarity
* Visualizations of average reported health by demographic groups
* A correlation heatmap of exercise variables and mental health indicators

## Usage
### How to Run the Analysis:
1. Place the raw BRFSS .xpt data file (`brfss_data.xpt`) in the same directory as the script.
2. Run the Python script (`brfss_analysis.py`) to:
    * Load and clean the data
    * Generate descriptive statistics
    * Visualize group differences and correlations

### Outputs:
The script will produce the following:
* Bar plots showing average poor physical and mental health by gender and race/ethnicity
* A correlation heatmap showing relationships between mental health and exercise behavior

## Required Dependencies
* `pandas`: Data manipulation
* `numpy`: Numerical operations
* `matplotlib`: Data visualization
* `seaborn`: Statistical visualizations
* `scikit-learn`: For any machine learning-related tasks (if applicable)
* `os`: File handling

## Sources
* [2023 BRFSS Survey Data and Documentation](https://www.cdc.gov/brfss/annual_data/annual_2023.html)
* 2023 BRFSS Data (SAS Transport Format) saved as 'brfss_data.xpt'

## Important Columns in Original Dataset

### 1. Physical and Mental Health Variables
These columns assess general health status and specific issues related to physical and mental health, key to understanding the potential impact of physical activity on overall health.

- **GENHLTH (General Health)**: Respondent's self-reported general health status, ranging from excellent to poor.
- **PHYSHLTH (Physical Health)**: Number of days in the past 30 days the respondent had poor physical health.
- **MENTHLTH (Mental Health)**: Number of days in the past 30 days the respondent had poor mental health.
- **POORHLTH (Poor Health)**: Number of days in the past 30 days when poor physical or mental health prevented usual activities.

### 2. Exercise-Related Variables
These columns provide insights into exercise frequency, duration, and types, which are crucial for analyzing the relationship between exercise and health outcomes.

- **EXERANY2 (Exercise in Past 30 Days)**: Whether the individual engaged in physical activity in the past month.
- **EXRACT12 (Primary Physical Activity in Past Month)**: The most common physical activity in the past month.
- **EXEROFT1 (Frequency of Walking, Running, Jogging, Swimming)**: Frequency of engagement in walking, running, jogging, or swimming.
- **EXERHMM1 (Duration of Walking, Running, Jogging, Swimming)**: Duration of each session for these activities.
- **EXEROFT2 (Frequency of Another Physical Activity)**: Frequency of another type of physical activity.
- **EXERHMM2 (Duration of Another Physical Activity)**: Duration of another type of physical activity.
- **EXRACT22 (Other Physical Activity Giving Most Exercise)**: The next most common physical activity.
- **STRENGTH (Strength-Training Activity Frequency)**: Frequency of strength exercises, associated with both physical and mental health improvements.

### 3. Computed Variables
These variables simplify health status into categories based on poor health days, which could be useful for comparisons or categorization.

- **_MENT14D (Computed Mental Health Status)**: Categorizes respondents based on poor mental health days (0 days, 1-13 days, 14-30 days).
- **_PHYS14D (Computed Physical Health Status)**: Categorizes respondents based on poor physical health days (0 days, 1-13 days, 14-30 days).

### 4. Demographic Variables
Demographic information is important for subgroup analysis to understand if physical activity and mental health outcomes differ by gender or race/ethnicity.

- **SEXVAR (Sex/Gender)**: Gender differences in physical activity and mental health.
- **_RACE (Race/Ethnicity)**: Racial/ethnic differences in physical activity and mental health.
