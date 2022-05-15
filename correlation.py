import pandas as pd
df = pd.read_csv("/Users/nirajkc/Desktop/Lesson 3 Practice /mtcars.csv")
df.describe()

df[["hp","carb"]].groupby(["hp"]).describe().unstack()

df[["hp","carb"]].corr()

df.to_csv("/Users/nirajkc/Desktop/Lesson 3 Practice /mtcars1.csv")
# Python code in juypter notebook