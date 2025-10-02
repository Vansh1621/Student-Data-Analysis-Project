import pandas as pd
import numpy as np
from faker import Faker
import random
n = 100
fake = Faker()
data = {
    "Roll no.": range(1,n+1,),
    "Name":  [fake.first_name() for _ in range(n)] ,
    "Maths":np.random.randint(40,100,n), 
    "Physics":np.random.randint(40,100,n),  
    "Chemistry": np.random.randint(40,100,n), 
    "English": np.random.randint(40,100,n), 
    "Computer": np.random.randint(40,100,n), 
}
df = pd.DataFrame(data)
df.to_csv("students.csv", index=False)
df = pd.read_csv("students.csv")
print (df.head())
marks = df[["Maths","Physics","Chemistry", "English", "Computer"]].values
df["Total"]= np.sum(marks,axis=1)
df["Average"] = np.mean(marks, axis=1)
df.to_csv("students.csv",index=False)
print("\nWith Total & Average:\n", df.head())
top_5 = df.sort_values(by="Total",ascending = False).head(5)

subjects = ["Maths", "Physics", "Chemistry", "English", "Computer"]
for sub in subjects:
    topper = df.loc[df[sub].idxmax()]
    print(f"{sub}: {topper['Name']} (Marks: {topper[sub]})")

exam_topper = df.loc[df["Total"].idxmax()]
print(f"Name: {exam_topper['Name']}, Total: {exam_topper['Total']}, Avg: {exam_topper['Average']}")
