SELECT yes24;
-- 모든 책의 제목과 저자
SELECT title, author FROM books;
-- 평점 4점 이상
SELECT * FROM books WHERE rating >= 4.0;
-- 리뷰 100개 이상의 첵 제목, 리뷰수 조회
SELECT title, reivew WHERE review >= 100 ORDER By review DESC;
-- 가격 2만원 미만 제목 가격 조회
SELECT title, price FROM books WHERE price < 20000;
-- 국내 top100에 4주 이상 머문 책 조회
SELECT * FROM books WHERE ranking_weeks >= 4 ORDER BY ranking_weeks DESC;
-- 특정 저자의 모든 책을 조회하세요.
SELECT title FROM Books WHERE author = '김종원 저';    
-- 특정 출판사가 출판한 책들을 조회하세요.
SELECT title FROM Books WHERE publisher = '카시오페아';

-- 저자별 평균 평점은?
SELECT author, AVG(rating) FROM Books GROUP BY author;
-- 출판일별 출간된 책의 수는?
SELECT publishing, COUNT(*) FROM Books GROUP BY publishing;
-- 책 제목별 평균 가격은?
SELECT title, AVG(price) FROM Books GROUP BY title;
-- 리뷰 수가 가장 많은 상위 5권의 책은?
SELECT title, review FROM Books ORDER BY review DESC LIMIT 5;
-- 국내도서랭킹 별 평균 리뷰 수는?
SELECT ranking, AVG(review) FROM Books GROUP BY ranking;

-- 평균 평점보다 높은 평점을 받은 책들은?
SELECT title, rating FROM Books WHERE rating > (SELECT AVG(rating) FROM Books);
-- 평균 가격보다 비싼 책들의 제목과 가격은?
SELECT title, price FROM Books WHERE price > (SELECT AVG(price) FROM Books);
-- 가장 많은 리뷰를 받은 책보다 많은 리뷰를 받은 다른 책들은?
SELECT title, review FROM Books WHERE review > (SELECT MAX(review) FROM Books);
-- 평균 판매지수보다 낮은 판매지수를 가진 책들은?
SELECT title, sales FROM Books WHERE sales < (SELECT AVG(sales) FROM Books);
-- 가장 많이 출판된 저자의 책들 중 최근에 출판된 책은?
SELECT title, publishing FROM Books WHERE author = (SELECT author FROM Books GROUP BY author ORDER BY COUNT(*) DESC LIMIT 1) ORDER BY publishing DESC LIMIT 1;

-- 특정 책의 가격을 업데이트
UPDATE Books SET price = 99990 WHERE title = '이중 하나는 거짓말';
-- 특정 저자의 책 제목을 변경
UPDATE Books SET title = '새로운 이름으로 정함' WHERE author = '세이노(SayNo) 저';
-- 판매지수가 가장 낮은 책을 삭제
DELETE FROM Books WHERE sales = (SELECT MIN(sales) FROM Books);
-- 특정 출판사가 출판한 모든 책의 평점을 1점 증가
UPDATE Books SET rating = rating + 1 WHERE publisher = '데이원';

-- 저자별 평균 평점 및 판매지수를 분석하여 인기 있는 저자를 확인
SELECT author, AVG(rating) as avg_rating, AVG(sales) as avg_sales FROM Books GROUP BY author;
-- 출판일에 따른 책 가격의 변동 추세를 분석
SELECT publishing, AVG(price) as avg_price FROM Books GROUP BY publishing;
-- 출판사별 출간된 책의 수와 평균 리뷰 수를 비교 분석
SELECT publisher, COUNT(*) as num_books, AVG(review) as avg_review FROM Books GROUP BY publisher;
-- 국내도서랭킹과 판매지수의 상관관계를 분석
SELECT ranking, AVG(sales) as avg_sales FROM Books GROUP BY ranking;
-- 가격 대비 리뷰 수와 평점의 관계를 분석하여 가성비 좋은 책을 찾기
SELECT price, AVG(review) as avg_review, AVG(rating) as avg_rating FROM Books GROUP BY price;

-- 출판사별 평균 판매지수가 가장 높은 저자 찾기
SELECT publisher, author, AVG(sales) as avg_sales
FROM Books
GROUP BY publisher, author
ORDER BY publisher, avg_sales DESC;
-- 리뷰 수가 평균보다 높으면서 가격이 평균보다 낮은 책 조회
SELECT title, review, price
FROM Books
WHERE review > (SELECT AVG(review) FROM Books) AND price < (SELECT AVG(price) FROM Books);
-- 가장 많은 종류의 책을 출판한 저자 찾기
SELECT author, COUNT(DISTINCT title) as num_books
FROM Books
GROUP BY author
ORDER BY num_books DESC
LIMIT 1;
-- 각 저자별로 가장 높은 판매지수를 기록한 책 조회
SELECT author, title, MAX(sales) as max_sales
FROM Books
GROUP BY author;
-- 연도별 출판된 책 수와 평균 가격 비교
SELECT YEAR(publishing) as year, COUNT(*) as num_books, AVG(price) as avg_price
FROM Books
GROUP BY year;
-- 출판사가 같은 책들 중 평점 편차가 가장 큰 출판사 찾기
SELECT publisher, MAX(rating) - MIN(rating) as rating_difference
FROM Books
GROUP BY publisher
ORDER BY rating_difference DESC
LIMIT 1;
-- 특정 저자의 책들 중 판매지수 대비 평점이 가장 높은 책 찾기
SELECT title, rating / sales as ratio
FROM Books
WHERE author = '김재훈 글그림/서정욱 글'
ORDER BY ratio DESC
LIMIT 1;