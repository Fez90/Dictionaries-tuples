pol_eng_dictionary = {
    "kwiat": "flower",
    "woda": "water",
    "gleba": "soil"
    }

item_1 = pol_eng_dictionary["woda"]    # ex. 1
print(item_1)    # outputs: soil

item_2 = pol_eng_dictionary.get("kwiat")
print(item_2)    # outputs: water

pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

pol_eng_dictionary["zamek"] = "lock"
item = pol_eng_dictionary["zamek"]    
print(item)  # outputs: lock

phonebook = {}    # an empty dictionary

phonebook["Adam"] = 3456783958    # create/add a key-value pair
print(phonebook)    # outputs: {'Adam': 3456783958}

del phonebook["Adam"]
print(phonebook)    # outputs: {}

# pop and update method
pol_eng_dictionary = {"kwiat": "flower"}

pol_eng_dictionary.update({"gleba": "soil"})
print(pol_eng_dictionary)    # outputs: {'kwiat': 'flower', 'gleba': 'soil'}

pol_eng_dictionary.popitem()
print(pol_eng_dictionary)    # outputs: {'kwiat': 'flower'}

d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    # Write your code here.
    d3.update(item)
    
print(d3)

colors = (("green", "#008000"), ("blue", "#0000FF"))

# Write your code here.
colors_dictionary = dict(colors)

print(colors_dictionary)

for key,value in colors_dictionary.items():
    print(key,value)

while True:
    try:
        number = int(input("Enter an integer number: "))
        print(number/2)
        break
    except:
        print("Warning: the value entered is not a valid number. Try again...")

while True:
    try:
        number = int(input("Enter an int number: "))
        print(5/number)
        break
    except (ValueError, ZeroDivisionError):
        print("Wrong value or No division by zero rule broken.")
    except:
        print("Sorry, something went wrong...")

def checkio(array: list) -> int:
    """
        sums even-indexes elements and multiply at        the last
    """
    for i in array:
        print(i.index())

def max_digit(number: int) -> int:
    # your code here
    
    digits = list(str(number))
    
    int_list = []
    
    for i in digits:
        i = int(i)
        int_list.append(i)
        

    return max(int_list)
        

print(max_digit(0))


def is_all_upper(text: str) -> bool:
    # your code here
    if len(text) <= 0:
        if text is text.isalnum():
            return False
    
    if text == text.upper():
        return True
    else:
        return False

print(is_all_upper(""))

