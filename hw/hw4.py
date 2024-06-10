# Exercise #1: (10 points)

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12, 'map fragments':3}
print("Inventory:")
total = 0
for key, item in inventory.items():
    print(item, key)
    total += item
print("Total number of items :", total)

# Exercise #2: (10 points)
characters = ["Thor", "Thanos", "Black Panther", "Iron Man", "Hulk", "Batman", "Captain America"]
print(", ".join(characters[:-1]),"and", characters[-1],".")

# Exercise #3: (10 points)
dictionary = {
    "dict" : "stores a key/value pair",
    "list" : "stores a value at each index",
    "map" : "see dict",
    "set" : "stores unordered unique elements"
}
while(True):
    word = input("Enter the word to lookup: ")
    if word == "exit":
        break
    else:
        print(dictionary[word])

# Exercise #4: (2 points)
print(set("Mississippi"))

# Exercise #5: (2 points)
list1 = [1, 2, [3, 4, "hello"]]
list1[2][2] = "goodbye"
print(list1)

# Exercise #6: (3 points)
# 6a.
d = {'simple_key':"hello"}
print(d["simple_key"])

# 6b.
d = {"k1":{"k2":"hello"}}
print(d["k1"]["k2"])