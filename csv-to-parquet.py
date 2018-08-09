import pandas as pd

csvPath = ""
parquetFilename = ""

df = pd.read_csv(csvPath)
df.to_parquet(parquetFilename)
