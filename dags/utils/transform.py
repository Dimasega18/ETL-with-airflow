from utils import extract
import pandas as pd
import glob


import pandas as pd

def transform(dataframe: pd.DataFrame) -> pd.DataFrame:
    try:
        df_transform = dataframe.copy()

        # Change object types if possible
        df_transform = df_transform.infer_objects()

        # Convert column 'Date' to datetime, skip error if column not found
        if 'Date' in df_transform.columns:
            df_transform['Date'] = pd.to_datetime(df_transform['Date'], errors='coerce')

        # Drop columns with more than 40% missing values
        total_rows = len(df_transform)
        null_percent = df_transform.isnull().mean()
        cols_to_drop = null_percent[null_percent > 0.4].index
        df_transform.drop(columns=cols_to_drop, inplace=True)

        # Fill remaining nulls
        num_cols = df_transform.select_dtypes(include='number').columns
        obj_cols = df_transform.select_dtypes(include='object').columns

        df_transform[num_cols] = df_transform[num_cols].fillna(0)
        df_transform[obj_cols] = df_transform[obj_cols].fillna('unknown')

        # Final check: no remaining nulls
        if df_transform.isnull().sum().sum() == 0 and not df_transform.empty:
            print("✅ Transform berhasil tanpa null")
            return df_transform
        else:
            raise ValueError("❌ Transform gagal: masih ada nilai null / dataframe menjadi empty")
    except Exception as e:
        raise RuntimeError(f"TRANSFORM ERROR : {e}")