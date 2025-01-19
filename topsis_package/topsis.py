import pandas as pd
import numpy as np

def run_topsis(file_path):
    try:
        # Load the data with appropriate encoding and delimiter
        df = pd.read_csv(file_path, encoding='latin1', delimiter=',', on_bad_lines='skip')
        print("Data loaded successfully.")
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    # Extract criteria matrix and alternative names
    criteria = df.iloc[:, 1:].values  # Performance metrics (P1 to P5)
    alternatives = df.iloc[:, 0].values  # Fund Names

    # Step 1: Normalize the decision matrix
    normalized_matrix = criteria / np.sqrt((criteria**2).sum(axis=0))
    
    # Step 2: Assign equal weights to all criteria
    weights = np.ones(criteria.shape[1]) / criteria.shape[1]
    
    # Weighted normalized matrix
    weighted_matrix = normalized_matrix * weights
    
    # Step 3: Identify ideal (best) and anti-ideal (worst) solutions
    ideal_solution = np.max(weighted_matrix, axis=0)
    anti_ideal_solution = np.min(weighted_matrix, axis=0)
    
    # Step 4: Calculate distances from ideal and anti-ideal solutions
    distance_to_ideal = np.sqrt(((weighted_matrix - ideal_solution)**2).sum(axis=1))
    distance_to_anti_ideal = np.sqrt(((weighted_matrix - anti_ideal_solution)**2).sum(axis=1))
    
    # Step 5: Compute the relative closeness to the ideal solution
    relative_closeness = distance_to_anti_ideal / (distance_to_ideal + distance_to_anti_ideal)

    # Add TOPSIS Score and Rank to the dataframe
    df['TOPSIS Score'] = relative_closeness
    df['Rank'] = df['TOPSIS Score'].rank(ascending=False)
    
    # Sort by rank
    df_sorted = df.sort_values(by='Rank')

    # Save the result to a CSV file
    df_sorted.to_csv('102203351-result.csv', index=False)
    print("Results saved to '102203351-result.csv'.")
    return df_sorted

# Call the function with the file path
result = run_topsis(r'C:\Users\waliamax\Downloads\102203351-data.csv')
