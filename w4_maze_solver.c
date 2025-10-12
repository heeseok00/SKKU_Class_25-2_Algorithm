#include <stdio.h>
#include <stdlib.h>

#define ROWS 3
#define COLS 4

int maze[ROWS][COLS] = {
    {0, 1, 0, 0},
    {0, 0, 0, 1},
    {1, 0, 0, 0}
};

int visited[ROWS][COLS] = {0};

typedef struct {
    int x, y;
    int dist;
} Point;

typedef struct {
    Point data[100];
    int front, rear;
} Queue;

void initQueue(Queue* q) {
    q->front = q->rear = 0;
}

int isEmpty(Queue* q) {
    return q->front == q->rear;
}

void enqueue(Queue* q, Point p) {
    q->data[q->rear++] = p;
}

Point dequeue(Queue* q) {
    return q->data[q->front++];
}

// BFS�� �ִ� ��� Ž��
int bfs(Point start, Point goal) {
    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};

    Queue q;
    initQueue(&q);
    enqueue(&q, start);
    visited[start.x][start.y] = 1;

    while (!isEmpty(&q)) {
        Point cur = dequeue(&q);

        if (cur.x == goal.x && cur.y == goal.y)
            return cur.dist;

        for (int i = 0; i < 4; i++) {
            int nx = cur.x + dx[i];
            int ny = cur.y + dy[i];
            if (nx >= 0 && nx < ROWS && ny >= 0 && ny < COLS) {
                if (maze[nx][ny] == 0 && !visited[nx][ny]) {
                    visited[nx][ny] = 1;
                    Point next = {nx, ny, cur.dist + 1};
                    enqueue(&q, next);
                }
            }
        }
    }
    return -1; // ��� ����
}

int main() {
    Point start = {0, 0, 0};   // ������
    Point goal = {2, 3, 0};    // ��ǥ��

    int result = bfs(start, goal);
    if (result != -1)
        printf("�ִ� ��� ����: %d\n", result);
    else
        printf("��θ� ã�� �� �����ϴ�.\n");

    return 0;
}
