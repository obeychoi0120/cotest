## 라이브러리 및 데이터 로드 
import pandas as pd 
import matplotlib.pyplot as plt 
%matplotlib inline 
import seaborn as sns 
from sklearn.preprocessing import OneHotEncoder 
from sklearn.preprocessing import LabelEncoder 
from sklearn.preprocessing import MinMaxScaler 
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.ensemble import RandomForestRegressor 
from sklearn.metrics import mean_squared_error 

# pd.read_csv() 
## 전처리 
# 학습, 테스트 데이터 나누기 
train_X, train_y, test_X, test_y = train_test_split(x, y, test_size = 0.3) 

# 스케일링
scaler = MinMaxScaler() 
scaler.fit(df) 
scaler.trainsform(df) 

# 원핫 인코딩
encoder = OneHotEncoder() 
encoder.fit_transform(df) 

# 레이블 인코딩 
encoder = LabelEncoder() 
encoder.fit_transform(df.values) 

# 시계열 데이터 전처리 
df['date'] = pd.to_datetime(df['datetime']) 
df['date'].dt.year 
df['date'].dt.month 
df['date'].dt.dayofweek 

# 월요일 : 0 
pd.date_range(start_date,end_date,freq = 'D') 


# 결측치 채우기 
df.fillna(df.mean()) 
df.fillna(method = 'bfill') 
df.fillna(method = 'ffill') 

## EDA 및 시각화 
# heatmap 
sns.heatmap(target.corr().loc[['supply','chain'],['month', 'day', 'dayofweek']],annot=True) 

# matplotlib 
plt.figure(figsize=(15,10)) 
# 종이 크기 지정 

plt.suptitle('plotting method', fontsize = 20, y=0.9) 
# 종이의 제목, y는 제목의 위치(default=0.98) 

plt.subplot(2,2,1) 
# 2행 2열에서 첫번째 부분/ * stateless의 plt.subplots()와 다름 

plt.plot(1.98, 0.15, 'ro', t2, f(t2), 'k') 
# x=1.98, y=0.15 에 빨간 점 찍고, x=t2, y=f(t2)에 그림 그려라 

plt.title('1st plot') 
# 제목 

plt.xlabel('x') 
# x축 이름 지정 

plt.ylabel('y blue', fontdict = {'size':15, 'color': 'blue'})
# y축 이름 지정 

plt.grid(True, color='g', linestyle='--') 
plt.annotate('3rd max', xy=(2, 0.17), xytext=(2.5, 0.6), fontsize=15, arrowprops=dict(facecolor='blue', shrink=0.05))
# 화살표 추가 plt.subplot(2,2,3) 
# 2행 2열에서 세번째 부분 

plt.plot(t2, np.cos(2*np.pi*t2), 'r--', label= 'cos') 
plt.plot(4,1,marker='x', ms=8, mec = 'b', mew = 2) 
# ms: markersize/ mec: markeredgecolor, mew: markeredgewidth 

plt.title('2nd plot') plt.legend(loc='best') 
plt.subplot(2,2,(2,4)) 
# 2행 2열에서 두번째, 네번째 부분 

plt.scatter(data['a'], data['b'], c=data['c'], s=data['d'], cmap='jet')
# c: color, s: size 

plt.title('3rd plot') 
plt.xlabel('x 축') 
plt.ylabel('y 축') 
plt.subplots_adjust(top=0.8, bottom=0.28, left=0.10, right=0.95, hspace=0.5, wspace=0.2) 
# subplot layout 조절 /hspace : subplot간 위아래 공간, wspace : subpot간 좌우 공간 

## 모델링 
# 분류 
model = RandomForestClassifier(n_estimators=100) 
model.fit(train_X, train_y) 
predict_y = model.predict(test_X) 

# 회귀 
model = RandomForestRegressor() model.fit(train_X, train_y) 
predict_y = model.predict(test_X) print(mean_squared_error(y_true, predict_y))