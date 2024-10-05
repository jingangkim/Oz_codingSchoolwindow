from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
#내가 하고자 하는 것. 모바일 환경을 가정하고 스크래핑을 해야함.
#필요한 것. 모바일 환경에서 실행했을 때 접속하는 것과 똑같은 network user-agent
#아래는 제대로 입력을 했다. 그럼 이대로 실행하면 모바일로 접속했을 때랑 똑같은 환경으로 나와야하지 않는가?
user_agent = "Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36"

options = Options()
options.add_argument(f"User-Agent={user_agent}")
#options.add_argument("--window-size=375,667") #화면 크기를 모바일 화면 크기로
options.add_argument("disable-javascript")  # 자바스크립트 비활성화/ 하지만 작동 안됨
options.add_experimental_option("detach", True) #창이 꺼지지 않게
options.add_experimental_option("excludeSwitches", ["enable-logging"])
#크롬 드라이버 설치
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
#웹페이지 로딩
driver.get("https://m2.melon.com/index.htm#")
time.sleep(3)

# 접속 후 이벤트 페이지로 이동 되는 걸 막아야하는데, 못 하겠다. 그냥 멜론 버튼 눌러서 나가야겠다

logo_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".img-logo"))
)
logo_button.click()
#멜론 차트를 누른다
try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "ul.nav_wrap li:nth-child(3) a"))
    )
    element.click()
except Exception as e:
    print("Error:", e)
    # 오류 발생 시 처리


time.sleep(0.5)
#스크롤을 50위까지 내려야 버튼 활성화가 된다.
for i in range(15):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

#다 내렸으면 버튼을 눌러서 51위 이후도 나타내자    
try:
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".service_list_more.noline.sprite.hide"))
    )
    next_button.click()
except:
    pass
#이 부분이 문제가 있다. 뭐가 문제일까?

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.select(".content")

for rank, item in enumerate(items, 1):
    name = item.select_one(".title.ellipsis").text
    singer = item.select_one(".name.ellipsis").text
    print(f"순위 : {rank}")
    print(f"곡명 : {name}")
    print(f"가수명 : {singer}")
    print()
