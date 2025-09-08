
# WHERE

[[🏷️SQL]]

To create a filter in SQL, you need to use the keyword `WHERE`. `WHERE` indicates the condition for a filter.

If you needed to email all employees with a title of IT Staff, you might use a query like this:

```sql
SELECT firstname, lastname, title, email
FROM employees
WHERE title = 'IT Staff';
```

```
+-----------+----------+----------+------------------------+
| firstname | lastname | title    | email                  |
+-----------+----------+----------+------------------------+
| Robert    | King     | IT Staff | robert@chinookcorp.com |
| Laura     | Callahan | IT Staff | laura@chinookcorp.com  |
+-----------+----------+----------+------------------------+
```

Rather than returning all records in the `employee` table, this `WHERE` clause instructs SQL to return only those that contain `'IT Staff'` in the `title` column. It uses the equals sign (`=`) operator to set this condition.
