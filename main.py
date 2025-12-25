import numpy as np 
import pandas as pd

def main():
  data = {
    'age' : [25,32,47,51],
    'salary' : [40000,52000,80000,110000]
  }
  df = pd.DataFrame(data)
  print('mean age' , np.mean(df['age']))
  print('mean salary ' , np.mean(df['salary']))
  print("len:", len(df["salary"]))
  print("count:", df["salary"].count())
  print("NaN count:",
 df["salary"].isna().sum())

  print("Mean (default):", df["salary"].mean())
  print("Mean dropna:",  df["salary"].dropna().mean())
  print("Mean fillna(0):",  df["salary"].fillna(0).mean())




if __name__== '__main__':
  main()
