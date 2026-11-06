import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv") # It means that we are reading a CSV file named "students.csv" and storing its contents in a DataFrame called df. A DataFrame is a two-dimensional, size-mutable, and heterogeneous tabular data structure provided by the pandas library.

# df["score"].hist(bins = [40, 50, 60, 70, 80, 90, 100]) # What it does is it creates a histogram of the score column with bins ranging from 40 to 100 in increments of 10. This allows us to visualize the distribution of scores among the students.

# plt.xlabel("Score") # Sets the label for the x-axis
# plt.ylabel("Frequency") # Sets the label for the y-axis
# plt.show() # Displays the histogram plot

# print("\n")

# print(df["city"].value_counts() ["Lahore"], "\n") # This line of code counts the number of occurrences of each unique value in the "city" column of the DataFrame df. It then retrieves the count for the city "Lahore" and prints it. The value_counts() method returns a Series containing counts of unique values, and by indexing it with ["Lahore"], we get the specific count for that city.
# print(df.sort_values("score", ascending = False).head(3), "\n") # Top 3 students with the highest scores
# print((df["score"] >= 50).sum(), "\n") # Number of students with a score of 50 or higher
# print(df[["score", "hours"]].corr(), "\n") # Correlation between score and age

df["score_pct"] = df["score"] / 100
df["is_Karachi"] = (df["city"] == "Karachi").astype(int) # This line of code creates a new column in the DataFrame df called "is_Karachi". It checks each value in the "city" column to see if it is equal to "Karachi". If it is, the result is True; otherwise, it is False. The astype(int) method then converts these boolean values (True/False) into integers (1/0), where 1 represents that the city is Karachi and 0 represents that it is not. This new column can be useful for analysis or modeling purposes.
print(df[["name", "score_pct", "is_Karachi"]].head(3), "\n") # Displaying the first 3 rows of the DataFrame with the columns "name", "score_pct", and "is_Karachi" to show the new column's values.

