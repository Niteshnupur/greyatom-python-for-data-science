# --------------
# Loan Status
# Loan Status
# Let's start with the simple task of visualizing the company's record with respect to loan approvals.

#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# The path to the dataset has been stored in a variable path
# Load the dataframe using pd.read_csv() and store the dataframe in a variable called data.

data = pd.read_csv(path)
print(data)



# Save the value counts of Loan_Status in a variable called loan_status using value_counts()

loan_status = data["Loan_Status"].value_counts()
print(loan_status)


# Plot a bar graph of loan_status

loan_status.plot(kind= "bar" , figsize=(10,10))

plt.title('visualizing the companys record with respect to loan approvals')

plt.xlabel('Loan Status of approval')

plt.ylabel('VALUES')

plt.show()




#Code starts here


# --------------
# Everyone needs money
# Everyone needs money
# The company provides financial assistance across the different regions of the country. One interesting statistic that stakeholders want to see is the loan approval distribution across the regions.


#Code starts here

# Group the 'data' dataframe by Property_Area and Loan_Status and store it in a variable called 'property_and_loan'

property_and_loan = data.groupby(["Property_Area" , "Loan_Status"]).size().unstack()

print(property_and_loan)


# Use the .size() method on 'property_and_loan' and then use .unstack() and save it back to 'property_and_loan'

property_and_loan = data.groupby(["Property_Area" , "Loan_Status"]).size().unstack()

print(property_and_loan)


# Plot an unstacked bar plot of property_and_loan (It is similar to creating a stacked bar plot except change the parameter 'stacked' to False)

property_and_loan.plot(kind="bar" , stacked = False , figsize=(20,20))

plt.xlabel("Property Area")

plt.ylabel("Loan Status")

plt.xticks(rotation=45)

plt.show()






# --------------
# Expensive Education
# Expensive Education
# Higher education has always been an expensive endeavour for people but it results in better career opportunities and stability in life. But does higher education result in a better guarantee in issuing loans?


#Code starts here

# Group the 'data' dataframe by Education and Loan_Status and store it in a variable called 'education_and_loan'

education_and_loan = data.groupby(["Education" , "Loan_Status"])

print(education_and_loan)



# Use the .size() method on 'education_and_loan' and then use .unstack() and save it back to 'education_and_loan'


education_and_loan = data.groupby(["Education" , "Loan_Status"]).size().unstack()

print(education_and_loan)


# Plot an stacked bar plot of education_and_loan

education_and_loan.plot(kind="bar" , figsize=(20,20))



# Name the x-axis as Education Status

plt.xlabel("Education Status")


# Name the y-axis as Loan Status

plt.ylabel("Loan Status")


# Rotate the labels of x-axis by 45o

plt.xticks(rotation=45)



plt.show()





# --------------
# Smarter and Richer?
# Smarter and Richer?
# After seeing the loan status distribution, let's check whether being graduate or not also leads to different loan amount distribution by plotting an overlapping density plot of two values

#Code starts here


# Create a dataframe called 'graduate' which is a subset of 'data' dataframe with the condition "data['Education'] == 'Graduate'"

graduate = pd.DataFrame(data[data["Education"]=="Graduate"])
print(graduate)

#graduate=data[data['Education']=='Graduate']
#print(graduate)


# Create a dataframe called 'not_graduate' which is a subset of 'data' dataframe with the condition "data['Education'] == 'Not Graduate'"

not_graduate = pd.DataFrame(data[data["Education"]=="Not Graduate"])
print(not_graduate)





# Plot a density plot LoanAmount of 'graduate' dataframe using "Series.plot()" and pass the parameter kind='density' and label='Graduate'

graduate["LoanAmount"].plot(kind="density" , label="Graduate" , figsize=(20,20))


# Do the same for LoanAmount of 'not_graduate' dataframe but with label='Not Graduate'


not_graduate["LoanAmount"].plot(kind="density" , label="Not_graduate" , figsize=(20,20))




#Code ends here

#For automatic legend display
plt.legend()


# --------------
# Income vs Loan
# Income vs Loan
# For any financial institution to be successful in its loan lending system, there has to be a correlation between the borrower's income and loan amount he is lent. Let's see how our company fares in that respect:

#Code starts here

# Create three subplots with (nrows = 3 , ncols = 1) and store it in variable's fig ,(ax_1,ax_2,ax_3)

fig ,(ax_1,ax_2,ax_3) = plt.subplots(nrows = 3 , ncols = 1)


# Since both are continuous variables, plot scatter plot between 'ApplicantIncome' and LoanAmount using ax_1. Set axis title as Applicant Income


ax_1.scatter(data["CoapplicantIncome"] , data["LoanAmount"])

ax_1.set(title="Applicant Income")


# Plot scatter plot between 'CoapplicantIncome' and LoanAmount using ax_2. Set axis title as Coapplicant Income


ax_2.scatter(data["CoapplicantIncome"] , data["LoanAmount"])

ax_2.set(title="Coapplicant Income")




# Create a new column in the dataframe called 'TotalIncome' which is a sum of the values of columns ApplicantIncome and CoapplicantIncome


data["TotalIncome"] = data["ApplicantIncome"] + data["CoapplicantIncome"]




# Plot scatter plot between 'TotalIncome' and LoanAmount using ax_3. Set axis title as Total Income

ax_3.scatter(data["TotalIncome"] , data["LoanAmount"])

ax_3.set(title="Total Income")



