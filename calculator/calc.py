def add(num1 ,num2):
    return num1 + num2

def sub(num1 ,num2):
    return num1 - num2

def div(num1 ,num2):
    return num1 / num2

def mul(num1 ,num2):
    return num1 * num2

print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")

select = int(input("Select operations form 1, 2, 3, 4 :"))

number_1 = int(input("First number: "))
number_2 = int(input("Second number: "))

if(select == 1):
        print(number_1, "+", number_2, "=",
                    add(number_1, number_2))
        
if(select == 2):
        print(number_1, "-", number_2, "=",
                    sub(number_1, number_2))

if(select == 3):
        print(number_1, "*", number_2, "=",
                    mul(number_1, number_2))
        
if(select == 4):
        print(number_1, "/", number_2, "=",
                    div(number_1, number_2))
        
    
input("Press ENTER to leave")