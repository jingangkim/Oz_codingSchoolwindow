import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"} #사람이 요청한 것처럼

keyword = str(input("뭐 검색할까"))
url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="+keyword    #키워드에 해당하는 네이버 블로그 검색
print(url)

req = requests.get(url, header_user) #requests에서 get기능을 사용하고 get기능을 통해(url)을 가져옴 #요청을 보내되 헤더_유저 정보를 담아서 보낼거임. 그럼 사람이 보낸 것처럼 느끼겠지?
html = req.text
#print(str(html)) #html의 정보를 가져오지만, 문자형으로 된 텍스트를 가져올 뿐임. html 구조를 그대로 가져오는 게 아님.
soup = BeautifulSoup(html, "html.parser") #뷰티풀숲 패키지 안에 parser 기능을 html에 이용함. 그걸 soup에 담음
#정적 크롤링은 위 내용에서 url만 바꾸면 됨
#클래스는 . 아이디는 #
#결과물은 트리구조로 아래 있는 것들은 다 가져오게 됨

#클래스 명이 2개일 때 (spblog ico_ad) -> (".spblog.ico_ad")
#if문을 사용해서 광고가 적혀있는 거 필터링 이프문 개어렵네 진짜
#광고성을 띄우는 블로그의 특징 찾기 link_ad

results = soup.select(".bx:not(:has(.link_ad))") #has를 통해서 .bx에 모든 후손 중 .link_ad 클래스 가진 경우는 필터링
#만약 has를 제외한 results = soup.select(".bx:not(.link_ad)") 이런 식으로 작성하면 .bx 바로 밑에 후손만 관여하는 듯?
#name과 title값을 먼저 받기 전에 result로 soup 자료를 필터링을 한 번 해야할 거 같음.

for result in results:
    try:
        name = result.select_one(".name").text
        title_link = result.select_one(".title_link")
        title = title_link.text
        href = title_link.get('href')
        print(f"블로그 제목: {name}")
        print(f"블로그 작성자: {title}")
        print(f"블로그 주소 : {href}")
    except:
        print("실패함")
# 광고 배너의 id 또는 class 명을 찾아보세요
# 광고 배너의 결과값을 변수 담아서 if문으로 검증을 합니다.
# 아무것도 없는 경우는 어떤 값이 들어가는지 확인해주세요
# if문의 참과 거짓일 경우 어떻게 작동하는지에 대한 원리를 상기시켜보세요
# link_ad는 광고 배너를 말함. link_ad가 포함돼있으면 출력 안 할 것