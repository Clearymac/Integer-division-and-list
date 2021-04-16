#LIST RETARRD
list = ['Evi', 'Madeleine', 'Cool guy', 'Kelsey', 'Cayden', 'Hayley', 'Darian']

#sorts and prints the list
list.sort()
print('Sorted list:', list)

name = input("What is your name? ")

if name in list:
    print("Oh senpai! that name is already in the list asdahasdhahkshldgakshd uwu")
else:
    replace = input("would you like to add your name to the list? ")
    replace.lower()
    if replace == "no":
        print("OK stinker")
    elif replace == "yes":
        list += name
        print(list)
