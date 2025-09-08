
# Relational database

A relational database is a type of database model that stores and organizes data in tables, or "relations," that are linked by predefined relationships. In this model, data is structured into rows and columns, with each table representing a specific entity or concept. Each row, known as a **record**, contains data related to a single item, while each column, known as an **attribute**, contains data related to specific characteristics of that item. Relationships between tables are established through **foreign keys**, which reference primary keys in other tables.

The relational model is based on set theory and first-order predicate logic, allowing users to query and manipulate data using a standard language called **SQL (Structured Query Language)**. This makes relational databases flexible, powerful, and widely adopted in a variety of applications.

## Tables

Think of tables like lists. Each table is a list of similar items:

- **Table Name:** "Students"
- **Columns:** Name, Age, Grade

![[Table 1.51]]

## Primary Key

A primary key is like a unique ID card for each row. It’s a special column that ensures each row is different from the others:

- **Table Name:** "Students"
- **Primary Key Column:** `StudentID`

![[Table 1.52|no-link no-title clean]]

Here, `StudentID` is the primary key. Each student’s ID is unique.

## Foreign Keys

A foreign key is a way to link tables together. Imagine you have another table for "Classes" that lists the classes each student is taking. You want to connect this table to the "Students" table.

- **Table Name:** "Classes"
- **Primary Key Column:** `ClassID` (this uniquely identifies each class record in the "Classes" table)
- **Foreign Key Column:** `StudentID` (this references the `StudentID` in the "Students" table)

![[Table 1.53|no-link no-title clean]]

Here, `StudentID` in the "Classes" table is a foreign key that refers to `StudentID` in the "Students" table. It tells you which student is taking which class. 

> [!note]
> A table can only have one primary key, but multiple foreign keys.

---

See also:

- [[Hierarchical database]]
- [[Network database]]
- [[Data]]
- [[Structured Query Language (SQL)]]