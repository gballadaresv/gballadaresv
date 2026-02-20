import pandas as pd
from collections import Counter

# Define a function to categorize weather conditions
def categorize_weather(row):
    conditions = row['conditions'].lower() if pd.notnull(row['conditions']) else ""
    description = row['description'].lower() if pd.notnull(row['description']) else ""
    windspeed = row['windspeed'] if pd.notnull(row['windspeed']) else 0
    windgust = row['windgust'] if pd.notnull(row['windgust']) else 0
    
    # Priority-based categorization
    if "snow" in conditions or "snow" in description:
        return "Snowy"
    elif "rain" in conditions or "rain" in description:
        return "Rainy"
    elif "partially cloudy" in conditions or "partly-cloudy" in conditions or "partially cloudy" in description or "partly-cloudy" in description:
        return "Cloudy"  # Renamed from "Partially Cloudy"
    elif windspeed > 20 or windgust > 30:
        return "Windy"
    elif "overcast" in conditions or "cloudy" in conditions or "overcast" in description or "cloudy" in description:
        return "Foggy"  # Renamed from "Cloudy"
    elif "clear" in conditions or "clear-day" in conditions or "clear-night" in conditions or "clear" in description:
        return "Sunny"
    else:
        return "Unknown"  # For any uncategorized conditions

# Load the CSV files
file_paths = ["22-23.csv", "23-24.csv", "24-25.csv"]  # Add all file paths here
dataframes = [pd.read_csv(file_path) for file_path in file_paths]

# Concatenate all dataframes into one
weather_data = pd.concat(dataframes, ignore_index=True)

# Apply the categorization function
weather_data['state'] = weather_data.apply(categorize_weather, axis=1)

# Save the categorized data to a new CSV (optional)
weather_data.to_csv("categorized_weather_data.csv", index=False)

# Print the first few rows to verify
print(weather_data[['datetime', 'conditions', 'description', 'state']].head())

# Count the occurrences of each state
state_counts = Counter(weather_data['state'])

# Print the counts
print("State Counts:")
for state, count in state_counts.items():
    print(f"{state}: {count}")


# Create a list of consecutive state transitions
state_transitions = [
    (weather_data['state'][i], weather_data['state'][i + 1])
    for i in range(len(weather_data['state']) - 1)
]

# Count the occurrences of each state transition
transition_counts = Counter(state_transitions)

# Print the transition counts
print("State Transition Counts:")
for transition, count in transition_counts.items():
    print(f"{transition}: {count}")

# Optional: Normalize the counts to create a transition matrix
# Initialize a dictionary to store the transition probabilities
transition_matrix = {}

for (state_from, state_to), count in transition_counts.items():
    if state_from not in transition_matrix:
        transition_matrix[state_from] = {}
    transition_matrix[state_from][state_to] = count / state_counts[state_from]

# Print the transition matrix
print("\nTransition Matrix (Probabilities):")
for state_from, transitions in transition_matrix.items():
    print(f"{state_from}:")
    for state_to, probability in transitions.items():
        print(f"  {state_to}: {probability:.4f}")


# Define all possible states
states = ["Sunny", "Cloudy", "Foggy", "Rainy", "Snowy", "Windy"]

# Create a DataFrame to represent the transition matrix
matrix_df = pd.DataFrame(0.0, index=states, columns=states)

# Populate the DataFrame with probabilities from the transition_matrix
for state_from, transitions in transition_matrix.items():
    for state_to, probability in transitions.items():
        matrix_df.loc[state_from, state_to] = probability

# Print the transition matrix as a 6x6 table
print("\nTransition Matrix (6x6):")
print(matrix_df)