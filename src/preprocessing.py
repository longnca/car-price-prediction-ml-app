import pandas as pd

class DataPreprocessor:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_data(self, filepath):
        """Read the dataset in CSV and convert to a DataFrame."""
        return pd.read_csv(self.filepath)
    
    def preprocess_data(self, df):
        """Convert column names to lowercase and replace spaces with underscores."""
        df.columns = df.columns.str.lower().str.replace(' ', '_')
        string_columns = df.select_dtypes(include='object').columns
        for col in string_columns:
            df[col] = df[col].str.lower().str.replace(' ', '_')
        return df