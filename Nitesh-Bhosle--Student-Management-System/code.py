# --------------
# --------------
# Code starts here

import pandas as pd
import numpy as np

class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
print(class_1)
type(class_1)


class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']
print(class_2)
type(class_2)

new_class = class_1+class_2
print(new_class)


new_class.append('Peter Warden')
print(new_class)

new_class.pop(5)
print(new_class)









# Code ends here


# --------------
# Code starts here

courses={"Math":65 , "English":70 , "History":80,"French":70,"Science":60}
print(courses) 
type(courses)

total = 65+70+80+70+60
print(total)

percentage = 345/500*100
print(percentage)

# Code ends here


# --------------
# Code starts 

mathematics = {"Geoffrey Hinton":78 , "Andrew Ng":95 , "Sebastian Raschka":65 ,
            "Yoshua Benjio":50 , "Hilary Mason":70 , "Corinna Cortes":66 , 
            "Peter Warden":75        } 

print(mathematics)
type(mathematics)


max_marks_scored = max(courses,key = courses.get)
print (max_marks_scored)


topper = max(mathematics,key=mathematics.get)
print(topper)

# Code ends here  


# --------------
# Given string
topper = 'andrew ng'


print(topper)


first_name , last_name = topper.split()

print(first_name)
print(last_name)


full_name = last_name+" "+first_name
print(full_name)


certificate_name = full_name.upper()
print(certificate_name)

# Code starts here



# Code ends here



# Create the Dictionary



# Slice the dict and stores  the all subjects marks in variable


# Store the all the subject in one variable `Total`

# Print the total

# Insert percentage formula

# Print the percentage




# Create the Dictionary
 



# Given string


# Create variable first_name 

# Create variable Last_name and store last two element in the list

# Concatenate the string

# print the full_name

# print the name in upper case

# Code ends here


