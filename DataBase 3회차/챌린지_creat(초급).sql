-- employees 테이블을 생성해주세요

CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    position VARCHAR(100),
    salary DECIMAL(10, 2)
);
-- 1. **원 데이터를 `employees`에 추가해주세요**
   /* - 이름: 혜린, 직책: PM, 연봉: 90000
    - 이름: 은우, 직책: Frontend, 연봉: 80000
    - 이름: 가을, 직책: Backend, 연봉: 92000
    - 이름: 지수, 직책: Frontend, 연봉: 78000
    - 이름: 민혁, 직책: Frontend, 연봉: 96000
    - 이름: 하온, 직책: Backend, 연봉: 130000 */
    
INSERT INTO employees (name, position, salary) VALUES ('혜린', 'PM', 90000);
INSERT INTO employees (name, position, salary) VALUES ('은우', 'Frontend', 80000);
INSERT INTO employees (name, position, salary) VALUES ('가을', 'Backend', 92000);
INSERT INTO employees (name, position, salary) VALUES ('지수', 'Frontend', 78000);
INSERT INTO employees (name, position, salary) VALUES ('민혁', 'Frontend', 96000);
INSERT INTO employees (name, position, salary) VALUES ('하온', 'Backend', 130000);

-- 모든 직원의 이름과 연봉 정보만을 조회하는 쿼리를 작성해주세요
SELECT * FROM employees;

-- Frontend 직책을 가진 직원 중에서 연봉이 90000 이하인 직원의 이름과 연봉을 조회하세요.
SELECT name, salary FROM employees WHERE position = 'Frontend' AND salary <= 90000;

-- 업데이트함, salrary를 salary * 1.10 즉 110%로 바꿈, 포지션은 PM인 애들만
UPDATE employees SET salary = salary * 1.10 WHERE position = 'PM';
-- 업데이트함, salrary를 salary * 1.05 즉 105%로 바꿈, 포지션은 bacnend인 애들만
UPDATE employees SET salary = salary * 1.05 WHERE position = 'Backend';
-- 폼 삭제함 민혁이라는 이름 가진 데이터를
DELETE FROM employees WHERE name = '민혁';
-- 모든 직원을 position 별로 그룹화하여 각 직책의 평균 연봉을 계산하세요.
-- 안전모드 해제
SET SQL_SAFE_UPDATES = 0;
-- employees 테이블을 삭제하세요.
DROP TABLE employees;