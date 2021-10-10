# print("Hello World")

# create a dictionary
counties_dict = {}
# add arapahoe to the dictionary as the KEY and the number of voters
# for arapahoe as VALUES for this key
counties_dict["Arapahoe"] = 422829
counties_dict

# add denver and jefferson with their respective number of voters
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)

# to get keys and values use items() method
counties_dict.items()
print(counties_dict.items())

# to get ONLY the keys use the keys() method
counties_dict.keys()
print(counties_dict.keys())

# to get ONLY the values use the values() method
print(counties_dict.values())

# to get SPECIFIC VALUES use get('KEY') method
print(counties_dict.get("Denver"))
# or wrap the key in brackets
print(counties_dict["Arapahoe"])

# create a LIST of dictionaries
# create an empty list called voting_data
voting_data = []
# add each dictionary to the voting_data list
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)
print(len(voting_data))
# get one or more dictionaries
print(voting_data[:1])
# add a new dictionary
voting_data.append({"prueba": 1234})
print(voting_data)
# remove prueba dictionary
voting_data.pop(3)
print(voting_data)

# IF STATEMENT
# counties = ["Arapahoe", "Denver", "Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])

# IF-ELSE STATEMENT
# temperature = int(input("What is the temperature outside? "))

# if temperature > 80:
#     print("Turn on the AC")
# else:
#     print("Open the windows")

# NESTED IF-ELSE STATEMENT
# What is the score
# score = int(input("What is your test score?"))
# # determine the grade
# if score >= 90:
#     print('Your grade is an A')
# else:
#     if score >= 80:
#         print('Your grade is a B')
#     else:
#         if score >= 70:
#             print('Your grade is a C')
#         else:
#             if score >= 60:
#                 print('Your grade is a D')
#             else:
#                 print('Your grade is an F')

# IF ELIF STATEMENT
# score = int(input("What is your test score?"))
# if score >= 90:
#     print('Your grade is an A')
# elif score >= 80:
#     print('Your grade is a B')
# elif score >= 70:
#     print('Your grade is a C')
# else:
#     print('Your grade is a D')

# MEMBERSHIP OPERATORS
counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El paso is in the list of counties")
else:
    print("El paso is not in the list of counties")

# MEMBERSHIP AND LOGICAL OPERATORS
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties")
else:
    print("Arapahoe or El Paso is not in the list of counties")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties")
else:
    print("Arapahoe and El Paso are not in the list of counties")

for county in counties:
    print(county)

# ITERATE THROUGH LISTS AND TUPLES
numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

for i in range(len(counties)): # the variable i is used to indicate the index, or the values 0,1, and 2
    # inside the range() function, we get the lenght of the list of counties
    print(counties[i])

counties_tuple = ("Arapahoe", "Denver", "Jefferson")
for i in range(len(counties_tuple)):
    print(counties_tuple[i])

# ITERATE THROUGH DICTIONARIES
# get the KEYS of a dictionary
for county in counties_dict.keys(): # could be with keys() method or without the keys() method
    print(county)

# get the VALUES of a dictionary
for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county]) # when using this format, it must have th KEY in the for loop in the print statement
    # this will return the value of the key

# use get() method on the dictionary in the for loop to get the values
for county in counties_dict:
    print(counties_dict.get(county))

# get the KEY VALUE PAIRS of the dictionary using the items() method
for county, voters in counties_dict.items():
    print(county, voters)

# another option
# for key, value in dictionary_name.items():
#   print(key, value)
for key, value in counties_dict.items():
    print(key, value)

# when iterating over a dictionary, the first variable declared in the for loop is assigned to the keys
# the second variable is assigned to the values

# ITERATE THROUGH A LIST OF DICTIONARIES
# with a for loop we can: retrieve each dictionary in the list, retrieve only the values of each dictionary,
# retrieve the key-value pairs of each dictionary

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
    print(voting_data[i])

# GETTING THE VALUES FROM A LIST OF DICTIONARIES
# use a nested for loop
for county_dict in voting_data: # this will retrieve each dictionary
    for value in county_dict.values():
        print(value)

# retrieve the number of registered voters from each dictionary
for county_dict in voting_data:
    print(county_dict['registered_voters'])

# retrieve the county name from each dictionary
for county_dict in voting_data:
    print(county_dict['county'])

# using F strings to print
my_votes = int(input("How many votes did you get in the election?"))
total_votes = int(input("What is the total votes in the election"))
print(f"I received {my_votes / total_votes * 100}% of the total votes") # the f-string performs the calculations
# curly braces {} are used to add variables or expressions to the f-string

# using f strings with dictionaries
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters")

# using multiline f strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

# format floating point decimals
# the format for a number to format it in an f-string is as follows:
# f'{value:{width}.{precision}}'
# width specifies the number of characters used to display the value
# precision indicates the number of decimal places to format the value



