import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"c:\Users\asus\OneDrive\Desktop\heart_disease_proj\heart.csv")

# find and fill the Nan values with the mode value 
number_of_Nan = df.isna().sum()
null_values = df["Thal"].isna()
mode_Thal = df["Thal"].mode()[0]
new_column = df["Thal"].fillna(f"changed value:{mode_Thal}")

# find the remove duplicate values

number_of_dups = df.duplicated().sum() # no duplicated rows 

# ensure all columns have the correct data type

df["Sex"] = df["Sex"].replace(
    {1:"male" , 0:"female"}
)

df["Fbs"]= df["Fbs"].replace(

    {0:"False" , 1:"True"}
)

df["RestECG"]= df["RestECG"].replace(

    {0:"Normal" , 1:"ST-T wave abnormality" , 2:"Left ventricular hypertrophy"}
)

df["ExAng"] = df["ExAng"].replace(
    {0:"No" , 1:"Yes"}
)

df["Target"] = df["Target"].replace(
    {0:"False" , 1:"True" }
)
#as

columns = ["Age", "RestBP" , "Chol", "MaxHR", "Oldpeak" , "Slope", "Ca"]
# No outlier in Age column
# There are 8 outliers in RestBP but I will not remove them as they might be considered indicators of a heart disease case
# There are 5 outliers in Chol but I removed only four of them. That is, the outlier 394 is a very high cholestrol level but it might indicate a heart disease.

for col in columns:
    plt.figure(figsize = (5,4))
    df.boxplot(column = col)
    plt.title(f"{col}")
    plt.ylabel(col)
    plt.show()


for i in df["Chol"]:
    if i > 360:
        print(i)
        






        
