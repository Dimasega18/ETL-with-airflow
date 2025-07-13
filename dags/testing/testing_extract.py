import pytest 
import pandas as pd
from utils.extract import extract

def test_extract_csv_success(mocker):
    # Setup dummy path dan dummy dataframe
    dummy_path = "dummy.csv"
    dummy_df = pd.DataFrame({'a': [1, 2]})

    # Mock glob.glob agar seolah file ditemukan
    mocker.patch('glob.glob', return_value=[dummy_path])

    # Mock pd.read_csv agar tidak benar-benar load file
    mock_read = mocker.patch('pandas.read_csv', return_value=dummy_df)

    # Panggil fungsi
    result = extract(dummy_path)

    # Assertion
    assert result.equals(dummy_df)
    mock_read.assert_called_once_with(rf'{dummy_path}')  # pastikan read_csv dipanggil

def test_extract_csv_not_found(mocker):
    dummy_path = "notfound.csv"

    # Mock glob.glob agar seolah file tidak ditemukan
    mocker.patch('glob.glob', return_value=[])

    # Expect raise error
    with pytest.raises(ImportError, match="Can't find your csv file or your file is not csv."):
        extract(dummy_path)

def test_extract_not_csv_extension(mocker):
    dummy_path = "dummy.txt"

    # File ditemukan tapi bukan .csv
    mocker.patch('glob.glob', return_value=[dummy_path])

    # Expect raise error
    with pytest.raises(ImportError, match="Can't find your csv file or your file is not csv."):
        extract(dummy_path)