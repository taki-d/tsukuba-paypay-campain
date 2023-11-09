import pandas as pd
import tabula
import glob
import csv

if __name__=='__main__':
    print('Reading PDF file...')
    with open("output.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(["店舗名", "店舗住所", "業種"])
        for file in glob.glob('list/*.pdf'):
            dfs = tabula.read_pdf(file, lattice=True, pages='all')
            for df in dfs:
                for index, row in df.iterrows():
                    if pd.isna(row["屋号"]):
                        continue
                
                    csv_writer.writerow([f'{row["屋号"]} {row["店舗名"] if not pd.isna(row["店舗名"]) else "" }', row['店舗住所'], row['業種']])