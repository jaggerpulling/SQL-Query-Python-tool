
import sqlite3

def connect_sql():
    # Step 1: Connect to a database (stored in memory)
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    return conn, cursor


def create_database(cursor):
    # Step 2: Create a table
    cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
    """)

    # Step 3: Add some example users
    sample_data = [('Alice', 23),
                   ('Bob', 30),
                   ('Joe', 24),
                   ('Jeff', 36),
                   ('Charlie',25)]
    cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", sample_data)

    return sample_data


def parse_command(command,cursor):

    #Step 5: Convert command into SQL
    if command == "show all":
        cursor.execute("SELECT * FROM users")
    elif command == "show name":
        cursor.execute("SELECT name FROM users")
    else:
        print("Unknown command.")


def show_result(cursor):
    # Step 6: Show the results
    results = cursor.fetchall()
    print("\nResults:")
    for row in results:
        print(row)

def main():
    conn, cursor = connect_sql()
    sample_data = create_database(cursor)

    # Step 4: Ask user what they want to see
    command = input("Enter command (show all OR show name): ").strip().lower()

    parse_command(command,cursor)
    show_result(cursor)



    # Step 7: Close connection
    conn.close()

if __name__ == "__main__":
    main()