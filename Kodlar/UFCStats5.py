import pandas as pd

# Load the data
file_path = 'C:/Users/batuh/Desktop/ufc-fighters-statistics.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataframe to understand its structure
data.head()

# Filter the dataset for relevant columns and remove rows with missing stance or outcome data
filtered_data = data[['name', 'stance', 'wins', 'losses', 'draws', 'significant_striking_accuracy']].dropna(subset=['stance'])

# Calculate total fights and win rate for each fighter
filtered_data['total_fights'] = filtered_data['wins'] + filtered_data['losses'] + filtered_data['draws']
filtered_data['win_rate'] = filtered_data['wins'] / filtered_data['total_fights']

# Group by stance to calculate average win rate and average striking accuracy
stance_stats = filtered_data.groupby('stance').agg(
    average_win_rate=('win_rate', 'mean'),
    average_striking_accuracy=('significant_striking_accuracy', 'mean'),
    total_fighters=('name', 'count')
).reset_index()

stance_stats.sort_values(by='average_win_rate', ascending=False)

import seaborn as sns
import matplotlib.pyplot as plt

# Plotting the relationship between significant striking accuracy and win rate
plt.figure(figsize=(10, 6))
sns.scatterplot(data=filtered_data, x='significant_striking_accuracy', y='win_rate', hue='stance', alpha=0.6)
plt.title('Relationship between Significant Striking Accuracy and Win Rate by Stance')
plt.xlabel('Significant Striking Accuracy (%)')
plt.ylabel('Win Rate')
plt.legend(title='Stance')
plt.grid(True)
plt.show()

