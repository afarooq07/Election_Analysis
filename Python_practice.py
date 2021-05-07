"""
print("Hello World!")

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])


temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

#What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')


# What is the score? second technique
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')


# practice membership and logical operators
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

counties = ["Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

print("Testing range function")
for i in range(len(counties)):
    print(counties[i])


print("Testing while loop")
# WHile loop
x = 0
while x <= 5:
    print(x)
    x = x + 1    

print("Testing for loop")
# Practive for loop
for county in counties:
    print(county)    

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

print("iterate thru a dictionary")
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}    
for county in counties_dict.keys():
    print(county)

print("Print values of dictionary - part 1")
for county in counties_dict:
    print(counties_dict[county])
    
print("Print values of dictionary - Part 2")       
for voters in counties_dict.values():
    print(voters)

print("Print key-values of dictionary")  
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters")    

# print a ;ist of dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]


print("Print registered voters values")  
for county_dict in voting_data:
    print(county_dict.values())
    print(county_dict)

for county_dict in voting_data:
    for county in county_dict.values():
        print(county)

print("retrieve the number of registered voters from each dictionary") 
for county_dict in voting_data:    
   for value in county_dict.values():      
       print(value)

for county_dict in voting_data:
     print(county_dict['registered_voters'])

# F-strings: Formatted String Literals
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")   


print("Print key-values of dictionary")  
for county, voters in counties_dict.items():
    print(F"{county} county has {voters} registered voters")  

# Multipline f-strings
print("Multipline f-strings")
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)    
"""


"""

# Skill Drill 1 - 3.2.11
print ("********************** skill drill 1 **********************")
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters")  
 

 # Skill Drill 2 - 3.2.11
print ("********************** skill drill 2 **********************")
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}] 
for county_dict in voting_data:
     print(f" {county_dict['county']} county has {county_dict['registered_voters']:,} registered voters")

"""   


numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)   

counties = ["Arapahoe","Denver","Jefferson"]
#for county in counties:
#    print(county)

for i in range(len(counties)) :   
    print(counties[i])



