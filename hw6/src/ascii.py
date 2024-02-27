import pandas as pd
def load_data(datapath):
  return pd.read_csv(datapath)


def display():
  df1 = load_data('././data/diabetes.csv')
  df2 = load_data('././data/soybean.csv')
#   df1 = load_data('../../CSC591_ASE_HW_Group12/data/diabetes.csv')
#   df2 = load_data('../../CSC591_ASE_HW_Group12/data/soybean.csv')
  print('================================================================================')
  print(f"\nASCII table for diabetes")
  print(f"Number of classes in diabetes file: {len(df1['class!'].unique())}")
  print(f"Number of rows for each class in %:")
  print(f"{df1['class!'].value_counts()/len(df1)*100}")
  print('================================================================================')
  print()

  print(f"ASCII table for Soybean")
  print(f"Number of classes in diabetes file: {len(df2['class!'].unique())}")
  print(f"Number of rows for each class in %:")
  print(f"{df2['class!'].value_counts()/len(df2)*100}")
  print('================================================================================')

if __name__=="__main__":
  display()