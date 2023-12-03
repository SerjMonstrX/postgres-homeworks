-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100),
	title varchar(100) NOT NULL,
	birth_date DATE,
	notes text
);

CREATE TABLE customers
(
	customer_id int PRIMARY KEY,
	company_name varchar(100),
	fullname varchar(100)
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id int REFERENCES customers(customer_id),
	employee_id int REFERENCES employees(employee_id),
	rder_date DATE,
	ship_city varchar(100)
);