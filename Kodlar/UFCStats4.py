import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
ufc_data = pd.read_csv("C:/Users/batuh/Desktop/ufc-fighters-statistics.csv")

# Handle missing reach data
average_reach_height_difference = ufc_data['reach_in_cm'].mean() - ufc_data['height_cm'].mean()
ufc_data['reach_in_cm'].fillna(ufc_data['height_cm'] + average_reach_height_difference, inplace=True)

# Function to analyze and plot for each weight class
def analyze_plot_class(data, lower_bound, upper_bound, class_name):
    class_data = data[(data['weight_in_kg'] > lower_bound) & (data['weight_in_kg'] <= upper_bound)]
    correlation = class_data['reach_in_cm'].corr(class_data['wins'])
    
    # Plot
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=class_data, x='reach_in_cm', y='wins')
    sns.regplot(data=class_data, x='reach_in_cm', y='wins', ci=None, color='blue', line_kws={'color':'red'})
    plt.title(f"Correlation between Reach and Wins in {class_name}: {round(correlation, 2)}")
    plt.xlabel("Reach (cm)")
    plt.ylabel("Wins")
    plt.show()

# Plot for each weight class
analyze_plot_class(ufc_data, 93.5, float('inf'), "Heavyweight")
analyze_plot_class(ufc_data, 92, 93.4, "Light Heavyweight")
analyze_plot_class(ufc_data, 83, 84, "Middleweight")
analyze_plot_class(ufc_data, 77, 78, "Welterweight")
analyze_plot_class(ufc_data, 70, 71, "Lightweight")
analyze_plot_class(ufc_data, 65, 67, "Featherweight")
analyze_plot_class(ufc_data, 60, 62, "Bantamweight")
analyze_plot_class(ufc_data, 55, 57, "Flyweight")
