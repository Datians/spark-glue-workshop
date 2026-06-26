"""
scripts/prepare_csv.py

Convierte el archivo Excel Online Retail II en dos archivos CSV,
uno por cada hoja/año del dataset.

Requisito:
    pip install pandas openpyxl

Entrada esperada:
    data/online_retail_II.xlsx

Salidas:
    data/online_retail_ii_2009_2010.csv
    data/online_retail_ii_2010_2011.csv
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path("data")
EXCEL_PATH = DATA_DIR / "online_retail_II.xlsx"

SHEET_TO_FILENAME = {
    "Year 2009-2010": "online_retail_ii_2009_2010.csv",
    "Year 2010-2011": "online_retail_ii_2010_2011.csv",
}


def main() -> None:
    if not EXCEL_PATH.exists():
        raise FileNotFoundError(
            f"No se encontró {EXCEL_PATH}. Descarga y descomprime el dataset en data/."
        )

    xls = pd.ExcelFile(EXCEL_PATH)

    for sheet_name, filename in SHEET_TO_FILENAME.items():
        df = xls.parse(sheet_name)
        output_path = DATA_DIR / filename
        df.to_csv(output_path, index=False)
        print(f"{filename} generated: {len(df):,} rows")


if __name__ == "__main__":
    main()
