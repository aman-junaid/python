"""
The script is solution to my capstone project after completing the Python Training
If provides solution to problem of find total cost of tiling a floor

Find Cost of Tile to Cover W x H Floor - Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.
"""


def calculate_cost(length: float, height: float, costpersq: float):
    return length * height * costpersq


def get_usr_input():
    height = float(input('Please enter floor height(in feet): '))
    width = float(input('Please enter floor width(in feet): '))
    costpersq = float(input('Please enter cost per square feet: '))
    return height, width, costpersq

def main():
    height, width, costpersq = get_usr_input()
    print(f'\nThe total cost of tiling the floor is: {calculate_cost(height,width,costpersq)}')


if __name__ == '__main__':
    main()
