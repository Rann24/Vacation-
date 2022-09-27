# Program Name: Lab 4py
 # Course: IT1114/Section 01
 # Student Name: Randy Rice
 # Assignment Number: Lab4
 # Due Date: 9/18/22
 # Purpose: Have the user slect their room, meal and excursion

#room cost function
def roomCost(num_nights, room_type):
    if room_type == 1:
        room_type = 375 * num_nights
    elif room_type == 2:
        room_type = 350 * num_nights
    elif room_type == 3:
        room_type = 525 * num_nights
    elif room_type == 4:
        room_type = 475 * num_nights

    return room_type

# meal cost function
def mealCost(brunch, dinner):
    brunch_Cost = brunch * 25
    dinner_Cost = dinner * 75
    gratuity = (brunch_Cost + dinner_Cost) * 0.15
    total = brunch_Cost + dinner_Cost + gratuity
    return total

#excursion function
def excursionCost(picnic, snorkeling, hike, boat):
    if picnic == "y":

        picnic= 50
    elif picnic =="n":
        picnic=0

    if snorkeling == "y":
        snorkeling = num_people * 25
    elif snorkeling=="n":
        snorkeling=0

    if hike == "y":
        hike = num_people * 17
    elif hike =="n":
        hike=0

    if boat == "y":
        boat= 200
    elif boat =="n":
        boat=0

    total = int (picnic) + int (snorkeling) + int (hike) + int(boat)

    return total

#Gets user input for number of nights and people
num_nights = int(input("Number of nights: "))
num_people = int(input("Number of people"))
#prints what type of room
print("Room Types:\n(1)-Two Queen Beds\n(2)-One King Bed\n(3)-Queen Suite\n(4)-King Suit")

room_type = int(input("Select Type:"))
brunch = int(input("How many brunches "))
dinner = int(input("How many dinners"))

picnic = input("Picnic?: ")
snorkeling = input("Snorkeling?:")
hike = input("Guided Hike?: ")
boat = input("Boat Dinner? : ")

#functions
room_cost = roomCost(num_nights, room_type)
print(+room_cost)

meal_cost = mealCost(brunch, dinner)
print(+meal_cost)

excursion_cost = excursionCost(picnic, snorkeling, hike, boat)
print(excursion_cost)

print(room_cost+meal_cost+excursion_cost)
