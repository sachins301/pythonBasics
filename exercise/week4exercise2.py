#1.1 Create Dictionaries (2.5 points)
bday_dict = {
    "Susan" : "14/01/2002",
    "Bejamin": "21/02/1998",
    "Blaze": "30/08/2006"
}
for key in bday_dict:
    print(key, "->", bday_dict[key])

#1.2 Update Dictionaries (2.5 points)
last_key = list(bday_dict.keys())[-1]
bday_dict[last_key] = '06/06/1980'
print(bday_dict)

#1.3 Dictionary With Lists (2.5 points)
seasons ={
    "Fall": ["September", "October", "November"],
    "Spring": ["March", "April", "May"],
    "Summer": ["June", "July", "August"]
}
print(seasons["Fall"])

#1.4 Dictionary Merge (2.5 points)
winter_season = {"Winter": ["December", "January", "February"]}
seasons.update(winter_season)
print(seasons)