#include <stdio.h>
#include <stdlib.h>

#define MAX_VERTICES 100

// 노드 구조체
typedef struct Node {
    int vertex;
    struct Node* next;
} Node;

// 그래프 구조체
typedef struct {
    Node* adjList[MAX_VERTICES];
    int visited[MAX_VERTICES];
    int n; // 정점 개수
} Graph;

// 그래프 초기화
void initGraph(Graph* g, int n) {
    g->n = n;
    for (int i = 0; i < n; i++) {
        g->adjList[i] = NULL;
        g->visited[i] = 0;
    }
}

// 정점에 간선 추가
void addEdge(Graph* g, int v1, int v2) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->vertex = v2;
    newNode->next = g->adjList[v1];
    g->adjList[v1] = newNode;

    newNode = (Node*)malloc(sizeof(Node));
    newNode->vertex = v1;
    newNode->next = g->adjList[v2];
    g->adjList[v2] = newNode;
}

// 그래프 출력
void printGraph(Graph* g) {
    for (int i = 0; i < g->n; i++) {
        Node* temp = g->adjList[i];
        printf("%d -> ", i);
        while (temp) {
            printf("%d ", temp->vertex);
            temp = temp->next;
        }
        printf("\n");
    }
}

// 메인 테스트
int main() {
    Graph g;
    initGraph(&g, 5);

    addEdge(&g, 0, 1);
    addEdge(&g, 0, 2);
    addEdge(&g, 1, 3);
    addEdge(&g, 2, 4);

    printf("그래프 (인접 리스트):\n");
    printGraph(&g);

    return 0;
}
