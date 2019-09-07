# --------------
##File path for the file 
file_path

#Code starts here
def read_file(path):
    file = open(path,"r")
    sentence = file.read()
    file.close()
    return sentence

sample_message = read_file(file_path)
print(sample_message)








# --------------
#Code starts here

def read_file(path1,path2):
    file1 = open(path1,"r")
    file2 = open(path2,"r")

    message_1 = file1.read()
    message_2 = file2.read()
    print(message_1,message_2)
    return (message_1,message_2)

message = read_file(file_path_1,file_path_2)

message_1 = (message[0])
message_2 = (message[1])
a = int(message_1)
b = int(message_2)
def fuse_msg(message_a,message_b):

    quotient = message_b//message_a
    return str(quotient)
secret_msg_1 = fuse_msg(a,b)
print(secret_msg_1)







# --------------
#Code starts here
def read_file(file_path):
    file1 = open(file_path,"r")
    message_3 = file1.read()
    return message_3

message = read_file(file_path_3)
message_3 = str(message)
print(message_3)
def substitute_msg(message_c):
    if message_c == "Red" :
        sub = 'Army General'
    elif message_c == "Green" :
        sub = 'Data Scientist'
    elif message_c == "Blue" :
        sub = 'Marine Biologist'

    return sub

secret_msg_2 = substitute_msg(message_3)
print(secret_msg_2)






# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here
def read_file(path4,path5):
    file4 = open(path4,"r")
    file5 = open(path5,"r")
    message_4 = file4.read()
    message_5 = file5.read()
    return(message_4,message_5)
message = read_file(file_path_4,file_path_5)
message_4 = str(message[0])
message_5 = str(message[1])
print(message_4,message_5)

def compare_msg(message_d,message_e):
    a_list = message_d.split()
    b_list = message_e.split()
    c_list = [i for i in a_list if not i in b_list]
    final_msg = " ".join(c_list)
    return final_msg
secret_msg_3 = compare_msg(message_4,message_5)
print(secret_msg_3)






# --------------
#Code starts here
def read_file(path):
    file1 = open(path,"r")
    message_6 = file1.read()
    return message_6
message_6 = str(read_file(file_path_6))
print(message_6)

def extract_msg(message_f):
    a_list = message_f.split()
    even_word = lambda x: len(x)%2==0
    b_list = filter(even_word,a_list)
    final_msg = " ".join(b_list)
    return final_msg
secret_msg_4 = extract_msg(message_6)
print(secret_msg_4)


# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


final_path= user_data_dir + '/secret_message.txt'

#Code starts here
secret_msg = " ".join(message_parts)
def write_file(secret_msg,path):
    file1 = open(path,"a+")
    file1.write(secret_msg)
    file1.close()
write_file(secret_msg,final_path)
print(secret_msg)


