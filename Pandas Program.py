import pandas as pd

df = pd.DataFrame({
    "name": ["Hamza", "Ali", "Taha"],
    "age": [12, 13, 14],
    "city": ["Karachi", "Lahore", "Islamabad"],   
})    

# print(df[df["city"] == "Karachi"])
# print(df["age"].mean())
# print(df.loc[df["age"].idxmax(), "name"])

# input("Press Enter to continue...")

# print("\n")

# df = pd.read_csv("students_messy.csv")
# print(df.isnull().sum())
# print(df.duplicated().sum())
# print(df["city"].unique())
# print(df.dtypes)

df = pd.read_csv("students_messy.csv")
df = df.drop_duplicates()
df = df.dropna(subset=["name"])
df["score"] = df["score"].fillna(df["score"].median())
df["city"] = df["city"].str.strip().str.title()
df["age"] = pd.to_numeric(df["age"], errors="coerce")
print(df.shape, df["city"].unique().tolist(), "\n")

print(df.shape, "\n")