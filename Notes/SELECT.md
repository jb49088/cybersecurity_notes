
# Select

[[🏷️SQL]]

The `SELECT` keyword specifies which columns to include in the query results. For example, to return just the `customerid` column from a table named `customers` you would write:

```sql
SELECT customerid
FROM customers;
```

To select multiple columns, separate them with commas. For example, to return both `customerid` and `city`, you would write:

```sql
SELECT customerid, city
FROM customers;
```

If you want to return all columns from a table, use an asterisk (`*`) after `SELECT`. The query would be:

```sql
SELECT *
FROM customers;
```

> [!note] 
> Be cautious when using `SELECT *`, especially with large databases and tables. This approach can lead to a cluttered result set and may slow down query performance.