# 1. 그래프 기본
import matplotlib.pyplot as plt
# 한글 설정
import matplotlib 
matplotlib.rcParams['font.family'] = 'Malgun Gothic' #windows
# matplotlib.rcParams['font.family'] = 'AppleGothic' #Mac인 경우
matplotlib.rcParams['font.size'] = 15  #글자크기 
# 한글 폰트 사용시, 마이너스 글자가 깨지는 현상을 해결
matplotlib.rcParams['axes.unicode_minus'] = False  

# -1 -가 깨짐. 환경설정을 해줘야 함.
plt.plot([-1,0,1],[-5,-1,2])
plt.title('라인 그래프')
plt.show()

