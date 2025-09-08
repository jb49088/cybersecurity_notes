
# Basic queries

In this video, we're going to be running our very first SQL query! This query will be based on a common work task that you might encounter as a security analyst. We're going to determine which computer has been assigned to a certain employee. Let's say we have access to the employees table. 

![[Table 1.48|no-link no-title clean]]

The employees table has five columns. Two of them, employee_id and device_id, contain the information that we need. We'll write a query to this table that returns only those two columns from the table.

The two SQL keywords we need for basic SQL queries are `SELECT` and `FROM`. `SELECT` indicates which columns to return. `FROM` indicates which table to query. The use of these keywords in SQL is very similar to how we would use these words in everyday language. For example, we can ask a friend to select apples and bananas from the big box when going out to buy fruit. This is already very similar to SQL.

So let's go ahead and use SELECT and FROM in SQL to return the information we need on employees and the computers they use. We start off by typing in the SQL statement. 

```sql
SELECT employee_id, device_id
FROM employees;
```

After `SELECT`, `employee_id` and `device_id` indicate the two columns we want to return from this table. Notice how a comma separates the two columns that we want to return. And after FROM, we've identified that the information will be pulled from the employees table.

It's also worth mentioning a couple of key aspects related to the syntax of SQL here. Syntax refers to the rules that determine what is correctly structured in a computing language. In SQL, keywords are not case-sensitive, so you could also write select and from in lowercase, but we're placing them in capital letters because it makes the query easier to understand. Another aspect of this syntax is that semicolons are placed at the end of the statement.

And now, we'll run the query by pressing Enter. 

```
+-------------+-----------------+
| employee_id | device_id       |
+-------------+-----------------+
| 1001        | a320b137c219    |
| 1002        | b321c456d220    |
| 1003        | c322d567e221    |
| 1004        | d323e678f222    |
+-------------+-----------------+
```

The output gives us the information we need to match employees to their computers. We just ran our very first SQL query!

Suppose you wanted to know what department the employee using the computer is from, or their username, or the office they work in. To do that, we can use SQL to make another statement that prints out all of the columns from the table. We can do this by placing an asterisk after SELECT. This is commonly referred to as select all. Now, let's run this query to the employees table in SQL. 

```
mysql> SELECT *
	-> FROM employees;
```

And now we should have the full table in the output.