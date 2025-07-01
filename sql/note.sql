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