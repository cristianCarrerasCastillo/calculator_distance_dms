# this program calculate the distance between two points in dms format and return the distance in meters
# the program is written by Cristian Carreras

import math

# function to convert dms to decimal degrees
def dms2dd(degrees, minutes, seconds, direction):
    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)
    if direction == 'S' or direction == 'W':
        dd *= -1
    return dd

def validate_dms(dms):
    # check if the input is in the correct format
    print(len(dms))
    if len(dms) != 8:
        print("The input is not in the correct format")
        return False
    # check if the degrees, minutes and seconds are numbers
    try:
        float(dms[0])
        float(dms[1])
        float(dms[2])
    except ValueError:
        print("The degrees, minutes and seconds must be numbers")
        return False
    # check if the direction is correct
    if dms[3] != 'N' and dms[3] != 'S' and dms[7] != 'E' and dms[7] != 'W' :
        print("The direction is not correct")
        print("The direction must be N, S, E or W, N or S first and E or W second")
        return False
    return True

def text():
    print("Enter the coordinates of the two points in dms format, for example: 40 26 46.302 N 79 58 56.073 W")
    print("Please remember separate all values with a space")

def main():
    dms1_list = []
    dms2_list = []
    # input the coordinates of the two points in dms format
    print("This program calculates the distance between two points in dms format")
    text()

    while validate_dms(dms1_list) == False or len(dms1_list) == 7:
        text()
        dms1 = input("Enter the coordinates of the first point in dms format: ")
        try:
            dms1_list = dms1.split()
            dms1_list[3] = dms1_list[3].upper()
            dms1_list[7] = dms1_list[7].upper()
        except ValueError:
            print("The input is not in the correct format")
            continue

    while validate_dms(dms2_list) == False or len(dms2_list) == 7:
        text()
        dms2 = input("Enter the coordinates of the second point in dms format: ")
        try:
            dms2_list = dms2.split()
            dms2_list[3] = dms2_list[3].upper()
            dms2_list[7] = dms2_list[7].upper()
        except ValueError:
            print("The input is not in the correct format")
            continue

    # convert the dms to decimal degrees
    lat1 = dms2dd(dms1_list[0], dms1_list[1], dms1_list[2], dms1_list[3])
    lon1 = dms2dd(dms1_list[4], dms1_list[5], dms1_list[6], dms1_list[7])

    lat2 = dms2dd(dms2_list[0], dms2_list[1], dms2_list[2], dms2_list[3])
    lon2 = dms2dd(dms2_list[4], dms2_list[5], dms2_list[6], dms2_list[7])

    # calculate the distance between the two points
    radius = 6371000 # meters
    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = radius * c
    print("The distance between the two points is: ", distance, "meters")

if __name__ == "__main__":
    print("This program is being run by itself")
    main()