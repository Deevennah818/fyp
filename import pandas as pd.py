import pandas as pd

# List of CSV file paths with labels
file_paths = [
    (r"C:\\Users\\Dee\\OneDrive - Asia Pacific University\\Desktop\\fyp dataset\\NewsFakeCOVID-19.csv", 0),
    (r"C:\\Users\\Dee\\OneDrive - Asia Pacific University\\Desktop\\fyp dataset\\NewsFakeCOVID-19_5.csv", 0),
    (r"C:\\Users\\Dee\\OneDrive - Asia Pacific University\\Desktop\\fyp dataset\\NewsFakeCOVID-19_7.csv", 0),
    (r"C:\\Users\\Dee\\OneDrive - Asia Pacific University\\Desktop\\fyp dataset\\NewsRealCOVID-19.csv", 1),
    (r"C:\\Users\\Dee\\OneDrive - Asia Pacific University\\Desktop\\fyp dataset\\NewsRealCOVID-19_5.csv", 1),
    (r"C:\\Users\\Dee\\OneDrive - Asia Pacific University\\Desktop\\fyp dataset\\NewsRealCOVID-19_7.csv", 1)
]

# Columns to keep
important_columns = ['news_url', 'title', 'content', 'publish_date', 'meta_keywords', 'label']

# Load datasets
dfs = []
for file, label in file_paths:
    try:
        df = pd.read_csv(file)
        df["label"] = label  # Assign label
        
        # Ensure all important columns exist, filling missing ones with NaN
        for col in important_columns:
            if col not in df.columns:
                df[col] = pd.NA
                
        # Keep only the important columns
        df = df[important_columns]
        dfs.append(df)
        
    except FileNotFoundError:
        print(f"File not found: {file}")

# Merge datasets if there are valid DataFrames
output_path = "C:\\Users\\Dee\\OneDrive - Asia Pacific University\\Desktop\\fyp dataset\\Merged_COVID19_Data.csv"
if dfs:
    merged_df = pd.concat(dfs, ignore_index=True)
    merged_df.to_csv(output_path, index=False)
    print(f"Merged dataset saved at: {output_path}")
else:
    print("No valid datasets to merge.")





