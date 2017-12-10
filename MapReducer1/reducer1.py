# input format  User_id,Contest_name , location,user_rate in Ascending
import sys


def modify(line, separator='\t'):
    return line.strip().split(separator)


def encypt(contest_name, user_rate, user_id, location):
    return str(contest_name) + "\t" + str(user_rate) + "\t" + str(user_id) + "\t" + str(location)


def reducer():
    prev_user_id = '#'
    All_info = []
    Contents = []
    for line in sys.stdin:
        Contents.append(line)

    Contents.sort()
    for line in Contents:
        Components = modify(line)
        if Components[2] != '~' and Components[0] == prev_user_id:
            for row in All_info:
                if row[1] != '~':
                    print(encypt(row[1], row[2], row[0], Components[2]))
            All_info = []
            prev_user_id = '#'
        else:
            All_info.append([Components[0], Components[1], Components[3]])
            prev_user_id = Components[0]


# Output format Contest_Name , User_Rate, User_ID,User_location
if __name__ == '__main__':
    reducer()
