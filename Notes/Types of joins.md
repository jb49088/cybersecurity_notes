
# Types of joins

Welcome back. I hope you enjoyed working on inner joins. In the previous video and exercises, we saw how inner joins can be useful by only returning records that share a value in specify columns. However, in some situations, we might need all of the entries from one or both of our tables. This is where we need to use outer joins.

There are three types of outer joins: LEFT JOIN, RIGHT JOIN, and FULL OUTER JOIN. Similar to inner joins, outer joins combine two tables together; however, they don't necessarily need a match between columns to return a row. Which rows are returned depends on the type of join.

LEFT JOIN returns all of the records of the first table, but only returns rows of the second table that match on a specified column. Like we did in the previous video, let's examine this type of join by looking at just four rows of two tables with a small number of columns. Employees is the left table, or the first table, and machines is the right table, or the second table. 

![[Table 1.57|no-link no-title clean]]

Let's join on employee_id. There's a matching value in this column for two of the four records. When we execute the join, SQL returns these rows with the matching value, all other rows from the left table, and all columns from both tables. 

![[Table 1.59|no-link no-title clean]]

Records from the employees table that didn't match but were returned through the LEFT JOIN contain NULL values in columns that came from the machines table. Next, let's talk about right joins.

RIGHT JOIN returns all of the records of the second table but only returns rows from the first table that match on a specified column. 

With a RIGHT JOIN on the previous example, the full result returns matching rows from both, all the rows from the second table, and all the columns in both tables. 

![[Table 1.60|no-link no-title clean]]

For the values that don't exist in either table, we are left with a NULL value. Last, we'll discuss full outer joins.

FULL OUTER JOIN returns all records from both tables. Using our same example, a FULL OUTER JOIN returns all columns from all tables. If a row doesn't have a value for a particular column, it returns NULL. 

![[Table 1.61|no-link no-title clean]]

For example, the machines table do not have any rows with employee_id 1190, so the values for that row and the columns that came from the machines table is NULL. To implement left joins, right joins, and full outer joins in SQL, you use the same syntax structure as the INNER JOIN but use these keywords: LEFT JOIN, RIGHT JOIN, and FULL OUTER JOIN.

As a security analyst, you're not required to know all of these from memory. Once you understand the type of join you need, you can quickly search and find all the information you need to execute these queries. With this information on joins, we've now covered some very important information you'll need as a security analyst using SQL. Thank you for joining me in this video.