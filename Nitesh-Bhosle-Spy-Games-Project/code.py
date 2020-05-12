# --------------
# --------------
##File path for the file 
file_path 
print(file_path)

def read_file(path):
    # Opens the file associated with the 'path' in the read-only mode ('r') and store it in a variable file
    file = open(path, "r")
    # Reads the content(first line) of the file and stores it in a variable called 'sentence'
    sentence = file.readline()
    # Closes the file
    file.close()
    # Returns 'sentence'
    return sentence

# Call the function "read_file()" with 'file_path' as input parameter and store the result in a variable called 'sample_message'
sample_message = read_file(file_path)

# Print the 'sample_message'
print(sample_message)


# --------------
#Code starts here
file_path_1
print(file_path_1)

file_path_2
print(file_path_2)

message_1 = read_file(file_path_1)
print(f'Message in Text File M1 is : {message_1}')
message_2 = read_file(file_path_2)
print(f'Message in Text File M2 is : {message_2}')

def fuse_msg(message_a, message_b):
    quotient = int(message_b)//int(message_a)
    return str(quotient)


secret_msg_1 = fuse_msg(message_1,message_2)
print("--"*40)
print(f'Secret Message from File 1 and File 2 is : {secret_msg_1}')






# --------------
#Code starts here

file_path_3
print(file_path_3)

message_3 = read_file(file_path_3)

print(f'Message in Text File file.txt is : {message_3}')


# Create a function substitute_msg() that takes message_c as a parameter 
def substitute_msg(message_c):
    # Creates a new variable 'sub' and in it stores:
    #'Army General' if message_c is 'Red'
    if message_c == "Red":
        sub = "Army General"
    #'Data Scientist' if message_c is 'Green'
    elif message_c == "Green":
        sub = "Data Scientist"
     #'Marine Biologist' if message_c is 'Blue'
    else:
        sub = "Marine Biologist"
    # Returns 'sub'
    return sub



secret_msg_2 = substitute_msg(message_3)
print("--"*40)
print(f'Secret Message from File 3: {secret_msg_2}')


# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

print(file_path_4)

print(file_path_5)

message_4 = read_file(file_path_4)
message_5 = read_file(file_path_5)

print(f'Message in Text File file.txt_4 is : {message_4}')
print(f'Message in Text File file.txt is_5 : {message_5}')


def compare_msg(message_d, message_e):
    #Breaks down the sentences in message_d & message_e into words using split() function
    #stores them in a_list & b_list respectively
    a_list = list(message_d.split())
    b_list = list(message_e.split())
    # Stores all the words that are there in a_list but not in b_list in a new list called c_list
    c_list = list([i for i in a_list if not i in b_list])
    # Combines the words of c_list back to a sentence using join() and stores it in a variable called final_msg and returns it
    final_msg = " ".join(c_list)
    # return final_msg
    return final_msg



#Call the function "compare_msg()" with 'message_4' & 'message_5' and store the result of it in a variable called 'secret_msg_3'

secret_msg_3 = compare_msg(message_4, message_5)
print("--"*40)
print(f'Secret Message from File 4 and File 5 is : {secret_msg_3}')

#Code starts here







# --------------
#Code starts here

file_path_6
print(file_path_6)

# Call the function read_file() for file_path_6 and store its message sentence in variables message_6

message_6 = read_file(file_path_6)
print(message_6)


##### creating the function
## Write a function extract_msg() that :
## Takes message_f as a parameter

def extract_msg(message_f):
    # Breaks down the sentence in message_f into words and stores them in a_list
    a_list = list(message_f.split())
    # Creates a lambda function called even_word with the condition that will return true if length of x (lambda function variable) is even
    even_word = lambda x : len(x)%2==0
    # Implements filter() function with function parameter as even_word and sequence parameter as a_list and stores the result of it in a variable called b_list
    b_list = list(filter(even_word, a_list))
    # Combines the words of b_list back to a sentence and stores it in a variable called final_msg and returns it    
    final_msg = " ".join(b_list)
    # returns final_msg
    return final_msg



# Call the function "extract_msg()" with 'message_6' and store the result of it in a variable called 'secret_msg_4'
secret_msg_4 = str(extract_msg(message_6))
print("--"*100)
print(f'Secret Message from File file.txt_6 : {secret_msg_4}')





# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


final_path= user_data_dir + '/secret_message.txt'


print(message_parts)

print(final_path)


# Create  a function write_file() that takes secret_msg and path as parameters
def write_file(secret_msg, path):
    # Open the file mentioned in the path in a+ ( a+ : Opens a file for both appending and reading ) mode
    file = open(path, "a+")
    # Writes the content of the secret_msg in the above opened file
    file.writelines(secret_msg)
    # Closes the file
    file.close()


# Call the function "write_file()" with 'secret_msg' and 'final_path'
write_file(message_parts, final_path)

# Print the content of the 'secret_msg' so you can also see the message
secret_msg = " ".join(message_parts)
print(secret_msg)

#Code starts here


