
# LIKE

[[🏷️SQL]]

To apply wildcards, you need to use the `LIKE` operator instead of an equals sign (`=`). `LIKE` is used with `WHERE` to search for a pattern in a column.

For instance, if you want to email employees with a title of either `'IT Staff'` or `'IT Manager'`, you can use `LIKE` operator combined with the `%` wildcard:

```sql
SELECT lastname, firstname, title, email
FROM employees
WHERE title LIKE 'IT%';
```

```
+----------+-----------+------------+-------------------------+
| lastname | firstname | title      | email                   |
+----------+-----------+------------+-------------------------+
| Mitchell | Michael   | IT Manager | michael@chinookcorp.com |
| King     | Robert    | IT Staff   | robert@chinookcorp.com  |
| Callahan | Laura     | IT Staff   | laura@chinookcorp.com   |
+----------+-----------+------------+-------------------------+
```

This query returns all records with values in the `title` column that start with the pattern of `'IT'`. This means both `'IT Staff'` and `'IT Manager'` are returned.

