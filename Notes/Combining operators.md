
# Combining operators

[[🏷️SQL]]

Logical operators can be combined in filters. For example, if you know that both the USA and Canada are not affected by a cybersecurity issue, you can combine operators to return customers in all countries besides these two. In the following query, `NOT` is placed before the first condition, it's joined to a second condition with `AND`, and then `NOT` is also placed before that second condition. You can run it to explore what it returns:

```sql
SELECT firstname, lastname, email, country
FROM customers
WHERE NOT country = 'Canada' AND NOT country = 'USA';
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
