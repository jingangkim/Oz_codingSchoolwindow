

#CREATE DATABASE fishbread_db;
#USE fishbread_db;

CREATE TABLE users (
	user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    email VARCHAR(100) UNIQUE,
    is_business VARCHAR(10) DEFAULT False
    );
    
CREATE TABLE orders (
	order_id INT PRIMARY KEY auto_increment,
    user_id INT, FOREIGN KEY (user_id) REFERENCES users(user_id),
    order_date DATE,
    amount DECIMAL(10, 2)
    );
    
CREATE TABLE inventory (
	item_id INT PRIMARY KEY AUTO_INCREMENT,
    item_name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL
    );
    
CREATE TABLE sales (
	sale_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT, FOREIGN KEY (order_id) REFERENCES orders (order_id),
    item_id INT, FOREIGN KEY (item_id) REFERENCES inventory(item_id),
    quanfity_sold INT NOT NULL);
    
CREATE TABLE daily_sales (
date DATE PRIMARY KEY,
total_sales DECIMAL(10,2) NOT null);