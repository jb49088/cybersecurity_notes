| **Category**        | SQL **Command**          | **Description**                                                                | 
| ------------------- | ------------------------ | ------------------------------------------------------------------------------ |
| Data Query          | `SELECT`                 | Retrieves data from one or more tables.                                        |
| Data Query          | `SELECT DISTINCT`        | Retrieves unique rows from a query.                                            |
| Data Query          | `SELECT INTO`            | Copies data from a table into a new table.                                     |
| Data Query          | `EXISTS`                 | Tests for the existence of rows in a subquery.                                 |
| Data Query          | `JOIN`                   | Combines rows from two or more tables based on a related column.               |
| Data Query          | `INNER JOIN`             | Retrieves rows with matching values in both tables.                            |
| Data Query          | `LEFT JOIN`              | Retrieves all rows from the left table and matching rows from the right table. |
| Data Query          | `RIGHT JOIN`             | Retrieves all rows from the right table and matching rows from the left table. |
| Data Query          | `FULL OUTER JOIN`        | Retrieves all rows when there is a match in one of the tables.                 |
| Data Query          | `CROSS JOIN`             | Produces a Cartesian product of two tables.                                    |
| Data Manipulation   | `INSERT`                 | Adds new rows to a table.                                                      |
| Data Manipulation   | `INSERT INTO ... SELECT` | Inserts rows selected from another table.                                      |
| Data Manipulation   | `UPDATE`                 | Modifies existing data in a table.                                             |
| Data Manipulation   | `DELETE`                 | Removes rows from a table.                                                     |
| Data Manipulation   | `MERGE`                  | Performs `INSERT`, `UPDATE`, or `DELETE` operations in a single statement.     |
| Data Definition     | `CREATE TABLE`           | Creates a new table in the database.                                           |
| Data Definition     | `ALTER TABLE`            | Modifies an existing table structure.                                          |
| Data Definition     | `DROP TABLE`             | Deletes a table and its data.                                                  |
| Data Definition     | `TRUNCATE TABLE`         | Removes all rows from a table but retains its structure.                       |
| Data Definition     | `CREATE DATABASE`        | Creates a new database.                                                        |
| Data Definition     | `DROP DATABASE`          | Deletes a database and all its tables.                                         |
| Data Definition     | `CREATE INDEX`           | Creates an index (search key).                                                 |
| Data Definition     | `DROP INDEX`             | Deletes an index.                                                              |
| Data Definition     | `CREATE VIEW`            | Creates a virtual table based on a query.                                      |
| Data Definition     | `DROP VIEW`              | Deletes a view.                                                                |
| Data Definition     | `CREATE PROCEDURE`       | Defines a stored procedure.                                                    |
| Data Definition     | `ALTER PROCEDURE`        | Modifies an existing stored procedure.                                         |
| Data Definition     | `DROP PROCEDURE`         | Deletes a stored procedure.                                                    |
| Data Definition     | `CREATE FUNCTION`        | Defines a user-defined function.                                               |
| Data Definition     | `ALTER FUNCTION`         | Modifies an existing function.                                                 |
| Data Definition     | `DROP FUNCTION`          | Deletes a function.                                                            |
| Data Definition     | `CREATE TRIGGER`         | Defines a trigger to execute a set of instructions in response to an event.    |
| Data Definition     | `DROP TRIGGER`           | Deletes a trigger.                                                             |
| Data Definition     | `CREATE SEQUENCE`        | Creates a sequence generator for unique values.                                |
| Data Definition     | `ALTER SEQUENCE`         | Modifies an existing sequence.                                                 |
| Data Definition     | `DROP SEQUENCE`          | Deletes a sequence.                                                            |
| Data Control        | `GRANT`                  | Provides privileges to users.                                                  |
| Data Control        | `REVOKE`                 | Removes privileges from users.                                                 |
| Data Control        | `DENY`                   | Explicitly denies permissions to a user or role.                               |
| Transaction Control | `BEGIN TRANSACTION`      | Starts a new transaction.                                                      |
| Transaction Control | `COMMIT`                 | Saves all changes made during the transaction.                                 |
| Transaction Control | `ROLLBACK`               | Undoes changes made during the transaction.                                    |
| Transaction Control | `SAVEPOINT`              | Sets a point within a transaction to which you can later roll back.            |
| Transaction Control | `SET TRANSACTION`        | Configures the properties of a transaction.                                    |
| Others              | `SHOW`                   | Displays database objects and settings (syntax varies by database).            |
| Others              | `DESCRIBE`               | Provides details about table structure (e.g., column names and types).         |
| Others              | `EXPLAIN`                | Provides execution plan of a query (syntax may vary by database).              |
| Others              | `ANALYZE`                | Gathers statistics about data distribution for query optimization.             |
| Others              | `USE`                    | Selects a database to use.                                                     |
| Others              | `RENAME`                 | Renames a table or column (syntax may vary by database).                       |
| Others              | `LOCK TABLE`             | Locks a table to control concurrent access.                                    |
