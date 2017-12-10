# input format ContestName and User_location Sorting Ascending By
# Contest_Name->Best Rate in Contest -> User_id -> User_HomeCountry
import sys


def modify(line, separator='\t'):
    return line.strip().split(separator)


def reducer():
    Count_Top_4 = 0
    contest = "#"
    for line in sys.stdin:
        Components = modify(line)
        if Components[0] == '0' or (Components[0] == contest and Count_Top_4 >= 4):
            continue
        elif Components[0] != contest:
            contest = Components[0]
            Count_Top_4 = 1
            print(str(Components[0]) + ": " + "\n" + "(" + str(Count_Top_4) + ")" + str(Components[3]) + " ")
        elif Components[0] == contest and Count_Top_4 < 4:
            Count_Top_4 = Count_Top_4 + 1
            print("(" + str(Count_Top_4) + ")" + str(Components[3]) + " ")
        else:
            continue


# Output the First 4 Contestant in Every Contest like format ACMICPC# : (1) # (2) # (3) # (4) #
if __name__ == '__main__':
    reducer()
