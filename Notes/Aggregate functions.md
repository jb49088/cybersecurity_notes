
# Aggregate functions

[[🏷️SQL]]

In SQL, aggregate functions are functions that perform a calculation over multiple data points and return the result of the calculation. The actual data is not returned.

There are various aggregate functions that perform different calculations:

- `COUNT` returns a single number that represents the number of rows returned from your query.
    
- `AVG` returns a single number that represents the average of the numerical data in a column.
    
- `SUM` returns a single number that represents the sum of the numerical data in a column.

## Aggregate function syntax

To use an aggregate function, place the keyword for it after the `SELECT` keyword, and then in parentheses, indicate the column you want to perform the calculation on.

For example, when working with the `customers` table, you can use aggregate functions to summarize important information about the table. If you want to find out how many customers there are in total, you can use the `COUNT` function on any column, and SQL will return the total number of records, excluding `NULL` values. You can run this query and explore its output:

```sql
SELECT COUNT(firstname)
FROM customers;
```

```
+------------------+
| COUNT(firstname) |
+------------------+
|               59 |
+------------------+
```

The result is a table with one column titled `COUNT(firstname)` and one row that indicates the count.

If you want to find the number of customers from a specific country, you can add a filter to your query:

```sql
SELECT COUNT(firstname)
FROM customers
WHERE country = 'USA';
```

```
+------------------+
| COUNT(firstname) |
+------------------+
|               13 |
+------------------+
```

With this filter, the count is lower because it only includes the records where the `country` column contains a value of '`USA`'.

There are a lot of other aggregate functions in SQL. The syntax of placing them after `SELECT` is exactly the same as the `COUNT` function.