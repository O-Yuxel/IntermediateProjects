import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

print("----------PART 1----------")

df = pd.read_csv("average-exposure-pm25-pollution.csv")

first5_row = df.head()

row_count = df.shape[0]
column_count = df.shape[1]

column_names = df.columns

numeric_columns = df.select_dtypes(include="number").columns
categorical_columns = df.select_dtypes(include=["category", "object"]).columns

country_count = df["Entity"].nunique()

range_of_years = str(df["Year"].min()) + " - " + str(df["Year"].max())

number_of_na = df.isna().sum().sum()
number_of_duplicates = df.duplicated().sum()

min_of_pm25 = df["PM2.5 air pollution, mean annual exposure (micrograms per cubic meter)"].min()
max_of_pm25 = df["PM2.5 air pollution, mean annual exposure (micrograms per cubic meter)"].max()
mean_of_pm25 = df["PM2.5 air pollution, mean annual exposure (micrograms per cubic meter)"].mean()


print("First 5 rows of Average Exposure", first5_row, "\n")
print("İnformations about Average Exposure")
df.info()

print("Column count of PM2.5 Dataframe:\n", column_count)
print("Row count of PM2.5 Dataframe:\n", row_count)

print("Column names of PM2.5 Dataframe:\n", column_names)

print("Numeric columns of PM2.5 Dataframe:\n", numeric_columns)
print("Categorical columns of PM2.5 Dataframe:\n", categorical_columns)

print("Total count of countries:\n", country_count)

print("The range of years that included on PM2.5 Dataframe:\n", range_of_years)

print("Count of missing value:\n", number_of_na)
print("Count of duplicates:\n", number_of_duplicates)

print("Minimum value of Air Pollution (micrograms per cubic meter):\n", min_of_pm25)
print("Maximum value of Air Pollution (micrograms per cubic meter):\n", max_of_pm25)
print("Mean value of Air Pollution (micrograms per cubic meter):\n", mean_of_pm25)


print("\n----------PART 2----------")

df = df.rename(columns= {"PM2.5 air pollution, mean annual exposure (micrograms per cubic meter)": "pm25",
                         "Year": "year",
                         "Entity": "country"})

print("Column names was succesfully changed!")


country_pm25_mean = df.groupby("country")["pm25"].mean()
top10_pm25_countries = country_pm25_mean.sort_values(ascending=False).head(10)
print("First 10 Highest air pollution countries:\n", top10_pm25_countries)


print("\n----------PART 3----------")

sns.set_theme()

g = sns.barplot(
        x=top10_pm25_countries.index,
        y=top10_pm25_countries.values
)

plt.title("Top 10 Highest Air Pollution Countries")
plt.xlabel("Countries")
plt.ylabel("Air Pollution")
plt.grid(True)

g.figure.text(
    0.98, 0.98,
    "Qatar has the highest average PM2.5 exposure in this dataset.\n" \
    "Pakistan is among the 10 countries with the highest average PM2.5 exposure.",
    ha="right",
    va="top",
    bbox=dict(boxstyle="round", alpha=0.8, color="black"),
    color="white"
)

plt.show()

print("Graph 1 was showed")


print("\n----------PART 4----------")

sns.set_theme()

countries = ["Turkey", "Norway", "Cameroon"]
filtred_df = df[df["country"].isin(countries)]

g = sns.lineplot(
        data=filtred_df,
        x="year",
        y="pm25",
        hue="country"
)

g.figure.text(
    0.98, 0.98,
    "Turkey consistently shows higher PM2.5 exposure than Norway throughout the observed period.",
    ha="right",
    va="top",
    bbox=dict(boxstyle="round", alpha=0.8, color="black"),
    color="white"
)


plt.title("Air Pollution Over Time")
plt.xlabel("Years")
plt.ylabel("Air Pollution")
plt.grid(True)

plt.show()

print("Graph 2 was showed")


print("\n----------PART 5----------")

sns.set_theme()

g = sns.histplot(
        x=country_pm25_mean.values,
        bins=15,
        kde=True
)

g.figure.text(
    0.98 ,0.98,
    "Air pollution is concentrated around a value of 20.",
    ha="right",
    va="top",
    bbox=dict(boxstyle="round", alpha=0.8, color="black"),
    color="white"
)

plt.title("Distribution of Average PM2.5 Exposure by Country")
plt.xlabel("Average PM2.5 Exposure")
plt.ylabel("Count")
plt.grid(True)

plt.show()

print("Graph 3 was showed")


print("\n----------PART 6----------")

sns.set_theme()

df["period"] = pd.cut(
    df["year"],
    bins=[float("-inf"), 2000, 2010, 2020, float("inf")],
    labels=["1990s","2000s","2010s", "2020s"]
)

g = sns.boxplot(
        data=df,
        x="period",
        y="pm25")

g.figure.text(
    0.98, 0.98,
    "2000s and 2010s have more outlier than other periods.\n" \
    "1990s median value higher than othe periods.",
    ha="right",
    va="top",
    bbox=dict(boxstyle="round", alpha=0.8, color="black"),
    color="white"
)

plt.title("pm 2.5 by Periods")
plt.xlabel("Periods")
plt.ylabel("Air Pollution")
plt.grid(True)


plt.show()

print("Graph 4 was showed")


print("\n----------PART 7----------")

sns.set_theme()

year_pm25_mean = df.groupby("year")["pm25"].mean()
print(year_pm25_mean)

sns.lineplot(
    x=year_pm25_mean.index,
    y=year_pm25_mean.values
)

sns.regplot(
    x=year_pm25_mean.index,
    y=year_pm25_mean.values,
    scatter=False
)

plt.text(
    0.98, 0.98,
    "PM2.5 exposure appears to decrease over time.",
    ha="right",
    va="top",
    bbox=dict(boxstyle="round", alpha=0.8, color="black"),
    color="white"
)

plt.title("Average PM2.5 Exposure Over Time")
plt.xlabel("Years")
plt.ylabel("Air Pollution")
plt.grid(True)

plt.show()

print("Graph 5 was showed.")


print("\n----------PART 8----------")

sns.set_theme()

top5_pm25_countries = country_pm25_mean.head()
print(top5_pm25_countries)
filtred_df2 = df[df["country"].isin(top5_pm25_countries.index)]
print(filtred_df2)

g = sns.relplot(
        data=filtred_df2,
        x="year",
        y="pm25",
        hue="country",
        col="period",
        kind="line"
)

g.figure.suptitle("PM2.5 Exposure Over Time")
g.set_axis_labels("Years", "Air Pollution")
g.figure.subplots_adjust(top=0.85)

plt.show()

print("Graph 6 was showed.")


print("\n----------PART 9----------")

sns.set_theme()

g = sns.FacetGrid(
        data=df,
        col="period"
)

g.map_dataframe(
    sns.histplot,
    x="pm25",
    bins=10
)

g.figure.text(
    0.98, 0.98,
    "It seems like 2000s pm2.5 exposure little bit higher than other periods.\n" \
    "PM2.5 exposure appears to have decreased slightly over the last 20 years.",
    ha="right",
    va="top",
    bbox=dict(boxstyle="round", alpha=0.8, color="black"),
    color="white"
)

g.figure.suptitle("Air Pollution Ranges Over Time")
g.set_axis_labels("Air Pollution", "Count")
g.figure.subplots_adjust(top=0.85)

plt.show()

print("Graph 7 was showed")