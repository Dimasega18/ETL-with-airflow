import pandas as pd

def load(dataframe: pd.DataFrame, output_file:str):
    try:
        # Validasi input
        if dataframe.empty:
            raise ValueError("❌ DataFrame kosong, tidak bisa disimpan.")
        
        # Validasi isi data null semua
        if dataframe.dropna(how="all").empty:
            raise ValueError("❌ Semua baris null, tidak bisa disimpan.")

        # Simpan ke CSV
        dataframe.to_csv(output_file, index=False, mode='w')
        print(f"✅ Data berhasil disimpan ke: {output_file}")

    except Exception as e:
        raise RuntimeError(f"LOAD ERROR : {e}")