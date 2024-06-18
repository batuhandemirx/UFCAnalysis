import pandas as pd
from scipy.stats import pearsonr, linregress
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
data = pd.read_csv(r"C:\Users\batuh\Desktop\ufc-fighters-statistics.csv")


# Unique stances
stances = data['stance'].unique()

# Calculating the correlation coefficient and linear regression for each stance
for stance in stances:
    stance_data = data[data['stance'] == stance].copy()  # Create a copy to avoid SettingWithCopyWarning
    stance_data['win_rate'] = stance_data['wins'] / (stance_data['wins'] + stance_data['losses'])

    # Check if there are at least two data points
    if len(stance_data) > 1:
        correlation, _ = pearsonr(stance_data['significant_striking_accuracy'], stance_data['win_rate'])
        print(f'Correlation coefficient for {stance} stance: {correlation:.3f}')
        
        # ... (rest of your linear regression code)

    else:
        print(f'Not enough data to calculate correlation or perform regression for {stance} stance.')


# Linear regression and plotting
for stance in stances:
    stance_data = data[data['stance'] == stance]
    stance_data['win_rate'] = stance_data['wins'] / (stance_data['wins'] + stance_data['losses'])

    if len(stance_data) > 1:
        slope, intercept, r_value, p_value, std_err = linregress(stance_data['significant_striking_accuracy'], stance_data['win_rate'])
        
        # Plotting the regression line
        plt.scatter(stance_data['significant_striking_accuracy'], stance_data['win_rate'], label=f'{stance} stance')
        line = slope * stance_data['significant_striking_accuracy'] + intercept
        plt.plot(stance_data['significant_striking_accuracy'], line, label=f'{stance} Regression Line')
        
        print(f'Linear regression for {stance} stance: Slope = {slope:.3f}, Intercept = {intercept:.3f}, '
              f'R-squared = {r_value**2:.3f}, p-value = {p_value:.3g}')
    else:
        print(f'Not enough data to perform linear regression for {stance} stance.')

plt.xlabel('Significant Striking Accuracy')
plt.ylabel('Win Rate')
plt.title('Linear Regression Analysis by Stance')
plt.legend()
plt.show()

# Group statistics for each stance
for stance in stances:
    stance_data = data[data['stance'] == stance]
    stance_data['win_rate'] = stance_data['wins'] / (stance_data['wins'] + stance_data['losses'])

    if len(stance_data) > 0:
        mean_accuracy = stance_data['significant_striking_accuracy'].mean()
        median_accuracy = stance_data['significant_striking_accuracy'].median()
        std_accuracy = stance_data['significant_striking_accuracy'].std()
        mean_win_rate = stance_data['win_rate'].mean()
        median_win_rate = stance_data['win_rate'].median()
        std_win_rate = stance_data['win_rate'].std()

        print(f'{stance} stance: Mean Accuracy = {mean_accuracy:.2f}%, Median Accuracy = {median_accuracy:.2f}%, '
              f'Std Accuracy = {std_accuracy:.2f}%, Mean Win Rate = {mean_win_rate:.2f}%, '
              f'Median Win Rate = {median_win_rate:.2f}%, Std Win Rate = {std_win_rate:.2f}%')
    else:
        print(f'Not enough data for {stance} stance statistics.')

