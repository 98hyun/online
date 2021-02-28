## machine learning

#### 비교

빅데이터 분석  

그로스해킹,마케팅에 많이 쓰였다.  
상관관계(현상)를 찾는 분석방법이다.   

통계 분석  

현상을 이해하고 해석하는데 관심이 있다.  
모형에서 나오는 수치,통계치, 가정과 모형이 확실한지 불확실한지 관심이 있다.  
적은데이터로 분석 한다.  

머신러닝  

예측과 패턴을 분석한다.  

#### 접근 방법

전통적인 접근 방법은 문제 파악 후 규칙 작성, 평가 에러 확인 후 문제에 반영 다시 규칙 작성 평가 후 서비스 도입이었다.  
아무래도 늦고 많은 리소스,인력이 소비된다는 단점이 있었다.  

개선된 접근 방법은 문제 파악 후 머신러닝 모델 학습 평가 에러 확인 후 문제에 반영. 여기서 서비스에 도입한 후 데이터를 업데이트 부터 모델의 학습부터 평가가 자동화가 된다.  

#### domain knowledge

특정 분야의 전문적인 지식.  
이게 어떻게 수집이 됐는지 이걸 어떻게 사용하는지 이 현상이 의미하는것이 무엇인지에 충분히 대답할 수 있는 지식.

#### 데이터 준비와 파이프라인

think first (garbage input and output).  

data acquisition  

data preprocessing  

feature engineering   

model  
 
#### key

대다수 data preprocess와 feature engineering 은 도메인에 영향을 많이 받는다.  
preprocess는 컴퓨터가 잘 알아듣게 표현하는것. (vectorization, normalization, handling missing values ... )  
feature engineering 은 학습을 잘 진행될 수 있게 변환하는 작업. (transformation, generation, selection, extraction ...)  
