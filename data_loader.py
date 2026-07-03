import pandas as pd


DATA_PATH = 'data/Test task (Operations Research Scientist) (1).xlsx'


def load_data(sheet_name: str, data_path=DATA_PATH):
    return pd.read_excel(data_path, sheet_name=sheet_name, header=0)