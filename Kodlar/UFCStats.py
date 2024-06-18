import pandas as pd

# Load the dataset
file_path = 'C:/Users/batuh/Desktop/ufc-fighters-statistics.csv'
ufc_data = pd.read_csv(file_path)

# Selecting relevant columns
relevant_columns = ['height_cm', 'weight_in_kg', 'reach_in_cm', 'wins', 'losses', 
                    'significant_strikes_landed_per_minute', 'significant_striking_accuracy',
                    'average_takedowns_landed_per_15_minutes', 'takedown_accuracy']

# Creating a new DataFrame with only relevant columns
ufc_analysis = ufc_data[relevant_columns]

# Dropping rows with missing values in the relevant columns
ufc_analysis_clean = ufc_analysis.dropna()
import seaborn as sns
import matplotlib.pyplot as plt

# Calculating the correlation matrix
correlation_matrix = ufc_analysis_clean.corr()

# Plotting the correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix of UFC Fighters' Attributes and Performance Metrics")
plt.show()


stances = ufc_data['stance'].dropna().unique()

# Initializing an empty list to store performance data for each stance
performance_data = []

for stance in stances:
    stance_data = ufc_data[ufc_data['stance'] == stance]
    performance_mean = stance_data[performance_metrics].mean()
    performance_mean.name = stance
    performance_data.append(performance_mean)

# Converting the list of Series into a DataFrame
stance_performance = pd.concat(performance_data, axis=1).transpose()

# Plotting the performance metrics for different stances
stance_performance.plot(kind='bar', figsize=(15, 8))
plt.title('Comparison of Performance Metrics Across Different Stances')
plt.ylabel('Average Metrics')
plt.xlabel('Stance')
plt.xticks(rotation=45)
plt.show()

# Analyzing the impact of striking accuracy on fight outcomes (wins)
plt.figure(figsize=(8, 5))
sns.scatterplot(x='significant_striking_accuracy', y='wins', data=ufc_data)
plt.title('Impact of Striking Accuracy on Fight Outcomes (Wins)')
plt.xlabel('Significant Striking Accuracy')
plt.ylabel('Wins')
plt.show()


# Visualizing Takedown Defense and Takedown Accuracy

# Filtering out irrelevant or extreme values (e.g., takedown defense above 100%)
filtered_ufc_data = ufc_data[(ufc_data['takedown_defense'] <= 100) & (ufc_data['takedown_accuracy'] <= 100)]

# Scatter plot for Takedown Defense vs. Takedown Accuracy
plt.figure(figsize=(10, 6))
sns.scatterplot(x='takedown_accuracy', y='takedown_defense', data=filtered_ufc_data)
plt.title('Takedown Defense vs. Takedown Accuracy')
plt.xlabel('Takedown Accuracy (%)')
plt.ylabel('Takedown Defense (%)')
plt.show()

# Analyzing Striking Accuracy and Defense

# Scatter plot for Significant Striking Accuracy vs. Significant Strike Defense
plt.figure(figsize=(10, 6))
sns.scatterplot(x='significant_striking_accuracy', y='significant_strike_defence', data=ufc_data)
plt.title('Significant Striking Accuracy vs. Strike Defense')
plt.xlabel('Significant Striking Accuracy (%)')
plt.ylabel('Significant Strike Defence (%)')
plt.show()

# Correlation between Takedown Accuracy and Takedown Defense
takedown_corr = filtered_ufc_data[['takedown_accuracy', 'takedown_defense']].corr()

# Displaying the correlation
takedown_corr




