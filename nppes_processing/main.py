# This is a placeholder for your pipeline processing logic

import sys

def transform(df):
  return df

if __name__ == "__main__":
  import pandas as pd

  df = pd.read_csv(sys.argv[1], low_memory=False)
  transformed_df = transform(df)

  n_rows = len(transformed_df)

  print(f"Transformed df has {n_rows} rows.")

  sys.exit(0)
