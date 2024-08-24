import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='@Ab1480718',
    db='airbnb',
    charset='utf8mb4'
)
#1. **새로운 제품 추가**: Python 스크립트를 사용하여 'Products' 테이블에 새로운 제품을 추가하세요. 예를 들어, "Python Book"이라는 이름의 제품을 29.99달러 가격으로 추가합니다.
with connection.cursor() as cursor:
#    sql = "INSERT INTO Products (productName, price, stockQuantity) VALUES (%s, %s, %s)"
#    cursor.execute(sql, ("PythonBook", 29.99, 10))
#    connection.commit()

#2. **고객 목록 조회**: 'Customers' 테이블에서 모든 고객의 정보를 조회하는 Python 스크립트를 작성하세요.
##    sql = "SELECT * FROM Customers"
##    cursor.execute(sql)
##    result = cursor.fetchall()
##    for row in result:
##        print(row)
#3. **제품 재고 업데이트**: 제품이 주문될 때마다 'Products' 테이블의 해당 제품의 재고를 감소시키는 Python 스크립트를 작성하세요.
#    sql = "UPDATE Products SET stockQuantity = stockQuantity - %s WHERE ProductID=%s"
#    cursor.execute(sql, (1, 1))
#    connection.commit()
#4. **고객별 총 주문 금액 계산**: 'Orders' 테이블을 사용하여 각 고객별로 총 주문 금액을 계산하는 Python 스크립트를 작성하세요.
#    sql = "SELECT customerID, SUM(totalAmount) FROM Orders GROUP BY customerID"
#    cursor.execute(sql)
#    result = cursor.fetchall()
#    for row in result:
#        print(row)
#5. **고객 이메일 업데이트**: 고객의 이메일 주소를 업데이트하는 Python 스크립트를 작성하세요. 고객 ID를 입력받고, 새로운 이메일 주소로 업데이트합니다.
#    sql = "UPDATE customers SET email=%s WHERE customerID=%s"
#    cursor.execute(sql, ('unignore@gmail.com', '1'))

#connection.commit()
#6. **주문 취소**: 주문을 취소하는 Python 스크립트를 작성세요. 주문 ID를 입력받아 해당 주문을 'Orders' 테이블에서 삭제합니다.
#with connection.cursor() as cursor:
#    sql = "DELETE FROM Orders WHERE OrderID=%s"
#    cursor.execute(sql, (7))
#connection.commit()
#7. **특정 제품 검색**: 제품 이름을 기반으로 'Products' 테이블에서 제품을 검색하는 Python 스크립트를 작성하세요.
#    sql = "SELECT * FROM Products WHERE productName = %s"
#    cursor.execute(sql,('Republican A'))
#    result = cursor.fetchall()
#    for row in result:
#        print(row)
#8. **특정 고객의 모든 주문 조회**: 고객 ID를 기반으로 그 고객의 모든 주문을 조회하는 Python 스크립트를 작성하세요.
#sql = "SELECT * FROM Orders WHERE customerID = %s"
#    cursor.execute(sql, (1,))
#    for row in cursor.fetchall():
#        print(row)
#9. **가장 많이 주문한 고객 찾기**: 'Orders' 테이블을 사용하여 가장 많은 주문을 한 고객을 찾는 Python 스크립트를 작성하세요.
#    sql = "SELECT customerID, COUNT(*) as orderCount FROM Orders GROUP BY customerID ORDER BY orderCount DESC LIMIT 1"
    
    
#    cursor.execute(sql)
    
#    data = cursor.fetchone
#    print(data)

    cursor.close()