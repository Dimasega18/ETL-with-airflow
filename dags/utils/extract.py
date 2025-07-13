import pandas as pd
import glob

def extract(file_input:str):
    
    check_file = glob.glob(file_input)
    
    if file_input.endswith('.csv') and len(check_file) > 0 :
    
        df_extract = pd.read_csv(rf'{file_input}').infer_objects()
    
        print("Data telah diekstrak...")
    
        return df_extract
    
    else:
        raise ImportError("Can't find your csv file or your file is not csv.")