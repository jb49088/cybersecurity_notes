
# More on filters with AND, OR, and NOT

Previously, you explored how to add filters containing the `AND`, `OR`, and `NOT` operators to your SQL queries. In this reading, you'll continue to explore how these operators can help you refine your queries.

## Logical operators

`AND`, `OR`, and `NOT` allow you to filter your queries to return the specific information that will help you in your work as a security analyst. They are all considered logical operators.

### AND

First, `AND` is used to filter on two conditions. `AND` specifies that both conditions must be met simultaneously.

As an example, a cybersecurity concern might affect only those customer accounts that meet both the condition of being handled by a support representative with an ID of 5 and the condition of being located in the USA. To find the names and emails of those specific customers, you should place the two conditions on either side of the `AND` operator in the `WHERE` clause:

```sql
SELECT firstname, lastname, email, country, supportrepid
FROM customers
WHERE supportrepid = 5 AND country = 'USA';
```

```
+-----------+----------+-------------------------+---------+--------------+
| FirstName | LastName | Email                   | Country | SupportRepId |
+-----------+----------+-------------------------+---------+--------------+
| Jack      | Smith    | jacksmith@microsoft.com | USA     |            5 |
| Kathy     | Chase    | kachase@hotmail.com     | USA     |            5 |
| Victor    | Stevens  | vstevens@yahoo.com      | USA     |            5 |
| Julia     | Barnett  | jubarnett@gmail.com     | USA     |            5 |
+-----------+----------+-------------------------+---------+--------------+
```

Running this query returns four rows of information about the customers. You can use this information to contact them about the security concern.

### OR

The `OR` operator also connects two conditions, but `OR` specifies that either condition can be met. It returns results where the first condition, the second condition, or both are met.

For example, if you are responsible for finding all customers who are either in the USA or Canada so that you can communicate information about a security update, you can use an `OR` operator to find all the needed records. As the following query demonstrates, you should place the two conditions on either side of the `OR` operator in the `WHERE` clause:

```sql
SELECT firstname, lastname, email, country
FROM customers
WHERE country = 'Canada' OR country = 'USA';
```

```
+-----------+------------+--------------------------+---------+
| FirstName | LastName   | Email                    | Country |
+-----------+------------+--------------------------+---------+
| François  | Tremblay   | ftremblay@gmail.com      | Canada  |
| Mark      | Philips    | mphilips12@shaw.ca       | Canada  |
| Jennifer  | Peterson   | jenniferp@rogers.ca      | Canada  |
| Frank     | Harris     | fharris@google.com       | USA     |
| Jack      | Smith      | jacksmith@microsoft.com  | USA     |
| Michelle  | Brooks     | michelleb@aol.com        | USA     |
| Tim       | Goyer      | tgoyer@apple.com         | USA     |
| Dan       | Miller     | dmiller@comcast.com      | USA     |
| Kathy     | Chase      | kachase@hotmail.com      | USA     |
| Heather   | Leacock    | hleacock@gmail.com       | USA     |
| John      | Gordon     | johngordon22@yahoo.com   | USA     |
| Frank     | Ralston    | fralston@gmail.com       | USA     |
| Victor    | Stevens    | vstevens@yahoo.com       | USA     |
| Richard   | Cunningham | ricunningham@hotmail.com | USA     |
| Patrick   | Gray       | patrick.gray@aol.com     | USA     |
| Julia     | Barnett    | jubarnett@gmail.com      | USA     |
| Robert    | Brown      | robbrown@shaw.ca         | Canada  |
| Edward    | Francis    | edfrancis@yachoo.ca      | Canada  |
| Martha    | Silk       | marthasilk@gmail.com     | Canada  |
| Aaron     | Mitchell   | aaronmitchell@yahoo.ca   | Canada  |
| Ellie     | Sullivan   | ellie.sullivan@shaw.ca   | Canada  |
+-----------+------------+--------------------------+---------+
```

The query returns all customers in either the US or Canada.

> [!note]
> Even if both conditions are based on the same column, you need to write out both full conditions. For instance, the query in the previous example contains the filter `WHERE country = 'Canada' OR country = 'USA'`.

### NOT

Unlike the previous two operators, the `NOT` operator only works on a single condition, and not on multiple ones. The `NOT` operator negates a condition. This means that SQL returns all records that don’t match the condition specified in the query.

For example, if a cybersecurity issue doesn't affect customers in the USA but might affect those in other countries, you can return all customers who are not in the USA. This would be more efficient than creating individual conditions for all of the other countries. To use the `NOT` operator for this task, write the following query and place `NOT` directly after `WHERE`:

```sql
SELECT firstname, lastname, email, country
FROM customers
WHERE NOT country = 'USA';
```

