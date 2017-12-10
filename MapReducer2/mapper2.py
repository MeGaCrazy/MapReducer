# input format Contest_Name , User_Rate, User_ID,User_location
import sys


def modify(line, separator='\t'):
    return line.strip().split(separator)


def encypt(Contest_Name, User_Rate, User_ID, User_location):
    return str(Contest_Name) + "\t" + str(User_Rate) + "\t" + str(User_ID) + "\t" + str(User_location)


def mapper():
    for line in sys.stdin:
        Components = modify(line)
        print(encypt(Components[0], Components[1], Components[2], Components[3]))


# Output ContestName and User_location  By Top Rate in Contest
if __name__ == '__main__':
    mapper()
