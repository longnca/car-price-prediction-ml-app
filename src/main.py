from preprocessing import DataPreprocessor

# Define the path to your dataset
filepath = "./data/car_prices_data.csv"

# Create an instance of the DataPreprocessor class
preprocessor = DataPreprocessor(filepath)

# Load and preprocess the data
df = preprocessor.load_data(filepath)
df_preprocessed = preprocessor.preprocess_data(df)

# Test printing the first 5 rows of dataframe
# print(df_preprocessed.head())