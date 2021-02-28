### exploring

+ scatter 

1. negative, strong linear  
기울기가 감소하고 값들이 가상의 선으로 부터 거의 떨어지지 않는  

2. positive, week linear
기울기가 증가하고 값들이 가상의 선으로 부터 좀 떨어져 있는.  

* clusters 

scatter plot 은 데이터를 보여줄 뿐, cluster가 왜 나타나는지 real world 에서는 알 수 없다고 한다.  

* correlation R

R= mean but divide by n-1 between multiply z score for x and z score for y  

R 은 -1<=R<=1 를 만족한다.  

* linear regression

우리가 scatter plot에서 두 변수 사이의 관계를 보면, 그 관계를 요약하는 linear 를 그릴 수 있다.  

값들을 어느정도 포함하면서 예측도 할 수 있는 그런 선이 그려지는 데 이 과정을 linear regression 이라고 한다.  

* residual square 

느낌으로 하는 것이 아니라, 차이를 적게 하는 선이 최적의 선이다.  

그래서 residual plot 을 그려 보는 것도 도움이 된다. 맞지 않는 선은 걸러진다.  

* how to get residual least line

[know-how](https://www.khanacademy.org/math/statistics-probability/describing-relationships-quantitative-data)

y=mx+b 에서 m = (mean xy - mean x mean y) / (mean square x - sqaure mean x)  

square r = 1 - (mean square x / mean square y)  

square r 은 outlier가 없어질 수록 1에 가까워진다. (0<=square r<=1) line에 fit 하다는 말이다.  

 