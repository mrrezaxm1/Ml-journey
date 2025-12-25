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
  high_salary = df[df["salary"] > 50000]
  

  print("High salary employees:")
  print(high_salary)

  print("Count high salary:",   high_salary.shape[0])
  print("Mean high salary:",
 high_salary["salary"].mean())

  df["level"] = ["junior", "mid", "senior", "senior"]

  grouped = df.groupby("level")["salary"].mean()

  print(grouped)







if __name__== '__main__':
  main()
