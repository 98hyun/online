### 선언, 입출력

자료형 : int 같은. 한번 자료형 선언하면 다음엔 안써도 된다. ex) int age=12;   
`printf("%d\n",age);` 뜻 : %d는 정수 formating. %.2f는 실수. %c 문자. %s 문자열.  
주석 : 한줄 // 여러줄 /* */  
`const` : 상수 선언. ex) const int age=12;  
입력 : int input; scanf_s("%d",&input); 

```c
// 라이브러리 import.
#include <stdio.h>

// main 이라는 함수 선언. 
int main(void){
    char str[256];
    scanf_s("%s",str,sizeof(str));
    printf("%s\n",str);
    return 0;
}
```

### 반복문

`for (선언,조건,증감){}` : ex) for (int i=1;i<=10;i++){printf("hello");}
`while (조건) ` : ex) i=1; while (i<=10){printf("hello %d\n",i++);}
`do while` : ex) do{} while(i<=10)

### 조건문

`if else if else ` : ex) if (조건){} else if(조건){} else(){}
`break continue` : ex) if(){...; break;} else if(){...; continue;}
` &&  || ` : && 는 and || 는 or 
`switch case` : ex) switch(i){case 1: ..; case 2: ...; default: ...;  } 특징은 break 안하면 뒤에 다 실행한다.  

### 랜덤

```c
#include <stdio.h> // 입출력
#include <time.h> // 시간
#include <stdlib.h> // 표준라이브러리

int main(void){
    srand(time(NULL)); //난수 초기화
    int num=rand()%3+1; //0부터 3개에 +1 즉, 1,2,3
    return 0; 
}
```

### 함수 

방법 : 위에 선언. 아래에 정의.  
구성 : 반환형 함수이름(전달값) ex) void p(int num); void 는 반환값이 없는.  

### 배열 

선언 : ex) int arr[3]; 3은 사이즈. int는 반환형. 
indexing : ex) arr[0]=1; 0부터 선언.  
바로 값 선언 : ex) int arr[5]={1,2,3}; 사이즈는 5인데 나머지 없으면 0으로 초기화. 만약 아예 값 안넣으면 쓰레기값이 선언.  
값만 선언 : ex) int arr[]={1,2}; 나중에 확인하면 arr은 2의 크기를 갖는다.  

문자열 : ex) char str[]="coding"; 크기는 7. 끝값은 \0 포함. 만약 크기보다 안넣으면 \0 으로 초기화.  
ascii : 표준 7bit 코드. 0~127의 수.  
