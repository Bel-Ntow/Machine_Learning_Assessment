import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('bank-additional-full.csv', sep=';')  

print(df.head(10))