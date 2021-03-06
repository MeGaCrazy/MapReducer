import sys


# First DataSet is like User_name , User_id, User_HomeCountry
# Second DataSet is like ContestName,Contest_id,User_id,Rate_OfUser,ContestLocation

def modify(line, separator='\t'):
    return line.strip().split(separator)


def encypt(contest_name, user_id, location, user_rate):
    return str(contest_name) + "\t" + str(user_id) + "\t" + str(location) + "\t" + str(user_rate)


def mapper():
    for line in sys.stdin:
        location = '~'
        contest_name = '0'
        user_rate = '~'
        user_id = '~'
        Components = modify(line)
        if len(Components) == 3:
            user_id = Components[1]
            location = Components[2]
        else:
            contest_name = Components[0]
            user_rate = Components[3]
            user_id = Components[2]
        print(encypt(user_id, contest_name, location, user_rate))

        # OutPut User_id,Contest_id,location,User_rate Sorted Ascending


if __name__ == '__main__':
    mapper()
