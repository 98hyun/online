```c
//project 
#include <stdio.h>
#include <time.h>

int main(void){

    srand(time(NULL));
    printf("\n\n=========아빠는 대머리 게임==========\n\n");
    int answer; //사용자 선택
    int treatment=rand()%4; //발모제 선택

    int cntShowBottle=0; // 게임에 보여줄 병 갯수
    int prevcntShowBottle=0; // 전 게임 보여준 병 갯수.
    // 서로 보여주는 병 갯수를 다르게 하여 정답률 향상. 

    // 3번의 기회.
    for (int i=1;i<=3;i++){
        int bottle[4]={0,0,0,0};
        
        do {
            cntShowBottle=rand()%2+2;
        } while (cntShowBottle==prevcntShowBottle);
        prevcntShowBottle=cntShowBottle;

        int isincluded=0; // 보여줄 병 중에 발모제가 있는지 여부.  
        printf(" > %d번째 시도 : ",i);

        //보여줄 병 종류 선택.
        for (int j=0;i<cntShowBottle;j++){
            int randBottle=rand()%4; //0~3

            //아직 선택이 안됐으면
            if (bottle[randBottle]==0){
                bottle[randBottle]=1;
                if (randBottle==treatment){
                    isincluded=1;
                }
            }
            else{
                j--;
            }

        // 사용자에게 표시
        for (int k=0;k<4;k++){
            if (bottle[k]==1){
                printf("%d ",k+1);
            }
        printf(" 물약을 머리에 바릅니다.\n\n");
        }
        if (isincluded==1){
            printf(" >> 성공\n");
        }
        else {
            printf(" >> 실패\n");
        }
        printf("\n 계속 하려면 아무키나 누르세요..");
        getchar();
    }
    printf("\n\n 발모제는 몇번일까요?");
    scanf_s(%d,&answer);
    if (answer==treatment+1){
        printf("정답");
    }
    else{
        printf("실패 정답은 %d 입니다.",treatment+1);
    }
    return 0;
}
```
