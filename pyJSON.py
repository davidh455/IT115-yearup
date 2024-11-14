#Importing class library JSON
import json

#Data Dictionary
data1 = {

    'name':'David Hoang',
    'age':22,
    'city': 'Tukwila, WA',
    'interests':['Board Games', 'Pickleball', 'Reading', 'Building', 'Videogames', 'Math'],
    'is_student': True

}

#dumps the data into data1 JSON file
with open( 'data1.json', 'w') as json_file:

    #Dump the Data Dictionary into the JSON file.
    json.dump(data1, json_file, indent = 4)

print("You have successfully written to data1.json")

#loaded_data is now assigned to loading the data1.json file
with open ('data1.json', 'r') as json_file:

    loaded_data = json.load(json_file)


print("Sucessfully able to read data1.json")
print(loaded_data)

#modifies the data, from changing age, appending values, and removing values
loaded_data['age'] = 11

loaded_data['interests'].append('David4')
loaded_data['interests'].append('David5')
loaded_data['interests'].append('David6')
loaded_data['interests'].remove('David5')

#loads the new data changes made to data1
with open('data1.json', 'w') as json_file:

    json.dump(loaded_data, json_file, indent=4)

print("Modifies data written to data1.json")
print(loaded_data)