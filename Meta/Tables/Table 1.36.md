| **Operator** | **Syntax**  | **Example**                                | **Description**                    |
| ------------ | ----------- | ------------------------------------------ | ---------------------------------- |
| **AND**      | **and, &&** | tcpdump -n src 192.168.1.1 and dst port 21 | Combine filtering options          |
| **OR**       | **or, \|**  | tcpdump dst 10.1.1.1 \| !icmp              | Either of the condition can match  |
| **EXCEPT**   | **not, !**  | tcpdump dst 10.1.1.1 and not icmp          | Negation of the condition          |
| **LESS**     | **<**       | tcpdump <32                                | Shows packets size less than 32    |
| **GREATER**  | **>**       | tcpdump >=32                               | Shows packets size greater than 32 |