
# ORDER BY

[[🏷️SQL]]

`ORDER BY` sequences the records returned by a query based on a specified column or columns. This can be in either ascending or descending order.

## Sorting in ascending order

To use the `ORDER BY` keyword, write it at the end of the query and specify a column to base the sort on. In this example, SQL will return the `customerid`, `city`, and `country` columns from the `customers` table, and the records will be sequenced by the `city` column from A to Z:

```sql
SELECT customerid, city, country
FROM customers
ORDER BY city;
```

```
+------------+--------------+----------------+
| customerid | city         | country        |
+------------+--------------+----------------+
|         48 | Amsterdam    | Netherlands    |
|         59 | Bangalore    | India          |
|         36 | Berlin       | Germany        |
|         38 | Berlin       | Germany        |
|         42 | Bordeaux     | France         |
|         23 | Boston       | USA            |
|         13 | Brasília     | Brazil         |
|          8 | Brussels     | Belgium        |
|         45 | Budapest     | Hungary        |
|         56 | Buenos Aires | Argentina      |
|         24 | Chicago      | USA            |
|          9 | Copenhagen   | Denmark        |
|         19 | Cupertino    | USA            |
|         58 | Delhi        | India          |
|         43 | Dijon        | France         |
|         46 | Dublin       | Ireland        |
|         54 | Edinburgh    | United Kingdom |
|         14 | Edmonton     | Canada         |
|         26 | Fort Worth   | USA            |
|         37 | Frankfurt    | Germany        |
|         31 | Halifax      | Canada         |
|         44 | Helsinki     | Finland        |
|         34 | Lisbon       | Portugal       |
|         52 | London       | United Kingdom |
|         53 | London       | United Kingdom |
+------------+--------------+----------------+
(Output limit exceeded, 25 of 59 total rows shown)
```

The `ORDER BY` keyword sorts the records based on the column specified after this keyword. By default, as shown in this example, the sequence will be in ascending order. This means

- if you choose a column containing numeric data, it sorts the output from the smallest to largest. For example, if sorting on `customerid`, the ID numbers are sorted from smallest to largest.
- if the column contains alphabetic characters, such as in the example with the `city` column, it orders the records from A to Z.

## Sorting in descending order

You can also use the `ORDER BY` with the `DESC` keyword to sort in descending order. The `DESC` keyword is short for "descending" and tells SQL to sort numbers from largest to smallest, or alphabetically from Z to A:

```sql
SELECT customerid, city, country
FROM customers
ORDER BY city DESC;
```

```
+------------+---------------------+----------------+
| customerid | city                | country        |
+------------+---------------------+----------------+
|         33 | Yellowknife         | Canada         |
|         32 | Winnipeg            | Canada         |
|         49 | Warsaw              | Poland         |
|          7 | Vienne              | Austria        |
|         15 | Vancouver           | Canada         |
|         27 | Tucson              | USA            |
|         29 | Toronto             | Canada         |
|         10 | São Paulo           | Brazil         |
|         11 | São Paulo           | Brazil         |
|          1 | São José dos Campos | Brazil         |
|          2 | Stuttgart           | Germany        |
|         51 | Stockholm           | Sweden         |
|         55 | Sidney              | Australia      |
|         57 | Santiago            | Chile          |
|         28 | Salt Lake City      | USA            |
|         47 | Rome                | Italy          |
|         12 | Rio de Janeiro      | Brazil         |
|         21 | Reno                | USA            |
|         17 | Redmond             | USA            |
|          5 | Prague              | Czech Republic |
|          6 | Prague              | Czech Republic |
|         35 | Porto               | Portugal       |
|         39 | Paris               | France         |
|         40 | Paris               | France         |
|         30 | Ottawa              | Canada         |
+------------+---------------------+----------------+
(Output limit exceeded, 25 of 59 total rows shown)
```

Now, cities at the end of the alphabet are listed first.

## Sorting based on multiple columns

You can also choose multiple columns to order by. For example, you might first choose the `country` and then the `city` column. SQL then sorts the output by `country`, and for rows with the same `country`, it sorts them based on `city`. You can run this to explore how SQL displays this:

```sql
SELECT customerid, city, country
FROM customers
ORDER BY country, city;
```

```
+------------+---------------------+----------------+
| customerid | city                | country        |
+------------+---------------------+----------------+
|         56 | Buenos Aires        | Argentina      |
|         55 | Sidney              | Australia      |
|          7 | Vienne              | Austria        |
|          8 | Brussels            | Belgium        |
|         13 | Brasília            | Brazil         |
|         12 | Rio de Janeiro      | Brazil         |
|          1 | São José dos Campos | Brazil         |
|         10 | São Paulo           | Brazil         |
|         11 | São Paulo           | Brazil         |
|         14 | Edmonton            | Canada         |
|         31 | Halifax             | Canada         |
|          3 | Montréal            | Canada         |
|         30 | Ottawa              | Canada         |
|         29 | Toronto             | Canada         |
|         15 | Vancouver           | Canada         |
|         32 | Winnipeg            | Canada         |
|         33 | Yellowknife         | Canada         |
|         57 | Santiago            | Chile          |
|          5 | Prague              | Czech Republic |
|          6 | Prague              | Czech Republic |
|          9 | Copenhagen          | Denmark        |
|         44 | Helsinki            | Finland        |
|         42 | Bordeaux            | France         |
|         43 | Dijon               | France         |
|         41 | Lyon                | France         |
+------------+---------------------+----------------+
(Output limit exceeded, 25 of 59 total rows shown)
```