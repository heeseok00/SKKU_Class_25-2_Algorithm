[1��]
#include <stdio.h>

int main() {
    int N, result, power=1;
    printf("������ �Է��ϼ���: ");
    scanf("%d", &N);
    result=N;
    while (result<=10000) {
        result*=N;
        power++;
    }
    printf("10000�� �Ѵ� ��: %d�� %d���� = %d", N, power, result);
    return 0;
}