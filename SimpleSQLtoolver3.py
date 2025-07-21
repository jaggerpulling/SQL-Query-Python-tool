"""
# ========================================
# File: SimpleSQLtool.py
# Description: Creates and edit databases using SQL commands within python for self-learning purposes.
#              Adding more functions as I continue learning
# Author: Jagger Pulling
# Created: July 18 2025
# Revisions:
July 19 2025
July 21 2025
# ========================================
"""


# === IMPORTS ===
# (No imports used yet, placeholder for future needs)


# === CONSTANTS ===
EXIT_COMMAND = 'DONE'
VERSION = "1.6"

# === DATA CREATION ===
def create_data():
    databases = {
        'people': [
            {'id': 1, 'name': 'Jagger', 'age': 22},
            {'id': 2, 'name': 'Bob', 'age': 12},
            {'id': 3, 'name': 'Joe', 'age': 67},
            {'id': 4, 'name': 'Alice', 'age': 32},
        ],
        'aliens': [
            {'id': 1, 'name': 'Zorglon', 'age': 152, 'planet': 'Xebulon-5', 'species': 'Glormak'},
            {'id': 2, 'name': 'Bleep', 'age': 23, 'planet': 'Nibiru', 'species': 'Zentar'},
            {'id': 3, 'name': 'Kranglor', 'age': 306, 'planet': 'Tauron', 'species': 'Vulkar'},
            {'id': 4, 'name': 'Luma', 'age': 89, 'planet': 'Venara', 'species': 'Sylphian'},
        ]
    }
    return databases

# === INPUT COLLECTION ===
def user_input():
    query = []
    print(f"Enter SQL command and enter '{EXIT_COMMAND}' to finish: ", end='')

    while True:
        command = input()
        query.append(command)

        # Exits input and removes 'done' from query
        if command.strip().lower() == EXIT_COMMAND.lower():
            del query[(len(query)) - 1]
            break

    return query

# === QUERY PARSING ===
def parse_command(query):
    operator = None
    selected_database = None
    limit_clause = None

    for line in query:
        if line.startswith('SELECT'):
            operator = line[7:].strip()

        elif line.startswith('FROM'):
            selected_database = line[5:].strip()

        elif line.startswith('LIMIT'):
            limit_clause = line[6:].strip()
            limit_clause = int(limit_clause)

        else:
            print('invalid command')

    return operator, selected_database, limit_clause

# ------------------------------
# Query Execution
# === QUERY EXECUTION ===
def build_query(operator, selected_database, limit_clause, databases):
    if selected_database.lower() in databases:
        data = databases[selected_database.lower()]
    else:
        print("Unknown database")
        return

    count = 0
    max_items = limit_clause if limit_clause is not None else len(data)

    for item in data:
        if count >= max_items:
            break

        if operator.lower() == 'name':
            print(item['name'])
        elif operator.lower() == 'age':
            print(item['age'])
        elif operator.lower() in ('all', '*'):
            print(item)

        else:
            print(f"Unknown field: {operator}")
            break

        count += 1

# === MAIN PROGRAM ENTRY ===
def main():
    databases = create_data()
    query = user_input()
    operator, selected_database, limit_clause = parse_command(query)
    build_query(operator, selected_database, limit_clause, databases)

# === PROGRAM START ===
if __name__ == '__main__':
    main()