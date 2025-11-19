import pandas as pd

df = pd.DataFrame(
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

# print(df) # prints the data frame
# print(df['Age']) # prints only the age column

pd.Series([45, 23, 109], name='Age')

age = df.describe()
print(age)

# ------------------------------------------

data = pd.read_csv('./pandas/data.csv')
df = pd.DataFrame(data)

# print(df)
# print(df.dtypes) // prints all datatypes of columns of the dataframe

