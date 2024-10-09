import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import plotly.express as px

file_path = './Sleep_health_and_lifestyle_dataset.csv'
df = pd.read_csv(file_path)
# df.head() #แสดงข้อมูล 5 ชุดแรก
# df.columns #แสดงชื่อคอลัมน์
# df.isnull().sum()
#df.info() #แสดงค่าข้อมูลของแต่ละคอลัมน์ ว่าเป็นชนิดข้อมูลแบบไหน
#df.describe() #แสดงค่าเชิงสถิติ
#df.duplicated().sum() #ใช้เพื่อตรวจสอบแถวที่ซ้ำกันใน DataFrame โดยมันจะคืนค่าเป็นซีรีส์ของค่าบูลีน (True หรือ False) 
#(df.isna().sum()/len(df))*100#ใช้สำหรับคำนวณ เปอร์เซ็นต์ของค่า missing (NaN) ในแต่ละคอลัมน์ของ DataFrame ซึ่งช่วยให้เข้าใจว่าแต่ละคอลัมน์มีข้อมูลสูญหายมากน้อยเพียงใด
#df[df['Sleep Disorder'].isna()] #ใช้เพื่อ กรองและเลือกแถว จาก DataFrame df ที่คอลัมน์ 'Sleep Disorder' มีค่าเป็น NaN
#df['Sleep Disorder'].unique() #ใช้เพื่อ แสดงค่าเฉพาะ ทั้งหมดในคอลัมน์ 'Sleep Disorder' ของ DataFrame df โดยจะคืนค่าเป็นอาร์เรย์ที่ประกอบด้วยค่าที่ไม่ซ้ำกันในคอลัมน์นั้น รวมถึงค่า NaN หากมี
df['Sleep Disorder'].fillna('No Sleep Disorder', inplace=True) #ใช้เพื่อ แทนที่ค่า NaN  ในคอลัมน์ 'Sleep Disorder' ด้วยค่า 'No Sleep Disorder' โดยทำการแก้ไข DataFrame ต้นฉบับ

print(df.info())

