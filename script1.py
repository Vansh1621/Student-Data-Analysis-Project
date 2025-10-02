import mysql.connector, matplotlib.pyplot as plt,pandas as pd, numpy as np
from faker import Faker
import random

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "school"
)
cursor = conn.cursor()
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS students(
    RollNo INT PRIMARY KEY,
    Name VARCHAR(50),
    Maths INT,
    Physics INT,
    Chemistry INT,
    English INT,
    Computer INT,
    Gender VARCHAR(10)
)
""")
fake = Faker()
Faker.seed(0)
random.seed(0)

num_students = 100
data = []

for roll in range(1,num_students+1):
    name = fake.first_name()
    marks = [random.randint(50,100) for _ in range(5)]
    gender = random.choice(["M","F"])
    row = (roll , name ,marks[0],marks[1],marks[2],marks[3],marks[4],gender)
    data.append(row)

cursor.execute("DELETE FROM students")
cursor.executemany("""
INSERT INTO students (RollNo, Name, Maths, Physics, Chemistry, English, Computer, Gender)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
""", data)
conn.commit()

df = pd.read_sql("SELECT * FROM students",conn)

df["Total"] = df.iloc[:,2:7].sum(axis = 1)
df["Average"] = np.round(df["Total"]/5,2)
# print(df)
subjects = ["Maths","Physics", "Chemistry","English", "Computer"]
for sub in subjects:
    topper = df.loc[df[sub].idxmax()]
    print(f"Subject: {sub}, Topper: {topper["Name"]}, Average: {topper[sub]}")

exam_topper = df.loc[df["Average"].idxmax()]
print(f"Exam_Topper: {exam_topper["Name"]}, Average: {exam_topper["Average"]}")


plt.bar(df["Gender"], df["Average"], color="skyblue")
plt.xlabel("Gender")
plt.ylabel("Average Marks")
plt.title("Gender Based Average")

plt.show()


df[subjects].mean().plot(kind="line", marker="o", color="red")
plt.title("Subject-wise Class Average")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.show()

df["Gender"].value_counts().plot.pie(autopct="%1.1f%%", colors=["pink","lightblue"])
plt.title("Gender Distribution")
plt.show()
