import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"} #사람이 요청한 것처럼

url = "https://www.melon.com/chart/index.htm"

req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")
# 순위 제목 앨범 정보 가수

result1 = soup.select(".lst50") #1위~50위 정보
result2 = soup.select(".lst100") #51~100위 정보
result = result1 + result2 #두 정보 합쳐줌
#필요한 정보에 대한 클래스들
#순위는 enumerate활용 .ellipsis rank01(제목), .ellipsis rank02(가수), .ellipsis rank03(앨범)
#enumerate = 리스트처럼 순서가 있는 자료형을 반복할 때 인덱스와 값을 동시에 얻음.
#아래 for문의 경우 result에 있는 리스트를 인덱스와 함께 값을 넣음. 시작값은 1부터
#rank와 i에 각각 튜플 형태로 
for rank, i in enumerate(result, 1):
    title = i.select_one(".ellipsis.rank01 a").text
    singer = i.select_one(".ellipsis.rank02 a").text
    album = i.select_one(".ellipsis.rank03 a").text
    print(f"순위 : {rank}위")
    print(f"제목 : {title}")
    print(f"가수 : {singer}")
    print(f"앨범 : {album}")
    print()
    