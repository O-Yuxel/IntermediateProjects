import pandas as pd

df = pd.read_csv("student-mat.csv", sep=";")


print("----------PART 1----------")

first5_rows = df.head()
row_count = df.shape[0]
column_count = df.shape[1]
columns_names = df.columns
columns_types = df.dtypes
statistics = df.describe()

print("First 5 rows of UCI Dataframe:\n", first5_rows, sep="")
print("Count of rows:", row_count)
print("Count of columns", column_count)
print("Column names:\n",columns_names, sep="")
print("Column types:\n",columns_types, sep="")
print("Statistics of UCI Dataframe:\n", statistics, sep="")


print("\n----------PART 2----------")

is_has_nan = df.isna().sum().sum()
is_has_duplicate = df.duplicated().sum()
number_unique = df.nunique()

print("Count of NaN:", is_has_nan)
print("Count of duplicate:", is_has_duplicate)
print("Count of different values:\n", number_unique, sep="")


print("\n----------PART 3----------")

mean_age = df["age"].mean()
min_age = df["age"].min()
max_age = df["age"].max()
count_girl = df["sex"].value_counts()["F"]
count_school = df["school"].value_counts()
count_adress = df["address"].value_counts()

print("Mean value of age: ", mean_age)
print("Minimum value of age: ", min_age)
print("Maximum value of age: ", max_age)
print("Count of girls: ", count_girl)
print("Count of schools:\n", count_school, sep="")
print("Count of adresses:\n", count_adress, sep="")


print("\n----------PART 4----------")

mean_g1 = df["G1"].mean()
mean_g2 = df["G2"].mean()
mean_g3 = df["G3"].mean()
max_g3 = df["G3"].max()
min_g3 = df["G3"].min()
fewer10_g3 = (df["G3"] < 10).sum()
greater15_g3 = (df["G3"] > 15).sum()
correlation_g = df[["G1", "G2", "G3"]].corr()

print("Mean value of G1: ", mean_g1)
print("Mean value of G2: ", mean_g2)
print("Mean value of G3: ", mean_g3)
print("Maximum value of G3: ", max_g3)
print("Minimum value of G3: ", min_g3)
print("The number of students with fewer than 10 G3 grades: ", fewer10_g3)
print("The number of students with greater than 15 G3 grades: ", greater15_g3)
print("Correlation of G Notes:\n", correlation_g, sep="")


print("\n----------PART 5----------")

sex_g3_group = df.groupby("sex")["G3"].agg("mean")
school_g3_group = df.groupby("school")["G3"].agg("mean")
studytime_g3_group = df.groupby("studytime")["G3"].agg("mean")

print("Sex that grouped by G3 notes:\n", sex_g3_group, sep="")
print("School that grouped by G3 notes:\n", school_g3_group, sep="")
print("Studytime that grouped by G3 notes:\n", studytime_g3_group, sep="")


print("\n----------PART 6----------")

correlation_triple = df[["freetime","health","goout"]].corrwith(df["G3"])
print("A fex correlation with G3:\n", correlation_triple, sep="")


print("\n----------PART 7----------")

best10_students = df.sort_values(by="G3", ascending=False).head(10)
istatistics_best_students = best10_students[["school" ,"sex", "age", "studytime", "absences", "G1", "G2", "G3"]]
print("The importants istatistics of best 10 students:\n", istatistics_best_students, sep="")


print("\n----------PART 8----------")

print("Analysis 1: The number of females greater than males.")
print("Analysis 2: Young ages are more common.")
print("Analysis 3: G1, G2 and G3 have strong correlation.")
print("Analysis 4: Males are more successful than females.")
print("Analysis 5: Studying for 3 hours for the G3 exam yields better results than studying for 4 hours.")