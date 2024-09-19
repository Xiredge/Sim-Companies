from Data_Base import fetch_one

"""
This function calculates the total materials and its costs required for each building when leveling up.
Parameters are:
building: type of building(i.e. electronics store), string.
m1: is for initial reinforced concrete needed, integer.
m2: is for initial bricks needed, integer.
m3: is for initial planks needed, integer.
m1: is for initial construction units needed, integer.
level: is for the level of the building, integer.
"""


def calculate(building, m1, m2, m3, m4, level, quantity):
    if level < 1:
        print("Enter a valid building level.")
        return None

    # Fetch the latest price from the database and assign it to their respective variables.
    p1, p2, p3, p4 = (fetch_one('Reinforced Concrete'), fetch_one('Bricks'),
                      fetch_one('Planks'), fetch_one('Construction Units'))
    c1 = (m1 * 2) + ((level - 3) * m1)
    c2 = (m2 * 2) + ((level - 3) * m2)
    c3 = (m3 * 2) + ((level - 3) * m3)
    c4 = (m4 * 2) + ((level - 3) * m4)

    print(f"\nThese are the required materials for a level {level} {building}.")

    if level < 3:
        print(f"Reinforced Concrete : {m1 * quantity} pieces at ${p1} each, total: {m1 * p1 * quantity}")
        print(f"Bricks              : {m2 * quantity} pieces at ${p2} each, total: {m2 * p2 * quantity}")
        print(f"Planks              : {m3 * quantity} pieces at ${p3} each, total: {m3 * p3 * quantity}")
        print(f"Construction Units  : {m4 * quantity} pieces at ${p4} each, total: {m4 * p4 * quantity}")
        print(f"Total Costs         : ${( (m1 * p1) + (m2 * p2) + (m3 * p3) + (m4 * p4) ) * quantity}")
    if level > 2:
        print(f"Reinforced Concrete : {c1 * quantity} pieces at ${p1} each, total: {c1 * p1 * quantity}")
        print(f"Bricks              : {c2 * quantity} pieces at ${p2} each, total: {c2 * p2 * quantity}")
        print(f"Planks              : {c3 * quantity} pieces at ${p3} each, total: {c3 * p3 * quantity}")
        print(f"Construction Units  : {c4 * quantity} pieces at ${p4} each, total: {c4 * p4 * quantity}")
        print(f"Total Costs         : ${( (c1 * p1) + (c2 * p2) + (c3 * p3) + (c4 * p4) ) * quantity}")


if __name__ == '__main__':
    x = int(input("Enter level of building      : "))
    y = int(input("Enter quantity of building   : "))
    calculate("Electronics Store", 20, 275, 80, 5, x, y)
    calculate("Car Dealership", 24, 330, 96, 6, x, y)
    calculate("Gas Station", 28, 385, 112, 7, x, y)
    calculate("Sales Office", 72, 990, 288, 18, x, y)
    calculate("Restaurant", 104, 1430, 416, 26, x, y)
    z = input("Press any key to continue")
