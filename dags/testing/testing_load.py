import pytest 
import pandas as pd
from utils.load import load

def test_validasi_input_raise_error(mocker):
    dummy_df = pd.DataFrame({
        'A': [None, None, None],
        'B': [None, None, None]
    })
    dummy_path = "dummy.csv"

    # 👇 Mock to_csv supaya tidak menulis file
    mocker.patch.object(pd.DataFrame, "to_csv")

    with pytest.raises(RuntimeError):
        load(dummy_df, dummy_path)
        
