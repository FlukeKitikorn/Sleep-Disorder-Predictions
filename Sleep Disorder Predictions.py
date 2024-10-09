#!/usr/bin/env python
# coding: utf-8

# In[56]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt 
import plotly.express as px

from sklearn.preprocessing import MinMaxScaler #ปรับขนาดข้อมูล (scaling) โดยการเปลี่ยนแปลงค่าในชุดข้อมูลให้อยู่ในช่วงระหว่าง 0 ถึง 1
from sklearn.model_selection import train_test_split #แบ่งชุดข้อมูลออกเป็น Training set และ Test set 
from sklearn.linear_model import LogisticRegression #สร้างโมเดล การถดถอยโลจิสติก (Logistic Regression) ซึ่งเป็นอัลกอริธึมที่ใช้สำหรับการจำแนกประเภท (classification)
from sklearn.metrics import accuracy_score #การคำนวณ ค่าความแม่นยำ (Accuracy) ของโมเดล โดยจะวัดสัดส่วนของการทำนายที่ถูกต้องเมื่อเปรียบเทียบกับการทำนายทั้งหมด

#----------------------------------------------------------------------------------------------
# ---------------------โหลดข่้อมูล---------------------
file_path = 'D:\CPE-433\Sleep_health_and_lifestyle_dataset.csv'
df = pd.read_csv(file_path)
#----------------------------------------------------------------------------------------------
# ---------------------เตรียม data---------------------
# df.head() #แสดงข้อมูล 5 ชุดแรก
# df.columns #แสดงชื่อคอลัมน์
# df.isnull().sum()
#df.info() #แสดงค่าข้อมูลของแต่ละคอลัมน์ ว่าเป็นชนิดข้อมูลแบบไหน
#df.describe() #แสดงค่าเชิงสถิติ
#df.duplicated().sum() #ใช้เพื่อตรวจสอบแถวที่ซ้ำกันใน DataFrame โดยมันจะคืนค่าเป็นซีรีส์ของค่าบูลีน (True หรือ False) 
#(df.isna().sum()/len(df))*100#ใช้สำหรับคำนวณ เปอร์เซ็นต์ของค่า missing (NaN) ในแต่ละคอลัมน์ของ DataFrame ซึ่งช่วยให้เข้าใจว่าแต่ละคอลัมน์มีข้อมูลสูญหายมากน้อยเพียงใด
#df[df['Sleep Disorder'].isna()] #ใช้เพื่อ กรองและเลือกแถว จาก DataFrame df ที่คอลัมน์ 'Sleep Disorder' มีค่าเป็น NaN
#df['Sleep Disorder'].unique() #ใช้เพื่อ แสดงค่าเฉพาะ ทั้งหมดในคอลัมน์ 'Sleep Disorder' ของ DataFrame df โดยจะคืนค่าเป็นอาร์เรย์ที่ประกอบด้วยค่าที่ไม่ซ้ำกันในคอลัมน์นั้น รวมถึงค่า NaN หากมี
# df['Sleep Disorder'].fillna("No Sleep Disorder", inplace=True) #ใช้เพื่อ แทนที่ค่า NaN  ในคอลัมน์ 'Sleep Disorder' ด้วยค่า 'No Sleep Disorder' โดยทำการแก้ไข DataFrame ต้นฉบับ
df['Sleep Disorder'] = df['Sleep Disorder'].replace('NaN', 'No Sleep Disorder')
# print(df.info())
# print(df)
#----------------------------------------------------------------------------------------------
# ---------------------การหาค่าผิดปกติ---------------------

numeric_col = ['Age', 'Sleep Duration', 'Quality of Sleep', 'Physical Activity Level', 'Stress Level', 'Heart Rate', 'Daily Steps']

fig = px.box(df, y=numeric_col, title="Outlier Detection in Numeric Columns")
fig.show()
#----------------------------------------------------------------------------------------------
#วิเคราะห์ความสัมพันธ์ระหว่างคุณภาพการนอนหลับ, ระยะเวลาการนอนหลับ, และระดับความเครียด โดยแบ่งกลุ่มตามโรคนอนไม่หลับ

#Sleep duration vs Stress level
fig = px.scatter(df, x='Sleep Duration', y='Stress Level', color='Sleep Disorder', 
                 title='Stress Level vs. Sleep Duration by Sleep Disorder')
fig.show()

#Quality of sleep vs Heart rate
fig = px.scatter(df, x='Quality of Sleep', y='Heart Rate', color='Sleep Disorder', 
                 title='Heart Rate vs. Quality of Sleep by Sleep Disorder')
fig.show()
#----------------------------------------------------------------------------------------------
# ---------------------การสเกลข้อมูล---------------------
scaler = MinMaxScaler()
df[['Sleep Duration', 'Quality of Sleep', 'Stress Level', 'Heart Rate']] = scaler.fit_transform(df[['Sleep Duration', 'Quality of Sleep', 'Stress Level', 'Heart Rate']])
# print(df.head(5))

X = df[['Age', 'Sleep Duration', 'Quality of Sleep', 'Stress Level', 'Heart Rate']]  # ตัวแปร feature
y = df['Sleep Disorder']  # ตัวแปร target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) #30%/70%

#----------------------------------------------------------------------------------------------
# ---------------------การฝึกโมเดล---------------------
model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
# print(y_pred)

#----------------------------------------------------------------------------------------------
# ---------------------การประเมินผล---------------------

# วัดเปอร์เซ็นต์ของการทำนายที่ถูกต้องทั้งหมด
accuracy = accuracy_score(y_test, y_pred)
error_rate = 1 - accuracy
print(f'Error Rate: {error_rate} or {error_rate * 100} %')
print(f'Accuracy: {accuracy} or {accuracy * 100} %')


# In[ ]:




