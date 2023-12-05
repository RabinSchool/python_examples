thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)  #  {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


#Get the value of the "model" key:
x = thisdict["model"]  # Mustang

#Get the value of the "model" key:
x = thisdict.get("model") # Mustang

#Print all key names in the dictionary, one by one:
for x in thisdict:
  print(x)  

# brand
# model
# year

#Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x])


#Loop through both keys and values, by using the items() function:
for x, y in thisdict.items():
  print(x, y)


#Check if "model" is present in the dictionary:
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


#Adding an item to the dictionary is done by using a new index key and assigning a value to it
thisdict["color"] = "red"

#The pop() method removes the item with the specified key name:
thisdict.pop("model")
# OR
del thisdict["model"]

#The clear() keyword empties the dictionary:
thisdict.clear()
# Or  "del thisdict" do delete the dic


#Make a copy of a dictionary with the copy() method:
mydict = thisdict.copy()