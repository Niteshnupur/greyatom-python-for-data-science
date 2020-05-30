# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

print(data)


#Code starts here

# Append 'new_record' (given) to 'data' using "np.concatenate()" and store the new array in a variable called censu

# New record


new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

new_record = np.array(new_record)

print(new_record)

type(new_record)


census = np.concatenate((data , new_record))
print(census)





#We often associate the potential of a country based on the age distribution of the people residing there. We too want to do a simple analysis of the age distribution

# Create a new array called 'age' by taking only age column(age is the column with index 0) of 'census' array.

age = census[:,0]
print(age)

# Find the max age and store it in a variable called 'max_age'

max_age = np.max(age)
print(max_age)


# Find the min age and store it in a variable called 'min_age'.

min_age = np.min(age)
print(min_age)


# Find the mean of the age and store it in a variable called 'age_mean'.

age_mean = np.mean(age)
print(age_mean)


# Find the standard deviation of the age and store it in a variable called 'age_std'

age_std = np.std(age)
print(age_std)






# The constitution of the country tries it's best to ensure that people of all races are able   to live harmoniously. Let's check the country's race distribution to identify the minorities   so that the government can help them.



#Create four different arrays by subsetting 'census' array by Race column(Race is the column    with index 2) and save them in 'race_0','race_1', 'race_2', 'race_3' and 'race_4'              respectively  (Meaning: Store the array where 'race'column has value 0 in 'race_0', so on and so forth)

race = census[:,2]
print(race)

c_0, c_1, c_2, c_3, c_4 = race==0, race==1, race==2, race==3, race==4

race_0, race_1, race_2, race_3, race_4 = census[c_0], census[c_1], census[c_2], census[c_3], census[c_4]


# Store the length of the above created arrays in 'len_0', 'len_1','len_2', 'len_3' and 'len_4' respectively

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)


# Find out which is the race with the minimum no. of citizens

# Store the number associated with the minority race in a variable called 'minority_race'(For eg: if "len(race_5)" is the minimum, store 5 in 'minority_race' because that is the index of the race having the least no. of citizens )


minimum = min((len_0, len_1, len_2, len_3, len_4))
if minimum == len_0:
    minority_race = 0
elif minimum == len_1:
    minority_race = 1
elif minimum == len_2:
    minority_race = 2
elif minimum == len_3:
    minority_race = 3
elif minimum == len_4:
    minority_race = 4







# As per the new govt. policy, all citizens above age 60 should not be made to work more than 25 hours per week. Let us look at the data and see if that policy is followed.





#Create a new subset array called 'senior_citizens' by filtering 'census' according to age>60 (age is the column with index 0)

senior_citizens = census[census[:,0]>60]
print(senior_citizens)


# Add all the working hours(working hours is the column with index 6) of 'senior_citizens' and store it in a variable called 'working_hours_sum'

working_hours_sum = senior_citizens[:,6].sum()
print(working_hours_sum)


# Find the length of 'senior_citizens' and store it in a variable called 'senior_citizens_len'

senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)


# Finally find the average working hours of the senior citizens by dividing 'working_hours_sum' by 'senior_citizens_len' and store it in a variable called 'avg_working hours'.

# Print 'avg_working_hours' and see if the govt. policy is followed.

avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)


# # Our parents have repeatedly told us that we need to study well in order to get a good(read: higher-paying) job. Let's see whether the higher educated people have better pay in general.




# Create two new subset arrays called 'high' and 'low' by filtering 'census' according to education-num>10 and education-num<=10 (education-num is the column with index 1) respectively.

high = census[census[:,1]>10]
print(high)

low = census[census[:,1]<=10]
print(low)



#Find the mean of income column(income is the column with index 7) of 'high' array and store  it in 'avg_pay_high'. Do the same for 'low' array and store it's mean in 'avg_pay_low'.

avg_pay_high = np.mean(high[:,7])
print(avg_pay_high)

avg_pay_low = np.mean(low[:,7])
print(avg_pay_low)




# Our parents have repeatedly told us that we need to study well in order to get a good(read: higher-paying) job. Let's see whether the higher educated people have better pay in general.



# Create two new subset arrays called 'high' and 'low' by filtering 'census' according to education-num>10 and education-num<=10 (education-num is the column with index 1) respectively.

high = census[census[:,1]>10]
print(high)

low = census[census[:,1]<=10]
print(low)



#Find the mean of income column(income is the column with index 7) of 'high' array and store  it in 'avg_pay_high'. Do the same for 'low' array and store it's mean in 'avg_pay_low'.

avg_pay_high = np.mean(high[:,7])
print(avg_pay_high)

avg_pay_low = np.mean(low[:,7])
print(avg_pay_low)





