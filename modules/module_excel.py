import pandas as pd

def search_excel(file_path, target_string):
    df = pd.read_excel(file_path)

    # Check if the first column contains the target string
    mask = df.iloc[:, 0].str.contains(target_string, case=False, na=False)

    # If any match is found, get the corresponding value from the 4th column
    if mask.any():
        result = df.loc[mask, df.columns[3]].values[0]
        return result
    else:
        return None


