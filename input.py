
x = input("Give An Input(number/lowercase/uppercase/special_char):")

if x>='0' and x<='9':
    print("Given input is a Digit")
elif x>='A' and x<='Z':
    print("Given input is a Upper Case Character")
elif x>='a' and x<='z':
    print("Given input is a Lower Case Character")     
else: 
    print("Given input is a special Character")
