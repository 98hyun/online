### 용어 

활성화함수 : 인공지능 모델의 표현력을 높이기 위한 함수. 비선형 분리가 가능해 데이터의 관계를 눈에 잘 띄게 할 수 있다.  
ReLU : max(0,x)로 간단해서 복잡하지않다. 시그모이드 함수에서의 기울기 0이 되는 문제를 극복했다. 컴퓨터 파워를 거의 소모 안하고.   
오차역전파법 : 순전파 계산으로 나온 예측값과 실제값을 비교해 가중치를 업데이트하며 거꾸로 계산하는 방법.  
regression loss func : mse, msle, mae   
binary classfication func : binary cross entropy, hinge, square hinge   
multiclass classfication func : multi-class cross entropy, sparse multiclass cross entropy, kullback divergence.  