```
+-----------+-------------+-------------------------------+----------------+
| FirstName | LastName    | Email                         | Country        |
+-----------+-------------+-------------------------------+----------------+
| Luís      | Gonçalves   | luisg@embraer.com.br          | Brazil         |
| Leonie    | Köhler      | leonekohler@surfeu.de         | Germany        |
| François  | Tremblay    | ftremblay@gmail.com           | Canada         |
| Bjørn     | Hansen      | bjorn.hansen@yahoo.no         | Norway         |
| František | Wichterlová | frantisekw@jetbrains.com      | Czech Republic |
| Helena    | Holý        | hholy@gmail.com               | Czech Republic |
| Astrid    | Gruber      | astrid.gruber@apple.at        | Austria        |
| Daan      | Peeters     | daan_peeters@apple.be         | Belgium        |
| Kara      | Nielsen     | kara.nielsen@jubii.dk         | Denmark        |
| Eduardo   | Martins     | eduardo@woodstock.com.br      | Brazil         |
| Alexandre | Rocha       | alero@uol.com.br              | Brazil         |
| Roberto   | Almeida     | roberto.almeida@riotur.gov.br | Brazil         |
| Fernanda  | Ramos       | fernadaramos4@uol.com.br      | Brazil         |
| Mark      | Philips     | mphilips12@shaw.ca            | Canada         |
| Jennifer  | Peterson    | jenniferp@rogers.ca           | Canada         |
| Robert    | Brown       | robbrown@shaw.ca              | Canada         |
| Edward    | Francis     | edfrancis@yachoo.ca           | Canada         |
| Martha    | Silk        | marthasilk@gmail.com          | Canada         |
| Aaron     | Mitchell    | aaronmitchell@yahoo.ca        | Canada         |
| Ellie     | Sullivan    | ellie.sullivan@shaw.ca        | Canada         |
| João      | Fernandes   | jfernandes@yahoo.pt           | Portugal       |
| Madalena  | Sampaio     | masampaio@sapo.pt             | Portugal       |
| Hannah    | Schneider   | hannah.schneider@yahoo.de     | Germany        |
| Fynn      | Zimmermann  | fzimmermann@yahoo.de          | Germany        |
| Niklas    | Schröder    | nschroder@surfeu.de           | Germany        |
+-----------+-------------+-------------------------------+----------------+
(Output limit exceeded, 25 of 46 total rows shown)
```

SQL returns every entry where the customers are not from the USA.

> [!tip]
> Another way of finding values that are not equal to a certain value is by using the `<>` operator or the `!=` operator. For example, `WHERE country <> 'USA'` and `WHERE country != 'USA'` are the same filters as `WHERE NOT country = 'USA'`.

## Combining logical operators

Logical operators can be combined in filters. For example, if you know that both the USA and Canada are not affected by a cybersecurity issue, you can combine operators to return customers in all countries besides these two. In the following query, `NOT` is placed before the first condition, it's joined to a second condition with `AND`, and then `NOT` is also placed before that second condition. You can run it to explore what it returns:

```sql
SELECT firstname, lastname, email, country
FROM customers
WHERE NOT country = 'Canada' AND NOT country = 'USA';
```

```
+-----------+-------------+-------------------------------+----------------+
| FirstName | LastName    | Email                         | Country        |
+-----------+-------------+-------------------------------+----------------+
| Luís      | Gonçalves   | luisg@embraer.com.br          | Brazil         |
| Leonie    | Köhler      | leonekohler@surfeu.de         | Germany        |
| Bjørn     | Hansen      | bjorn.hansen@yahoo.no         | Norway         |
| František | Wichterlová | frantisekw@jetbrains.com      | Czech Republic |
| Helena    | Holý        | hholy@gmail.com               | Czech Republic |
| Astrid    | Gruber      | astrid.gruber@apple.at        | Austria        |
| Daan      | Peeters     | daan_peeters@apple.be         | Belgium        |
| Kara      | Nielsen     | kara.nielsen@jubii.dk         | Denmark        |
| Eduardo   | Martins     | eduardo@woodstock.com.br      | Brazil         |
| Alexandre | Rocha       | alero@uol.com.br              | Brazil         |
| Roberto   | Almeida     | roberto.almeida@riotur.gov.br | Brazil         |
| Fernanda  | Ramos       | fernadaramos4@uol.com.br      | Brazil         |
| João      | Fernandes   | jfernandes@yahoo.pt           | Portugal       |
| Madalena  | Sampaio     | masampaio@sapo.pt             | Portugal       |
| Hannah    | Schneider   | hannah.schneider@yahoo.de     | Germany        |
| Fynn      | Zimmermann  | fzimmermann@yahoo.de          | Germany        |
| Niklas    | Schröder    | nschroder@surfeu.de           | Germany        |
| Camille   | Bernard     | camille.bernard@yahoo.fr      | France         |
| Dominique | Lefebvre    | dominiquelefebvre@gmail.com   | France         |
| Marc      | Dubois      | marc.dubois@hotmail.com       | France         |
| Wyatt     | Girard      | wyatt.girard@yahoo.fr         | France         |
| Isabelle  | Mercier     | isabelle_mercier@apple.fr     | France         |
| Terhi     | Hämäläinen  | terhi.hamalainen@apple.fi     | Finland        |
| Ladislav  | Kovács      | ladislav_kovacs@apple.hu      | Hungary        |
| Hugh      | O'Reilly    | hughoreilly@apple.ie          | Ireland        |
+-----------+-------------+-------------------------------+----------------+
(Output limit exceeded, 25 of 38 total rows shown)
```
