import pandas as pd
import glob
import os

from geopy.geocoders import Nominatim
n = input("현재 위치를 적어주세요:")
app = Nominatim(user_agent='tutorial')
location = app.geocode('{n}'.format(n=n))
print(location.latitude, location.longitude)

df = pd.read_csv("info.csv", engine='python', encoding='utf-8')

df_coffee = df[(df['상권업종중분류명']=='커피점/카페')]
df_coffee.index = range(len(df_coffee))
print('커피 전문점 점포 수 :', len(df_coffee))
df_coffee.head()

df_seoul_starbucks = df_coffee[df_coffee['상호명'].str.contains('스타벅스')]
df_seoul_starbucks.index = range(len(df_seoul_starbucks))
print('스타벅스 점포 수 :', len(df_seoul_starbucks))
df_seoul_starbucks.head()

df_seoul_ediya = df_coffee[df_coffee['상호명'].str.contains('이디야')]
df_seoul_ediya.index = range(len(df_seoul_ediya))
print('서울시 내 이디야 점포 수 :', len(df_seoul_ediya))
df_seoul_ediya.head()

from geopy.distance import great_circle
import pandas as pd
import folium
import CountByWGS84

# 파라미터 설정
# 35.1613737 129.1479813
location.latitude, location.longitude
lat = location.latitude
lon = location.longitude
dist = 1
# 반경 집계 인스턴스 생성
cbw = CountByWGS84(df, lat, lon, dist)

# 반경 범위 내 데이터 필터링
result_radius = cbw.filter_by_radius()


plot_2 = cbw.plot_by_radius(result_radius)
plot_2