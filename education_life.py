import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("gapminder.csv")


print("----------PART 1----------")

row_count = df.shape[0]
column_count = df.shape[1]
numeric_columns = df.select_dtypes(include=["number"]).columns
categoric_columns = df.select_dtypes(include=["object", "category"]).columns
min_year = df["year"].min()
max_year = df["year"].max()
which_countries = pd.unique(df["country"])

print("Number of Rows: ", row_count)
print("Number of Columns: ", column_count)
print("The columns which numeric: ", numeric_columns)
print("The columns which categoric: ", categoric_columns)
print(f"Data is between {min_year} and {max_year} years.")
print("The countries in data:\n", which_countries, sep="")


print("\n----------PART 2----------")

number_nan = df.isna().sum()
number_duplicate = df.duplicated().sum()

print("Missing values:\n", number_nan, "\n", sep="")
print("Duplicate rows:\n", number_duplicate, sep="")


print("\n----------PART 3----------")

lifeExp_grouped = df.groupby("country")["lifeExp"].mean()
sorted_grouped = lifeExp_grouped.sort_values(ascending=False)
top10_lifeExp = sorted_grouped.head(10)

print(top10_lifeExp)


print("\n----------PART 4----------")

plt.figure()

plt.bar(top10_lifeExp.index, top10_lifeExp.values, color="blue")

plt.title("Top 10 Countries by Life Expectancy")
plt.xlabel("Countries")
plt.ylabel("Life Expectance")

plt.grid(True)
plt.xticks(rotation=0.75, color="blue")
plt.tight_layout()

plt.show()
print("Top 10 Countries by Life Expextancy was showed.")


print("\n----------PART 5----------")

maskTurkey = df["country"] == "Turkey"
Turkey_df = df[maskTurkey] 

maskUSA = df["country"] == "United States"
USA_df = df[maskUSA]

maskJapan = df["country"] == "Japan"
Japan_df = df[maskJapan]

plt.figure()

plt.plot(Turkey_df["year"], Turkey_df["lifeExp"], color="red", marker="*", label="Turkey")
plt.plot(USA_df["year"], USA_df["lifeExp"], color="blue", marker="+", label="USA")
plt.plot(Japan_df["year"], Japan_df["lifeExp"], color="gray", marker="o", label="Japan")

plt.title("Life Expextance Over Year")
plt.xlabel("Year")
plt.ylabel("Life Expextance")

plt.grid(True)
plt.tight_layout()
plt.legend()

plt.show()
print("Life Expextance Over Year was showed")


print("\n----------PART 6----------")

avrg_pop_lifeExp = df.groupby("country")[["pop", "lifeExp"]].mean()
print(avrg_pop_lifeExp)

plt.figure()

plt.scatter(avrg_pop_lifeExp["pop"], avrg_pop_lifeExp["lifeExp"], color="black", alpha=0.6)

plt.title("Scatter of Life Expectance by Population")
plt.xlabel("Average Population")
plt.ylabel("Average Life Expextance")

plt.text(
    0.98, 0.98,
    "Analysis: It seems like we have not\nstrong correlation between Average Population\nand Average Life Expectance.Because As\n population increases, life expextance does not\n appear to increase consistently.",
    transform=plt.gca().transAxes,
    ha="right",
    va="top",
    bbox=dict(boxstyle="round", alpha=0.8)
)

plt.grid(True)
plt.tight_layout()

plt.show()

print("Scatter of Life Expectance by Population was showed")


print("\n----------PART 7----------")

plt.figure()

plt.hist(avrg_pop_lifeExp["lifeExp"], bins=10, alpha=0.7)

plt.title("Distribution of Life Expectancy")
plt.xlabel("Average Life Expectancy")
plt.ylabel("Number of Countries")

plt.text(
    0.98, 0.98,
    "Analysis: We have 5 countries its life expextance under 40.75.\nAnalysis: The range with the highest number of countries is 72.5 – 76.5 ",
    transform=plt.gca().transAxes,
    ha="right",
    va="top",
    bbox=dict(boxstyle="round", alpha=0.8)
)

plt.grid(True)

plt.show()

print("Distribution of Life Expectancy was showed")


print("\n----------PART 8----------")

continents_grouped_by_lifeExp = df.groupby("continent")["lifeExp"].mean()

plt.figure()

plt.bar(continents_grouped_by_lifeExp.index, continents_grouped_by_lifeExp.values, color="green")

plt.title("Average life expextance by continents")
plt.xlabel("Continents")
plt.ylabel("Life Expextance")

plt.text(
    0.98, 0.98,
    "Analysis: Africa has least life expextance.\nAnalysis: Oceania has most life expextance.\nAnalysis: The difference between africa's and \noceania's life expextance is about  26 years.",
    transform=plt.gca().transAxes,
    ha="right",
    va="top",
    bbox=dict(boxstyle="round", alpha=0.8)
)

plt.grid(True)
plt.tight_layout()

plt.show()

print("Average life expextance by continents was showed")


print("\n----------PART 9----------")

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0][0].bar(top10_lifeExp.index, top10_lifeExp.values, color="blue")
axes[0][0].set_title("Top 10 Countries by Life Expectancy")
axes[0][0].set_xlabel("Countries")
axes[0][0].set_ylabel("Life Expectance")
axes[0][0].grid(True)

axes[0][1].plot(Turkey_df["year"], Turkey_df["lifeExp"], color="red", marker="*", label="Turkey")
axes[0][1].plot(USA_df["year"], USA_df["lifeExp"], color="blue", marker="+", label="USA")
axes[0][1].plot(Japan_df["year"], Japan_df["lifeExp"], color="gray", marker="o", label="Japan")
axes[0][1].set_title("Life Expextance Over Year")
axes[0][1].set_xlabel("Year")
axes[0][1].set_ylabel("Life Expextance")
axes[0][1].grid(True)
axes[0][1].legend()

axes[1][0].scatter(avrg_pop_lifeExp["pop"], avrg_pop_lifeExp["lifeExp"], color="black", alpha=0.6)
axes[1][0].set_title("Scatter of Life Expectance by Population")
axes[1][0].set_xlabel("Average Population")
axes[1][0].set_ylabel("Average Life Expextance")
axes[1][0].grid(True)

axes[1][1].hist(avrg_pop_lifeExp["lifeExp"], bins=10, alpha=0.7)
axes[1][1].set_title("Distribution of Life Expectancy")
axes[1][1].set_xlabel("Average Life Expectancy")
axes[1][1].set_ylabel("Number of Countries")
axes[1][1].grid(True)

fig.tight_layout()

plt.show()

print("Subplot was showed")