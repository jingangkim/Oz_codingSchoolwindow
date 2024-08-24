-- customers 테이블에 새 고객 추가
INSERT INTO customers (lastname, firstname)
VALUES ('jingang', 'kim');
-- products 테이블에 새 제품 추가
INSERT INTO products (name, price)
VALUES ('toy jg', 2000);
-- employees 테이블에 새 직원을 추가하세요.
INSERT INTO employees (firstName, lastName)
VALUES ('kim', 'mingang');
-- offices 테이블에 새 사무실을 추가하세요.
INSERT INTO offices (city)
VALUES ('seoul');
-- orders 테이블에 새 주문을 추가하세요.
INSERT INTO orders (orderDate)
VALUES ('car');
-- orderdetails 테이블에 주문 상세 정보를 추가하세요.
INSERT INTO orderdetails (color)
VALUES ('red');
-- payments 테이블에 지불 정보를 추가하세요.
INSERT INTO payments (customerId, orderDate, price)
VALUES (5, 'car', 20000);
-- productlines 테이블에 제품 라인을 추가하세요.
INSERT INTO productlines (productLine)
VALUES ('Happy Cars');
-- customers 테이블에 다른 지역의 고객을 추가하세요.
INSERT INTO customers (lastname, firstname, city)
VALUES ('mini', 'jin', 'busan');
-- (10) products 테이블에 다른 카테고리의 제품을 추가하세요.
INSERT INTO products (name, pirce, productsline)
VALUES ('toy jin', 3000, 'new');

-- customers 테이블에서 모든 고객 정보를 조회하세요.
SELECT * FROM customers;
-- products 테이블에서 모든 제품 목록을 조회하세요.
SELECT * FROM products;
-- employees 테이블에서 모든 직원의 이름과 직급을 조회하세요.
SELECT name, position FROM employees;
-- offices 테이블에서 모든 사무실의 위치를 조회하세요.
SELECT location FROM offices;
-- order 테이블에서 최근 10개의 주문을 조회하세요.
SELECT orderData FROM orders LIMIT 10;
-- **`orderdetails`** 테이블에서 특정 주문의 모든 상세 정보를 조회하세요.
SELECT * FROM orderdetails WHERE customOder;
-- (7) **`payments`** 테이블에서 특정 고객의 모든 지불 정보를 조회하세요.
SELECT * FROM payments WHERE customUser;
-- (8) **`productlines`** 테이블에서 각 제품 라인의 설명을 조회하세요.
SELECT productline, 설명 FROM productlines;
-- (9) **`customers`** 테이블에서 특정 지역의 고객을 조회하세요.
SELECT customer FROM customers WHERE 'seoul';
-- (10) **`products`** 테이블에서 특정 가격 범위의 제품을 조회하세요.
SELECT products FROM products WHERE price BETWEEN 100 and 1000;
-- (1) **`customers`** 테이블에서 특정 고객의 주소를 갱신하세요.
UPDATE customers
SET customer_city = 'busan'
WHERE customer_name ='jingangkim';
-- (2) **`products`** 테이블에서 특정 제품의 가격을 갱신하세요.
UPDATE products
SET product_price = product_price * 1.5
WHERE productLine ='toy';
-- (3) **`employees`** 테이블에서 특정 직원의 직급을 갱신하세요.
UPDATE employees
SET employees_직급 = '바꿀 직급'
WHERE employees_ID = 5;
-- (4) **`offices`** 테이블에서 특정 사무실의 전화번호를 갱신하세요.
UPDATE offices
SET offices_넘버 = '010232132134'
WHERE offices_사무실위치 = 'seoul';
-- (5) **`orders`** 테이블에서 특정 주문의 상태를 갱신하세요.
UPDATE orders
SET order_상태 = 'lemon'
WHERE order_넘버 = 123;
-- (6) **`orderdetails`** 테이블에서 특정 주문 상세의 수량을 갱신하세요.
UPDATE orderdetails
SET orderdetail_수량 = orderdetail_수량 - 2
WHERE order_넘버 = 123;
-- (7) **`payments`** 테이블에서 특정 지불의 금액을 갱신하세요.
UPDATE payments
SET payment_price = 15000
WHERE payment_id = 123;
-- (8) **`productlines`** 테이블에서 특정 제품 라인의 설명을 갱신하세요.
UPDATE productlines
SET productline_설명 = '어쩌구저쩌구'
WHERE productlines = '특정 제품명';
-- (9) **`customers`** 테이블에서 특정 고객의 이메일을 갱신하세요.
UPDATE customers
SET customerEmail = 'unginroe4534@naver.com'
WHERE customerId = '특정고객번호'
-- (10) products 테이블에서 여러 제품의 가격을 한 번에 갱신하세요.
UPDATE products
SET Price = price * 1.5;
-- (1) **`customers`** 테이블에서 특정 고객을 삭제하세요.
DELETE FROM customers
WHERE customerid = 86;
-- (2) **`products`** 테이블에서 특정 제품을 삭제하세요.
DELETE FROM products
WHERE productName = 'toy';
-- (3) **`employees`** 테이블에서 특정 직원을 삭제하세요.
DELETE FROM employees
WHERE employeesNumber = 848;
-- (4) **`offices`** 테이블에서 특정 사무실을 삭제하세요.
DELETE FROM offices
WHERE officeCity = 'jeju';
-- (5) **`orders`** 테이블에서 특정 주문을 삭제하세요.
DELETE FROM orders
WHERE orderNumber = 291;
-- (6) **`orderdetails`** 테이블에서 특정 주문 상세를 삭제하세요.
DELETE FROM orderdetails
WHERE orderdetailNumber = 12;
-- (7) **`payments`** 테이블에서 특정 지불 내역을 삭제하세요.
DELETE FROM payments
WHERE paymentNumber = 131;
-- (8) **`productlines`** 테이블에서 특정 제품 라인을 삭제하세요.
DELETE FROM productlines
WHERE productline = '특정 제품명';
-- (9) **`customers`** 테이블에서 특정 지역의 모든 고객을 삭제하세요.
DELETE FROM customers
WHERE customerCity = 'dokdo';
-- (10) **`products`** 테이블에서 특정 카테고리의 모든 제품을 삭제하세요.
DELETE FROM products
WHERE product카테고리 = '카테고리명';