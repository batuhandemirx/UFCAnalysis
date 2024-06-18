import pandas as pd

# Load the data
data = pd.read_csv('C:/Users/batuh/Desktop/ufc.csv')

# Ensure all 'Time' values are strings to handle them uniformly
data['Time'] = data['Time'].astype(str)

# Calculate total fight duration in minutes
def calculate_total_minutes(row):
    try:
        rounds = (row['Round'] - 1) * 5
        time_parts = row['Time'].split(':')
        minutes = rounds + int(time_parts[0]) + int(time_parts[1]) / 60 if len(time_parts) == 2 else rounds
    except:
        minutes = 0  # Default to 0 in case of any issue
    return minutes

data['Total_Minutes'] = data.apply(calculate_total_minutes, axis=1)

# Filtering data for the specified weight classes
weight_classes_of_interest = ['Lightweight', 'Welterweight', 'Middleweight', 'Light Heavyweight', 'Heavyweight']
data_filtered = data[data['Weight_Class'].isin(weight_classes_of_interest)]

# Initialize DataFrame to store durability scores
durability_scores = pd.DataFrame()

# Calculate durability scores with adjusted criteria
for index, row in data_filtered.iterrows():
    for fighter_num in [1, 2]:
        opponent_num = 1 if fighter_num == 2 else 2
        fighter = row[f'Fighter {fighter_num}']
        weight_class = row['Weight_Class']
        won = row['Winner'] == fighter
        # Adjust criteria: Focus on knockdowns and takedowns absorbed, significant strikes absorbed
        knockdowns_absorbed = row[f'Fighter_{opponent_num}_KD']
        takedowns_absorbed = row[f'Fighter_{opponent_num}_TD']
        sig_strikes_absorbed = row[f'Fighter_{opponent_num}_STR']
        # Adjust fight duration score based on fight outcome
        fight_duration = row['Total_Minutes'] * (0.5 if not won else 1)
        # Simplified calculation for durability score
        durability_score = fight_duration + (knockdowns_absorbed + takedowns_absorbed) * 2 - sig_strikes_absorbed * 0.5
        # Append to DataFrame
        new_row = {
            'Fighter': fighter,
            'Weight_Class': weight_class,
            'Durability_Score': durability_score
        }
        durability_scores = pd.concat([durability_scores, pd.DataFrame([new_row])], ignore_index=True)

# Aggregate scores by fighter and weight class
durability_scores_aggregated = durability_scores.groupby(['Fighter', 'Weight_Class']).agg({'Durability_Score': 'sum'}).reset_index()

# Find top 5 durable fighters in each weight class
top_durable_fighters_per_class = durability_scores_aggregated.groupby('Weight_Class').apply(lambda x: x.nlargest(5, 'Durability_Score')).reset_index(drop=True)

top_durable_fighters_per_class


