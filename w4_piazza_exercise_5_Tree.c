#include <stdio.h>

#define MAX 100

int tree[MAX];
int n;

int getHeight(int index) {
    if (index > n || tree[index] == 0) return 0;

    int left = getHeight(index * 2);
    int right = getHeight(index * 2 + 1);

    return (left > right ? left : right) + 1;
}

int main() {
    printf("노드 개수를 입력하세요 (dummy 포함): ");
    scanf("%d", &n);

    printf("%d개의 노드를 입력하세요 (0은 dummy): ", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &tree[i]);
    }

    int height = getHeight(1);  // 루트 노드는 인덱스 1

    printf("트리의 높이 = %d\n", height);
    return 0;
}