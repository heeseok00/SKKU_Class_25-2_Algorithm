#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 100

typedef struct {
    char data[MAX][50];
    int front;
    int rear;
} Queue;

void init(Queue *q) {
    q->front = 0;
    q->rear = 0;
}

int isEmpty(Queue *q) {
    return q->front == q->rear;
}

int isFull(Queue *q) {
    return (q->rear + 1) % MAX == q->front;
}

void enqueue(Queue *q, const char *item) {
    if (isFull(q)) {
        printf("대기열이 가득 찼습니다.\n");
        return;
    }
    strcpy(q->data[q->rear], item);
    q->rear = (q->rear + 1) % MAX;
}

char* dequeue(Queue *q) {
    if (isEmpty(q)) {
        printf("대기열이 비어 있습니다.\n");
        return NULL;
    }
    char *item = q->data[q->front];
    q->front = (q->front + 1) % MAX;
    return item;
}

void printQueue(Queue *q) {
    if (isEmpty(q)) {
        printf("(비어 있음)\n");
        return;
    }
    printf("현재 대기열: ");
    int i = q->front;
    while (i != q->rear) {
        printf("%s ", q->data[i]);
        i = (i + 1) % MAX;
    }
    printf("\n");
}

int main() {
    Queue q;
    init(&q);

    int n;
    printf("인쇄할 파일 개수를 입력하세요: ");
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        char filename[50];
        printf("파일 이름 입력: ");
        scanf("%s", filename);
        enqueue(&q, filename);
        printQueue(&q);
    }

    printf("\n=== 인쇄 시작 ===\n");
    while (!isEmpty(&q)) {
        char *file = dequeue(&q);
        printf("출력 중: %s\n", file);
        printQueue(&q);
    }

    printf("모든 인쇄 작업이 완료되었습니다.\n");
    return 0;
}
