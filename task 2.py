#LIST RETARRD
list = ['Evi', 'Madeleine', 'Cool guy', 'Kelsey', 'Cayden', 'Hayley', 'Darian']

#sorts and prints the list
list.sort()
print('Sorted list:', list)

#asks the user to input their name
name = input("What is your name? ")
name = name.title()


#checks if name is in list and gives option to add to list
if name in list:
    print("Oh senpai! that name is already in the list asdahasdhahkshldgakshd uwu")
    
bruh = input("would you like to add your name or replace your name in the list or nothing? ")
bruh = bruh.lower()

if bruh == "add":
    list.append(name)
    print(list)
elif bruh == "replace":
    replace_name = input("What of the following names would you like to replace?\n{}\n".format(list))
    list = list.replace(replace_name, name)
    print(list)
elif bruh == "nothing":
    print("poopoo stinker")
else:
    print("what are you on?")
