import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import plotly.express as px

file_path = './Sleep_health_and_lifestyle_dataset.csv'
df = pd.read_csv(file_path)
df.head()
df.columns
df.isnull().sum()

print(df)