### sampling 

n이 충분히 크면, 추출한 샘플들의 평균은  

모평균(np)의 divide by n 한 p 로 수렴하고, 

표준편차또한 divide by n 한 sqrt(p(1-p)/n) 으로 수렴한다.  

* normal distribution

sampling 된 집합들이 normal distribution에 가까워지려면   

np>=10 이면ㅅ n(1-p)>=10 을 만족하면 된다.  

* comparison

1. skewed distribution and normal distribution

처음 skewed 인데 size n 도 >30 이 아니다. -> 말도 안된다.  
처음 skewed 인데 size n 은 >30 이다.      -> 정규 분포에 가까워 진다.  
처음 normal 인데 size n 은 >30 이 아니다. -> 상관없이 정규분포 된다.  
처음 normal 인데 size n 은 >30 이다.      -> 역시 정규 분포 된다.  

