import yfinance as yf#주가외데이터, 주식분할이력,배단내역, 애널리스트평가 가능
import pandas as pd

# https://pypi.org/project/yfinance/ 예시보기
#재무제표 받아오려면 YAHOOFINANCE 패키지로 가능

# yf.download(['AAPL','MU'],start = '2020-06-01')

tick = yf.Ticker('MSFT') #티커 지정
data = yf.download('MSFT',start = '2020-06-01')

# print(data)
# data.head() #칼럼의 헤드. 5행만 부르기
# data = data.rename(columns={'Open': 'open','High': 'high','Low': 'low','Adj Close': 'adjclose','Volume': 'volume'})
# data=data[["adjclose","volume","open","high","row"]] #순서바꾸기


data=data['Close'] #종가만 뽑아 그래프 : .plot()으로 colab에서 가능하다!
print(data.tail())

div=tick.dividends #배당내역.
print(div)



# tick.splits  #주식분할할력  #코랩에서는 프린트없이 확인가능
# tick.recommendations  #애널리스트 평가정보


#df = pd.DataFrame()
# hist = tsla.history(period="max", auto_adjust=True)

# df['ds'] = hist.index  #날짜인덱스
# df['y'] = hist['Close'].values #종가 #df로 두가지 칼럼만 추출한다.
#
# df.tail()