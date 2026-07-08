from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "Test task (Operations Research Scientist) (1).xlsx"


def load_data(sheet_name: str, data_path=DATA_PATH):
    return pd.read_excel(data_path, sheet_name=sheet_name, header=0)