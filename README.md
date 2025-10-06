# 🛠️ Simple Query Runner

A lightweight Python CLI app that mimics basic SQL-style querying from in-memory databases like `People` and `Aliens`. No setup, no SQL server — just Python logic and structured data.

---

##  Why I Built This

This was built as a personal learning tool to:

- Simulate SQL logic using Python
- Practice user input parsing and command interpretation
- Understand how a query engine processes and accesses data
- Improve backend skills for future projects

It’s a beginner-friendly foundation for future exploration into databases, interpreters, and even building a custom query language.

---

##  What It Does

- Defines two example databases in memory: `People` and `Aliens`
- Accepts user input with SQL-like commands:
  - `SELECT`
  - `FROM`
  - `LIMIT`
  - Ends with `DONE`
- Parses the command and fetches relevant results
- Displays the filtered data to the user

---

##  Example Usage

### User Input

```
SELECT name
FROM aliens
LIMIT 2
DONE
```

### Output

```
Zorglon
Bleep
```

---

##  Supported Commands

| Command      | Description                                |
|--------------|--------------------------------------------|
| `SELECT`     | What field to display (`name`, `age`, `*`) |
| `FROM`       | Which dataset to use (`people`, `aliens`)  |
| `LIMIT`      | How many results to show                   |
| `DONE`       | Ends input and runs the query              |

** Format matters!**  
Commands must be entered one per line and end with `DONE`.

---

##  Future Plans

- `WHERE` support (e.g., `WHERE age > 30`)
- Allow selecting multiple fields: `SELECT name, age`
- Add sorting (`ORDER BY age DESC`)
- Create a REPL-style session
- Load/save datasets from JSON or CSV
- Add error recovery for missing clauses or bad input

---

### Requirements

No libraries are required. Just Python 3.



