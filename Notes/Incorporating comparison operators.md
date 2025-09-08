
# Incorporating comparison operators

[[🏷️SQL]]

These comparison operators are used in the `WHERE` clause at the end of a query. The following query uses the `>` operator to filter the `birthdate` column. You can run this query to explore its output:

```sql
SELECT firstname, lastname, birthdate
FROM employees
WHERE birthdate > '1970-01-01';
```

```
+-----------+----------+---------------------+
| FirstName | LastName | BirthDate           |
+-----------+----------+---------------------+
| Jane      | Peacock  | 1973-08-29 00:00:00 |
| Michael   | Mitchell | 1973-07-01 00:00:00 |
| Robert    | King     | 1970-05-29 00:00:00 |
+-----------+----------+---------------------+
```

This query returns the first and last names of employees born after, but not on, `1970-01-01` (or January 1, 1970). If you were to use the `>=` operator instead, the results would also include results on exactly `1970-01-01`.

In other words, the `>` operator is exclusive and the `>=` operator is inclusive. An exclusive operator is an operator that does not include the value of comparison. An inclusive operator is an operator that includes the value of comparison.
