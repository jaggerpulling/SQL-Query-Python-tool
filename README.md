# 🛠️ Simple Query Runner

A lightweight Python CLI app that mimics basic SQL-style querying from in-memory databases like `People` and `Aliens`. No setup, no SQL server — just Python logic and structured data.

---

## 📌 Why I Built This

This was built as a personal learning tool to:

- Simulate SQL logic using Python
- Practice user input parsing and command interpretation
- Understand how a query engine processes and accesses data
- Improve backend skills for future projects

It’s a beginner-friendly foundation for future exploration into databases, interpreters, and even building a custom query language.

---

## 💻 What It Does

- Defines two example databases in memory: `People` and `Aliens`
- Accepts user input with SQL-like commands:
  - `SELECT`
  - `FROM`
  - `LIMIT`
  - Ends with `DONE`
- Parses the command and fetches relevant results
- Displays the filtered data to the user

---

## 📋 Example Usage

### 👤 User Input

```
SELECT name
FROM aliens
LIMIT 2
DONE
```

### 🖥️ Output

```
Zorglon
Bleep
```

---

## ✅ Supported Commands

| Command      | Description                                |
|--------------|--------------------------------------------|
| `SELECT`     | What field to display (`name`, `age`, `*`) |
| `FROM`       | Which dataset to use (`people`, `aliens`)  |
| `LIMIT`      | How many results to show                   |
| `DONE`       | Ends input and runs the query              |

**⚠️ Format matters!**  
Commands must be entered one per line and end with `DONE`.

---

## 🔧 Future Plans

- `WHERE` support (e.g., `WHERE age > 30`)
- Allow selecting multiple fields: `SELECT name, age`
- Add sorting (`ORDER BY age DESC`)
- Create a REPL-style session
- Load/save datasets from JSON or CSV
- Add error recovery for missing clauses or bad input

---

## 🧠 Skills Practiced

- Parsing strings and user input
- Control flow and conditionals
- Working with lists and dictionaries
- Simulating backend behavior
- CLI program structure and modularity

---

## 🧪 Project Setup

### Requirements

No libraries are required. Just Python 3.

```bash
python simple_query_runner.py
```

---

## 📁 Project Structure

```
simple-query-runner/
│
├── simple_query_runner.py     # Main program file
├── README.md                  # You're reading it!
```

---

## 🌱 Potential Requirements.txt (For Future Versions)

If you expand this project to include file input/output or JSON parsing, you might add:

```txt
# optional future additions
pandas
json
click         # for CLI improvement
```

---

## 🙌 Feedback & Contribution

Got suggestions? Want to build on top of this? Feel free to fork, clone, and remix this tool.

Reach out or open a pull request with your ideas 💡

---
