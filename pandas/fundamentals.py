import pandas as pd

df1 = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

# print(df1) # prints the data frame
# print(df1['Age']) # prints only the age column

pd.Series([45, 23, 109], name='Age')

age = df1.describe()
print(age)

# ------------------------------------------

data = pd.read_csv('./pandas/data.csv')
df = pd.DataFrame(data)

# print(df)
# print(df.dtypes) // prints all datatypes of columns of the dataframe

# print(df.info) prints out the technical information about the dataframe

# ---------------------------------------------------------------------------------------
# SELECTING SUBSETS OF A DATAFRAME




