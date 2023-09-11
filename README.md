# MySQL Codes

Python can be used in database applications. One of the most popular databases is MySQL.

**MySQL Database:** To be able to experiment with the code examples in this tutorial, you should have MySQL installed on your computer. You can download a MySQL database at https://www.mysql.com/downloads/.

**Creating Data Base**
> CREATE DATABASE mydatabase;

**Switching to a Database:**
> USE mydatabase;

**Creating a Table:**

>CREATE TABLE users (
>    id INT AUTO_INCREMENT PRIMARY KEY,
>    username VARCHAR(255),
>    email VARCHAR(255)
>);

**Inserting Data into a Table:**

>INSERT INTO users (username, email)
>VALUES ('john_doe', 'john@example.com');

**Querying Data from a Table:**

> SELECT * FROM users;

**Updating Data in a Table:**

>UPDATE users
>SET email = 'new_email@example.com'
>WHERE id = 1;


**Deleting Data from a Table:**

>DELETE FROM users
>WHERE id = 1;

**Altering a Table (Adding a Column):**

>ALTER TABLE users
>ADD COLUMN age INT;

**Dropping a Database:**

> DROP DATABASE mydatabase;

**Creating an Index:**

> CREATE INDEX idx_username ON users (username);

**Joining Tables (INNER JOIN):**

> SELECT users.username, orders.order_date
> FROM users
> INNER JOIN orders ON users.id = orders.user_id;

**Using WHERE Clause:**

>SELECT * FROM users
>WHERE age > 25;

**Using GROUP BY with Aggregate Functions:**

> SELECT department, AVG(salary) AS avg_salary
> FROM employees
> GROUP BY department;

**Using ORDER BY:**

> SELECT * FROM products
> ORDER BY price DESC;

**Limiting Results:**

> SELECT * FROM products
> LIMIT 10;

**Using Subqueries:**

> SELECT name
> FROM employees
> WHERE salary > (SELECT AVG(salary) FROM employees);
