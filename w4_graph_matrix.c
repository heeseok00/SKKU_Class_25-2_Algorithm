#include <stdio.h>

#define MAX 10

typedef struct {
    int n; // 정점 개수
    int matrix[MAX][MAX];
} Graph;

void initGraph(Graph* g, int n) {
    g->n = n;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            g->matrix[i][j] = 0;
}

void addEdge(Graph* g, int v1, int v2) {
    g->matrix[v1][v2] = 1;
    g->matrix[v2][v1] = 1; // 무방향 그래프
}

void removeEdge(Graph* g, int v1, int v2) {
    g->matrix[v1][v2] = 0;
    g->matrix[v2][v1] = 0;
}

void printGraph(Graph* g) {
    for (int i = 0; i < g->n; i++) {
        for (int j = 0; j < g->n; j++) {
            printf("%d ", g->matrix[i][j]);
        }
        printf("\n");
    }
}

int main() {
    Graph g;
    initGraph(&g, 4);

    addEdge(&g, 0, 1);
    addEdge(&g, 0, 2);
    addEdge(&g, 1, 2);
    addEdge(&g, 2, 3);

    printf("그래프 (인접 행렬):\n");
    printGraph(&g);

    removeEdge(&g, 0, 2);
    printf("간선 (0,2) 삭제 후:\n");
    printGraph(&g);

    return 0;
}
