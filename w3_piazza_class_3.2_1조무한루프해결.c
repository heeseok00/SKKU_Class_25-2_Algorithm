[1조]
#include <stdio.h>

int main() {
    int N, result, power=1;
    printf("정수를 입력하세요: ");
    scanf("%d", &N);
    result=N;
    while (result<=10000) {
        result*=N;
        power++;
    }
    printf("10000을 넘는 수: %d의 %d제곱 = %d", N, power, result);
    return 0;
}