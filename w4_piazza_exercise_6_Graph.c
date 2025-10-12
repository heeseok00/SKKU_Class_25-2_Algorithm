#include <stdio.h>

int main() {
    int n;
    int graph[10][10]; // 정점은 최대 10개까지 가정
    int degree[10] = {0};

    printf("정점의 개수를 입력하세요: ");
    scanf("%d", &n);

    printf("인접 행렬을 입력하세요:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &graph[i][j]);
        }
    }

    for (int i = 0; i < n; i++) {
        int count = 0;
        for (int j = 0; j < n; j++) {
            if (graph[i][j] == 1)
                count++;
        }
        degree[i] = count;
    }

    printf("\n각 정점의 차수:\n");
    for (int i = 0; i < n; i++) {
        printf("정점 %d → 차수 %d\n", i + 1, degree[i]);
    }

    return 0;
}
