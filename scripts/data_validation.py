import pandas as pd
import numpy as np

def validate_pmgsy_data(df):
    """Validate PMGSY dataset before loading to Power BI"""
    required_columns = [
        'STATE_NAME', 'DISTRICT_NAME', 'PMGSY_SCHEME',
        'LENGTH_OF_ROAD_WORK_SANCTIONED_KM', 'COST_OF_WORKS_SANCTIONED_LAKHS',
        'EXPENDITURE_OCCURED_LAKHS', 'LENGTH_OF_ROAD_WORK_COMPLETED_KM'
    ]
    
    # Check required columns exist
    missing = set(required_columns) - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    
    # Check for negative values
    numeric_cols = [
        'LENGTH_OF_ROAD_WORK_SANCTIONED_KM', 'COST_OF_WORKS_SANCTIONED_LAKHS',
        'EXPENDITURE_OCCURED_LAKHS', 'LENGTH_OF_ROAD_WORK_COMPLETED_KM'
    ]
    
    for col in numeric_cols:
        if (df[col] < 0).any():
            raise ValueError(f"Negative values found in {col}")
    
    # Check for missing values
    if df[required_columns].isnull().any().any():
        raise ValueError("Missing values found in required columns")
    
    print("Data validation passed successfully")
    return True

if __name__ == "__main__":
    pmgsy_data = pd.read_csv("PMGSY.csv")
    state_area = pd.read_csv("state_area.csv")
    
    validate_pmgsy_data(pmgsy_data)
    
    # Additional validation for state area
    if state_area['AREA_SQ_KM'].isnull().any():
        raise ValueError("Missing values in state area data")
    
    print("All datasets validated successfully")