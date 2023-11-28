"""
Variables:
1. Room No.
2. Sunlight direction
3. Sunlight intensity (based on time)
4. Time of Day

Constants:
1. Number of furniture
2. Number of heat sources excluding Sun (projector, server box, etc)
(try to make it a dictionary)

WHOEVER EDITS THIS: Please try to use better data structures than me (like Classes instead of dictionaries)
"""

# Furniture details below:
# Everything in meters please!
chair = {
    "length": 10,
    "breadth": 10,
    "height": 10,
}
table = {
    "length": 10,
    "breadth": 10,
    "height": 10,
}
podium = {
    "length": 10,
    "breadth": 10,
    "height": 10,
}
projector = {
    "length": 10,
    "breadth": 10,
    "height": 10,
}
blackboard = {
    "length": 10,
    "breadth": 10,
    "height": 10,
}
serverbox = {
    "length": 10,
    "breadth": 10,
    "height": 10,
}


# Room Class - contains the CONSTANTS of each room
# PLEASE CORRECT THE BELOW DETAILS, I'VE ASSUMED VALUES
class Room:
    number = int
    chairs = 97
    tables = 45
    podium = 1
    projector = 1
    blackboard = 1
    serverbox = 1
    ceiling_lights = 20
    blackboard_lights = 3
    humans = 110


# Room selection function
def room_selection(time):
    # Time of day check
    if time == 1:
        time = "morning"
    elif time == 2:
        time = "afternoon"
    elif time == 3:
        time = "evening"
    elif time == 4:
        time = "night"
    else:
        print("Please enter a valid time (1-4)!")
        user_prompt()

    # Room Selection
    room = Room()
    print("Please enter room number")
    room.number = int(input("To select A-605 enter '5', to select A-601 enter '1'\n"))
    if room.number == 1:
        print(f"You have selected {time} at A-601")
    elif room.number == 5:
        print(f"You have selected {time} at A-605")
    else:
        print("Please enter a valid room number (1 or 5)")
        room_selection(time)


# Initial user prompt function
def user_prompt():
    print(f"Please enter the time of day")
    time = int(
        input(
            "To select morning enter '1', to select afternoon enter '2', to select evening enter '3', to select night enter '4'\n"
        )
    )
    room_selection(time)


user_prompt()
