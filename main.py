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
"""

# Room dictionary - contains the CONSTANTS of each room
# PLEASE CORRECT THE BELOW DETAILS, I'VE ASSUMED VALUES
room = {
    "chairs": 97,
    "tables": 45,
    "podium": 1,
    "projector": 1,
    "blackboard": 1,
    "serverbox": 1,
    "boxlights": 20,
    "blackboardlights": 3,
    "humans": 110,
}

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
