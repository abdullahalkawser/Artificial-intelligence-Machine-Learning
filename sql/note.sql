✅ Types of SQL Commands

SQL commands are divided into 5 major types based on their functionality:

🔹 1. DDL (Data Definition Language)
Purpose: Defines and manages database structure (schema).

Commands:

CREATE — Create databases, tables, views.

ALTER — Modify existing table structures.

DROP — Delete tables, views, or databases.

TRUNCATE — Remove all data from a table but keep structure.




🔹 2. DML (Data Manipulation Language)
Purpose: Manipulate data inside tables.

Commands:

INSERT — Insert data into tables.

UPDATE — Update existing data.

DELETE — Delete data from tables.




🔹 3. DQL (Data Query Language)
Purpose: Query and fetch data from databases.

Command:

SELECT — Retrieve data from one or more tables.

🔹 4. DCL (Data Control Language)
Purpose: Control permissions and access rights.

Commands:

GRANT — Give privileges to users.

REVOKE — Remove privileges from users.




🔹 5. TCL (Transaction Control Language)
Purpose: Manage database transactions to maintain data integrity.

Commands:

COMMIT — Save changes permanently.

ROLLBACK — Undo changes since the last commit.

SAVEPOINT — Create savepoints within a transaction.

SET TRANSACTION — Set characteristics for a transaction.





 ✅ Database related Queries


CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;

SHOW DATABASES;
SHOW TABLES;

DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;



Table related Queries
CREATE TABLE table_name (
column_name1 datatype constraint,
column_name2 datatype constraint,
);

Table related Queries
Select & View ALL columns

SELECT * FROM table_name;


Insert
INSERT INTO table_name
(colname1, colname2);
VALUES
(col1_v1, col2_v1),
(col1_v2, col2_)

Primary Key
Foreign Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id)
There is only 1 PK & it should be NOT null.


A foreign key is a column (or set of columns) in a table that refers to the primary key in another table.
FKs can have duplicate & null values

CREATE TABLE table_name (
    column_name1 datatype PRIMARY KEY,
    column_name2 datatype,
    FOREIGN KEY (column_name2) REFERENCES other_table(other_column)
);

Select in Detail
used to select any data from the database

Basic Syntax
SELECT col1, col2 FROM table_name;
To Select ALL
SELECT * FROM table_name;


To Select Distinct Values
SELECT DISTINCT col1 FROM table_name;   

Where Clause
To define some conditions
SELECT col1, col2 FROM table_name
WHERE conditions;



Where Clause
Using Operators in WHERE

Arithmetic Operators : +(addition) , -(subtraction),
*(multiplication), /(division), %(modulus)
Using Operators in WHERE
Comparison Operators : = (equal to), != (not equal to), > , >=
, <, <=
Logical Operators : AND, OR , NOT, IN, BETWEEN, ALL, LIKE, ANY
Bitwise Operators : & (Bitwise AND), | (Bitwise OR)


Operators
AND (to check for both conditions to be true)




OR (to check for one of the conditions to be true)

Between (selects for a given range)

In (matches any value in the list)

NOT (to negate the given condition)

Limit Clause

Sets an upper limit on number of (tuples)rows to be returned

SELECT col1, col2 FROM table_name
LIMIT number;

Order By Clause

To sort in ascending (ASC) or descending order

SELECT col1, col2 FROM table_name
ORDER BY col_name(s) ASC;



Aggregate Functions

Aggregare functions perform a calculation on a set of values, and return a single value.
COUNT( )
MAX( )
MIN( )
SUM( )
AVG( )

Group By Clause
Groups rows that have the same values into summary rows.
It collects data from multiple records and groups the result by one or more column.
*Generally we use group by with some aggregation function.
Count number of students in each city


Having Clause
Similar to Where i.e. applies some condition on rows.
Used when we want to apply any condition after grouping.
Count number of students in each city where max marks cross 90.