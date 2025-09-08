
# Basic SQL query

[[🏷️SQL]]

There are two essential keywords in any SQL query: `SELECT` and `FROM`. You will use these keywords every time you want to query a SQL database. Using them together helps SQL identify what data you need from a database and the table you are returning it from.

As an example, you can run this query to return data from the customers table of the `Chinook` database:

```sql
SELECT customerid, city, country
FROM customers;
```

```
+------------+---------------------+----------------+
| CustomerId | City                | Country        |
+------------+---------------------+----------------+
|          1 | São José dos Campos | Brazil         |
|          2 | Stuttgart           | Germany        |
|          3 | Montréal            | Canada         |
|          4 | Oslo                | Norway         |
|          5 | Prague              | Czech Republic |
|          6 | Prague              | Czech Republic |
|          7 | Vienne              | Austria        |
|          8 | Brussels            | Belgium        |
|          9 | Copenhagen          | Denmark        |
|         10 | São Paulo           | Brazil         |
|         11 | São Paulo           | Brazil         |
|         12 | Rio de Janeiro      | Brazil         |
|         13 | Brasília            | Brazil         |
|         14 | Edmonton            | Canada         |
|         15 | Vancouver           | Canada         |
|         16 | Mountain View       | USA            |
|         17 | Redmond             | USA            |
|         18 | New York            | USA            |
|         19 | Cupertino           | USA            |
|         20 | Mountain View       | USA            |
|         21 | Reno                | USA            |
|         22 | Orlando             | USA            |
|         23 | Boston              | USA            |
|         24 | Chicago             | USA            |
|         25 | Madison             | USA            |
+------------+---------------------+----------------+
(Output limit exceeded, 25 of 59 total rows shown)
```

### SELECT

The `SELECT` keyword indicates which columns to return. For example, you can return the `customerid` column from the `Chinook` database with

`SELECT customerid`

You can also select multiple columns by separating them with a comma. For example, if you want to return both the `customerid` and `city` columns, you should write `SELECT customerid, city`.

If you want to return all columns in a table, you can follow the `SELECT` keyword with an asterisk (`*`). The first line in the query will be `SELECT *`.

> [!note]
> Although the tables you're querying in this course are relatively small, using `SELECT *` may not be advisable when working with large databases and tables; in those cases, the final output may be difficult to understand and might be slow to run.

### FROM

The `SELECT` keyword always comes with the `FROM` keyword. `FROM` indicates which table to query. To use the `FROM` keyword, you should write it after the `SELECT` keyword, often on a new line, and follow it with the name of the table you’re querying. If you want to return all columns from the `customers` table, you can write:

```sql
SELECT *
FROM customers;
```

When you want to end the query here, you put a semicolon (`;`) at the end to tell SQL that this is the entire query.

> [!note]
> Line breaks are not necessary in SQL queries, but are often used to make the query easier to understand. If you prefer, you can also write the previous query on one line as
> `SELECT * FROM customers;`
