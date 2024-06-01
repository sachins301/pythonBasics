#1.1 Color List

colors = ["Violet", "Indigo", "Blue", "Green", "Yellow", "Orange"]
print(colors)
print(len(colors))
print(colors[4])
print(colors[1:5])
print(colors[-3:])
print(colors * 2)

#1.2 Color List Mutation
colors[5] = "Red"
print(colors)
colors[2] = colors[4]
print(colors)
new_colors = ["Black", "White", "Grey"] + colors
print(new_colors)
new_colors[5] = colors
print(new_colors)