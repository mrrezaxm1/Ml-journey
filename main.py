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

if __name__== '__main__':
  main()
