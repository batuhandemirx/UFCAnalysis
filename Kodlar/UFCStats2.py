import pandas as pd

# Load the dataset
ufc_data_path = 'C:/Users/batuh/Desktop/ufc.csv'
ufc_data = pd.read_csv(ufc_data_path)


# Unifying fighter statistics into individual records
fighter_1_data = ufc_data[['Fighter 1', 'Fighter_1_KD', 'Fighter_1_STR', 'Weight_Class', 'Method', 'Date']].copy()
fighter_2_data = ufc_data[['Fighter 2', 'Fighter_2_KD', 'Fighter_2_STR', 'Weight_Class', 'Method', 'Date']].copy()

# Renaming columns to unify
fighter_1_data.columns = ['Fighter', 'KD', 'STR', 'Weight_Class', 'Method', 'Date']
fighter_2_data.columns = ['Fighter', 'KD', 'STR', 'Weight_Class', 'Method', 'Date']

# Create a new column 'Fighter_Name' to store fighter names
ufc_data['Fighter_Name_1'] = ufc_data['Fighter 1']
ufc_data['Fighter_Name_2'] = ufc_data['Fighter 2']

# Combining the datasets back into one
combined_data = pd.concat([fighter_1_data, fighter_2_data], axis=0)

# Filtering relevant weight classes
relevant_weight_classes = ['Lightweight', 'Welterweight', 'Middleweight', 'Light Heavyweight', 'Heavyweight']
combined_data = combined_data[combined_data['Weight_Class'].isin(relevant_weight_classes)]

# Calculating KO/TKO wins for each fighter
combined_data['KO/TKO_Win'] = combined_data['Method'].apply(lambda x: 1 if 'KO/TKO' in x else 0)
fighter_stats = combined_data.groupby('Fighter').agg(
    Total_KD=('KD', 'sum'),
    Total_STR=('STR', 'sum'),
    KO_TKO_Wins=('KO/TKO_Win', 'sum'),
    Fights=('Date', 'count')
)

# Filtering based on criteria: more than 100 significant strikes and at least 5 KO/TKO wins
filtered_fighter_stats = fighter_stats[(fighter_stats['Total_STR'] > 140) & (fighter_stats['KO_TKO_Wins'] >= 7)]

# Create a new column 'Fighter_Name' to store fighter names
filtered_fighter_stats['Fighter_Name'] = filtered_fighter_stats.index

# Create Punch_Power_Score and Adjusted_Score columns
filtered_fighter_stats['Punch_Power_Score'] = filtered_fighter_stats['Total_KD'] / filtered_fighter_stats['Total_STR']
filtered_fighter_stats['Adjusted_Score'] = filtered_fighter_stats['Punch_Power_Score'] * (1 + 0.01 * (filtered_fighter_stats['Fights'] - 1))

# Determine the most fought weight class for each fighter
most_frequent_weight_class = combined_data.groupby('Fighter')['Weight_Class'].agg(lambda x: x.mode().iloc[0])

# Joining the most frequent weight class with the filtered fighter stats
filtered_fighter_stats = filtered_fighter_stats.join(most_frequent_weight_class, on='Fighter', how='left').rename(columns={'Weight_Class': 'Most_Frequent_Weight_Class'})

# Ranking fighters within each weight class based on their adjusted punch power score
ranked_fighters_per_class = filtered_fighter_stats.groupby('Most_Frequent_Weight_Class').apply(
    lambda x: x.nlargest(5, 'Adjusted_Score')
).reset_index(drop=True)

# Display the top 5 power punchers in each specified division with fighter names
ranked_fighters_per_class[ranked_fighters_per_class['Most_Frequent_Weight_Class'].isin(relevant_weight_classes)]



