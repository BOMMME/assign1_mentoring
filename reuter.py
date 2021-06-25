from bs4 import BeautifulSoup
import urllib.request # 웹 상의 url을 파이썬이 인식할 수 있도록 해주는 모듈!

def Test01():
    list_res01 = []  #title list
  # 내용 담고
# 1. 웹에서 html 문서를 가져와서 BeautifulSoup으로 파싱!
    list_url = 'https://www.reuters.com/'
    url = urllib.request.Request(list_url) #페이지 요청
    result = urllib.request.urlopen(url).read().decode('utf-8') # 페이지 다운로드
    soup = BeautifulSoup(result, 'html.parser') # html 태그로 변환한 객체를 soup로 리턴

        # <span class=>As Iran veers right, ties with Gulf Arabs may hinge on nuclear pact</span>
    result01 = soup.find_all('span', class_="MediaStoryCard__title___2PHMeX")

    for i in result01:
        list_res01.append(i.get_text(' ', strip = True))

    for i in list_res01:
        print(i)

if __name__ == '__main__':
    Test01()
