# input format  User_id,Contest_name , location,user_rate in Ascending
import sys


def modify(line, separator='\t'):
    return line.strip().split(separator)


def encypt(contest_name, user_rate, user_id, location):
    return str(str(contest_name) + "\t" + str(user_rate) + "\t" + str(user_id) + "\t" + str(location))


def reducer():
    prev_user_id = '#'
    location = '#'
    for line in sys.stdin:
        Components = modify(line)
        if Components[1] == '0':
            location = Components[2]
            prev_user_id = Components[0]
        elif Components[1] != '0' and prev_user_id == Components[0]:
            print(encypt(Components[1], Components[3], Components[0], location))
        else:
            continue


# Output format Contest_Name,User_Rate ,User_ID,User_location
if __name__ == '__main__':
    reducer()
