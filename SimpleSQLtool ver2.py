def create_data():
    users = [
        {'id':1, 'name': 'Jagger', 'age':22},
        {'id': 2, 'name': 'Bob', 'age': 12},
        {'id': 3, 'name': 'Joe', 'age': 67},
        {'id': 4, 'name': 'Alice', 'age': 32},
    ]
    return users

def user_input():
    query = []
    print(f'Enter SQL command: ',end='')
    while True:
        command = input()
        query.append(command)
        print("Enter 'DONE' to end input")

        # Exits input and removes 'done' from query
        if command.strip().lower() == 'done':
            del query[(len(query))-1]
            break

    print(query)
    return query

def parse_command(query, users):

    for line in query:
        if line.startswith('SELECT'):
            if 'limit' in query:
                limit = int(query.split(' ')[1])
            operator = line[5:].strip()

            if operator.lower() == 'name':
                for user in users:
                    print(user['name'])

            elif operator.lower() == 'age':
                for user in users:
                    print(user['age'])

            elif operator.lower() == 'all' or '*':
                for user in users:
                    print(user)

            else:
                print('add debug HERE in OPERATOR IF ELSE')


        else:
            print('invalid command')




def main():
    users = create_data()
    query = user_input()
    parse_command(query,users)

main()