# input format ContestName and User_location Sorting Ascending By Best Rate in Contest
######
import sys


def modify(line, separator='\t'):
    return line.strip().split(separator)


def reducer():
    All_info = {}
    countries_per_contest = []
    for line in sys.stdin:
        Components = modify(line)
        if Components[0] == '~':
            continue
        if Components[0] not in All_info:
            All_info[Components[0]] = 1
            countries_per_contest.append(Components[1])
        elif Components[0] in All_info and All_info[Components[0]] < 4:
            All_info[Components[0]] = All_info[Components[0]] + 1
            countries_per_contest.append(Components[1])
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


if __name__ == '__main__':
    reducer()
