#include <stdio.h>

#define TABLE_SIZE 5

int main() {
    int hashTable[TABLE_SIZE] = {0};
    int n, key;

    printf("삽입할 정수 개수를 입력하세요: ");
    scanf("%d", &n);

    printf("%d개의 정수를 입력하세요: ", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &key);
        int index = key % TABLE_SIZE;

        printf("입력 값 %d → 해시 인덱스 %d", key, index);

        if (hashTable[index] != 0) {
            printf(" (충돌 발생: 기존 값 %d)\n", hashTable[index]);
        } else {
            printf("\n");
        }

        hashTable[index] = key;
    }

    printf("\n=== 해시 테이블 상태 ===\n");
    for (int i = 0; i < TABLE_SIZE; i++) {
        if (hashTable[i] != 0)
            printf("index[%d] = %d\n", i, hashTable[i]);
        else
            printf("index[%d] = (비어 있음)\n", i);
    }

    return 0;
}
