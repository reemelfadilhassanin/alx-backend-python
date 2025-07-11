# Context Managers and Asynchronous programming in python

* Novice
* Weight: 1
* Project will start **Jul 6, 2025 11:00 PM**, must end by **Jul 13, 2025 11:00 PM**
* Checker was released at **Jul 6, 2025 11:00 PM**
* **Manual QA review must be done** (request it when you are done with the project)
* An auto review will be launched at the deadline

## Tasks

##### 0. custom class based context manager for Database connection**mandatory**

**Objective:** create a class based context manager to handle opening and closing database connections automatically

**Instructions:**

* Write a class custom context manager `DatabaseConnection` using the `__enter__` and the `__exit__` methods
* Use the context manager with the `with` statement to be able to perform the query `SELECT * FROM users`. Print the results from the query.

**Repo:**

* GitHub repository: `alx-backend-python`
* Directory: `python-context-async-perations-0x02`
* File: `0-databaseconnection.py`

Check submission

##### 1. Reusable Query Context Manager**mandatory**

**Objective:** create a reusable context manager that takes a query as input and executes it, managing both connection and the query execution

**Instructions:**

* Implement a class based custom context manager `ExecuteQuery` that takes the query: `”SELECT * FROM users WHERE age > ?”` and the parameter `25` and returns the result of the query
* Ensure to use the `__enter__()` and the `__exit__()` methods

**Repo:**

* GitHub repository: `alx-backend-python`
* Directory: `python-context-async-perations-0x02`
* File: `1-execute.py`

Check submission

##### 2. Concurrent Asynchronous Database Queries**mandatory**

**Objective:** Run multiple database queries concurrently using `asyncio.gather`.

**Instructions:**

* Use the `aiosqlite` library to interact with SQLite asynchronously. To learn more about it, [click here](https://savanna.alxafrica.com/rltoken/Dp_5xrVa75wVwJSv5udTpA "click here").
* Write two asynchronous functions: `async_fetch_users()` and `async_fetch_older_users()` that fetches all users and users older than 40 respectively.
* Use the `asyncio.gather()` to execute both queries concurrently.
* Use `asyncio.run(fetch_concurrently())` to run the concurrent fetch

**Repo:**

* GitHub repository: `alx-backend-python`
* Directory: `python-context-async-perations-0x02`
* File: `3-concurrent.py`

Check submission

##### 3. Manual Review**mandatory**

**Repo:**

* GitHub repository: `alx-backend-python`
* Directory: `python-context-async-perations-0x02`

Ready for a review

[Back](https://savanna.alxafrica.com/concepts/111449?project_id=101621)

[Next](https://savanna.alxafrica.com/concepts/111671?project_id=102758)
