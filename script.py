# question 1
# a)
my_name = "katerina"

# b)
print(len(my_name))

# c)
print(my_name.count("a")) # str.count counts the number of times a character appears in a string

# question 2
my_list = [1, 5, "4", "six", 3.14]

# a)
for value in my_list:
    number = int(value)
    print(number) 
#raises ValueError: invalid literal for int() with base 10: 'six'

for value in my_list:
    try:
        number = int(value)
        print(number)
    except ValueError:
        print(f"Skipping invalid value: {value}") 
# starting with for loop ensures that the loop continues after invalid value

# b)
def clean_list(list):
    cleaned = []
    for value in list:
        try:
            number = int(value)
            print(number)
            cleaned.append(number)
        except ValueError:
            print(f"Skipping invalid value: {value}") 
    return cleaned

new_list = clean_list(my_list)
print(new_list)

# c)
for i in range(len(new_list)):
    if i == 0:
        print(new_list[i] + new_list[i+1]) # for position 0, calculate sum of position 0 and position 1
    elif i == len(new_list)-1: # for position except the last position in the list, sum of both neighbors
        print(new_list[i-1] + new_list[i])
    else:
        print(new_list[i-1] + new_list[i] + new_list[i+1])
