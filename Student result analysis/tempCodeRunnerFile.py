subjects = ["Maths", "Physics", "Chemistry", "English", "Computer"]
for sub in subjects:
    topper = df.loc[df[sub].idxmax()]
    print(f"{sub}: {topper['Name']} (Marks: {topper[sub]})")

exam_topper = df.loc[df["Total"].idxmax()]
print(f"Name: {exam_topper['Name']}, Total: {exam_topper['Total']}, Avg: {exam_topper['Average']}")