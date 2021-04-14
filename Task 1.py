#variables
bar_split = 18 // 5
extra_squares = ((18 % 5) * 7) // 5
squares_left = ((18 % 5) * 7) % 5


print("The total bars evenly split between people is {}\nThe number of extra squares each is {}\nThe amount of squares let over is {}".format(bar_split, extra_squares, squares_left))

