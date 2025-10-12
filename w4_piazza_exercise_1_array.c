#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, k;

    printf("배열 크기를 입력하세요: ");
    scanf("%d", &n);

    int *arr = (int *)malloc(n * sizeof(int));
    int *rotated = (int *)malloc(n * sizeof(int));

    printf("%d개의 정수를 입력하세요: ", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("회전할 칸 수를 입력하세요 (양수=오른쪽, 음수=왼쪽): ");
    scanf("%d", &k);

    k = k % n;
    for (int i = 0; i < n; i++) {
        int newIndex = (i + k + n) % n;
        rotated[newIndex] = arr[i];
    }

    printf("회전된 배열: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", rotated[i]);
    }
    printf("\n");

    free(arr);
    free(rotated);
    return 0;
}
