# # I want to creat a python program that filter your qestion and gives you a resinable answer
import math

print("--------------------------")
userInput = input("Enter a  calculation\n");


calculation = []; # This will contain the raw calculation
mathemetical_signs = ['+','-','*','/','x']

# This will filter the Numeric and the mathemetical signs from the User input
# This will check every value from the user input
for i in userInput: 
    if (i.isnumeric()):
        print(i,"is a number");
        calculation.append(int(i)); # Will cast (CONVERT) the user in put to an integer since input values are string

    elif (i in mathemetical_signs):
         #Converting the x in to computer multiplication sign
        if(i in mathemetical_signs): # Needs to be able to identify values for mathematical symbols whether you are using computer math or general math
            calculation.append(i)
        else: 
            i = "+"
            calculation.append(i)
         

    else:
        # This will catch anything which is not numeric or not used data
        print("--------------------------")
        print("is a not number")



 
# print("The original list : " + str(calculation))
 
 # Need to add more symboys for validation else it will skip filtering with a paticular value
result = []
temp_list = []
sign = []
for i in calculation:
    if i in mathemetical_signs:
        sign.append(i)
        result.append(temp_list)
        temp_list = []

    else:
        temp_list.append(i)
result.append(temp_list)
# print("The list after splitting by a value : " + str(result))
# print("Spreading Values",*result)

value_1 = result[0][0];
value_2 = result[1][0];

# print('Print test values')
# print(value_1)
# print(value_2)

#Filter Function which combans the values from each array
def filter_num_1(value_1):
    num_list = []
    # num_list = *value_1
    # print('Test')
    # print(*value_1)
    # print(num_1)
    # return type(num_1)
    

# filter_num_1(value_1)
# print("Testing the filter Function", filter_num_1(value_1)) 

# def f(x, y):
#     if y != 0:
#         a = math.floor(math.log10(y))
#     else:
#         a = -1

#     return int(x*10**(1+a)+y)

# num_1 = f(*value_1)
# num_2 = f(*value_2)

def calculate(sum_1,sum_2):
    if(sign[0] == '+'):
        print("Result of ",sum_1, sign[0], sum_2, "is ", sum_1 + sum_2);
    elif(sign[0] == '-'):
        print("Result of ",sum_1, sign[0], sum_2, "is ", sum_1 - sum_2);
    elif(sign[0] == '*'):
        print("Result of ",sum_1, sign[0], sum_2, "is ", sum_1 * sum_2);
    elif(sign[0] == '/'):
        print("Result of ",sum_1, sign[0], sum_2, "is ", sum_1 / sum_2);
    else:
        print("There was an issue ", sign);

calculate(value_1,value_2); # Need to add try block for when you divide by zero 
