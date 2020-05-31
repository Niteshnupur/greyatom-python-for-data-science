# --------------
# --------------
# Load the data
# Let's check which variable is categorical and which one is numerical so that you will get a basic idea about the features of the bank dataset.



# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 


# The path for the dataset has been stored in a variable path

# Create dataframe bank by passing the path of the file
 
#file1 = pd.read_csv(path)
#print(file1)

bank = pd.read_csv(path)
print(bank)


# Create the variable 'categorical_var' and using 'df.select_dtypes(include = 'object')' check all categorical values.

# print 'categorical_var'

categorical_var = bank.select_dtypes("object")

print(categorical_var)


# Create the variable 'numerical_var' and using 'df.select_dtypes(include = 'number')' check all categorical values.

# print 'numerical_var'


numerical_var = bank.select_dtypes("number")

print(numerical_var)







# --------------
# Something is Missing!
# Sometimes customers forget to fill in all the details or they don't want to share other details. Because of that, some of the fields in the dataset will have missing values. Now you have to check which columns have missing values and also check the count of missing values each column has. If you get the columns that have missing values, try to fill them.





# From the dataframe bank, drop the column Loan_ID to create a new dataframe banks


banks = bank.drop(["Loan_ID"] , axis = 1)

print(banks)


# To see the null values, use "isnull().sum()" function and print it.

banks.isnull().sum()


# Calculate mode for the dataframe banks and store in bank_mode

bank_mode = banks.mode().iloc[0]
print(bank_mode)


# Fill missing(NaN) values of banks with bank_mode and store the cleaned dataframe back in banks.

banks.fillna(bank_mode , inplace=True )
# print(banks)


# Check if all the missing values (NaN) are filled.

banks.isnull().sum()

print(banks.isnull().sum())





# --------------
# Loan Amount vs Gender
# Now let's check the loan amount of an average person based on 'Gender', 'Married', 'Self_Employed'. This will give a basic idea of the average loan amount of a person.


import numpy as np
import pandas as pd


# We will use previously created dataframe banks for this task.

# Generate a pivot table with index as 'Gender', 'Married', 'Self_Employed' and values as 'LoanAmount', using mean aggregation

pd.pivot_table(banks , index=['Gender', 'Married', 'Self_Employed'] , values=["LoanAmount"] , aggfunc=np.mean)



# Store the result in a variable called 'avg_loan_amount'

avg_loan_amount =pd.pivot_table(banks , index=['Gender', 'Married', 'Self_Employed'] , values=["LoanAmount"] , aggfunc=np.mean)

print(avg_loan_amount)






# --------------
# Loan Approval vs Employment
# Now let's check the percentage of loan approved based on a person's employment type



# We will use the previously created dataframe banks for this task.

# Create variable 'loan_approved_se' and store the count of results where Self_Employed == Yes and Loan_Status == Y.

loan_approved_se = banks.loc[(banks["Self_Employed"]=="Yes")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_se)


# Create variable 'loan_approved_nse' and store the count of results where Self_Employed == No and Loan_Status == Y.

loan_approved_nse = banks.loc[(banks["Self_Employed"]=="No")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()

print(loan_approved_nse)



# Calculate the percentage of loan approval for self-employed people and store result in variable 'percentage_se'.

percentage_se = (loan_approved_se * 100 / 614)

percentage_se = percentage_se[0]

print(percentage_se)


# Calculate the percentage of loan approval for people who are not self-employed and store the result in variable 'percentage_nse'.

percentage_nse = (loan_approved_nse * 100 /614)
percentage_nse = percentage_nse[0]

print(percentage_nse)






# --------------
# Transform the loan tenure from months to years
# A government audit is happening real soon! So the company wants to find out those applicants with long loan amount term.





# Use "apply()" function to convert Loan_Amount_Term which is in months to a year and store the result in a variable 'loan_term'.

N = banks["Loan_Amount_Term"]

loan_term = banks["Loan_Amount_Term"].apply(lambda N: N/12)

print(loan_term)


# Find the number of applicants having loan amount term greater than or equal to 25 years and store them in a variable called 'big_loan_term'.


#big_loan_term = (N>=25).astype(int)
#big_loan_term = len(list(big_loan_term))
#print(big_loan_term)

big_loan_term=[]
for n in loan_term:
    if n>=25:
        big_loan_term.append(n)
big_loan_term=len(list(big_loan_term))
print(big_loan_term)






# --------------
# Income/ Credit History vs Loan Amount
# Now let's check the average income of an applicant and the average loan given to a person based on their income.




import numpy as np
import pandas as pd


# Groupby the 'banks' dataframe by Loan_Status and store the result in a variable called 'loan_groupby'

loan_groupby = banks.groupby(["Loan_Status"])
print(loan_groupby)


# Subset 'loan_groupby' to include only ['ApplicantIncome', 'Credit_History'] and store the subsetted dataframe back in 'loan_groupby'

loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']
print(loan_groupby)



# Then find the mean of 'loan_groupby' and store the result in a new variable 'mean_values'


mean_values = loan_groupby.mean()

print(mean_values)












