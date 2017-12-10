# input format ContestName and User_location Sorting Ascending By
# Contest_Name->Best Rate in Contest -> User_id -> User_HomeCountry
######
import sys


def modify(line, separator='\t'):
    return line.strip().split(separator)


def reducer():
    All_info = {}     # To avoid Taking more than 4 Contest in Each Contest
    countries_per_contest = []  # To Store The Country of 4 Contest and print when the len equal 4
    Contents = []
    for line in sys.stdin:
        Contents.append(line)
    Contents.sort()
    for line in Contents:
        Components = modify(line)
        if Components[0] == '~':
            continue
        if Components[0] not in All_info:
            All_info[Components[0]] = 1
            countries_per_contest.append(Components[3])
        elif Components[0] in All_info and All_info[Components[0]] < 4:
            All_info[Components[0]] = All_info[Components[0]] + 1
            countries_per_contest.append(Components[3])
            Rank = 1
            if All_info[Components[0]] == 4:
                ret = str(Components[0]) + ": "
                for x in countries_per_contest:
                    ret = ret + "(" + str(Rank) + ")" + str(x) + " "
                    Rank = Rank + 1
                print(ret + "\n")
                countries_per_contest = []
        else:
            continue


# Output the First 4 Contestant in Every Contest like format ACMICPC# : (1) # (2) # (3) # (4) #
if __name__ == '__main__':
    reducer()
