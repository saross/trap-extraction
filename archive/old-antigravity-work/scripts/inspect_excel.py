import pandas as pd
import os

files = [
    '/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04/Kazanluk/2011-11-30/Project Records/MasterRecords/Kaz11_SurveySummary.xlsx',
    '/media/shawn/191c3b96-5fa5-4d0d-8805-0cf05d3d8468/synology/Adela/TRAP-WD-2020-04/Elhovo 2010-12-12/2009/Project Records/Master Records/ELH09 SurveySummary.xls'
]

for f in files:
    if os.path.exists(f):
        print(f"--- {os.path.basename(f)} ---")
        try:
            # Read first few rows to see layout
            df = pd.read_excel(f, header=None, nrows=10)
            print(df.to_string())
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"File not found: {f}")
