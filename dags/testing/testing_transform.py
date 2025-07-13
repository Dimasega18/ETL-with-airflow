import pytest 
import pandas as pd
from utils.transform import transform

def test_transform_basic():
    # Data sederhana, semua kolom valid
    data = {
        'A': [1, 2, 3],
        'B': ['x', 'y', 'z'],
        'Date': ['2024-01-01', '2024-02-02', '2024-03-03']
    }
    df = pd.DataFrame(data)
    result = transform(df)

    assert isinstance(result, pd.DataFrame)
    assert 'A' in result.columns
    assert 'B' in result.columns
    assert pd.api.types.is_datetime64_any_dtype(result['Date'])

def test_transform_drop_null_column():
    # Kolom C punya lebih dari 40% null
    data = {
        'A': [1, 2, 3],
        'B': ['a', 'b', 'c'],
        'C': [None, None, 3]
    }
    df = pd.DataFrame(data)
    result = transform(df)

    assert 'C' not in result.columns  # kolom C harus terhapus

def test_transform_fill_null():
    # Null pada numeric dan object
    data = {
        'A': [1, None, 3],
        'B': ['a', None, 'c']
    }
    df = pd.DataFrame(data)
    result = transform(df)

    assert result['A'].isnull().sum() == 0
    assert result['B'].isnull().sum() == 0
    assert result['A'][1] == 0  # Null numeric jadi 0
    assert result['B'][1] == 'unknown'  # Null object jadi 'unknown'

def test_transform_raises_error_if_still_null():
    # Force error with unfilled nulls
    data = pd.DataFrame({
        'A': [None, None, None]  # Kolom numeric, tapi semua null
    })
    with pytest.raises(RuntimeError):
        transform(data)