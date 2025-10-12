#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

void insertAt(Node** head, int pos, int data) {
    Node* newNode = createNode(data);

    if (pos == 1) {
        newNode->next = *head;
        *head = newNode;
        return;
    }

    Node* current = *head;
    for (int i = 1; i < pos - 1 && current != NULL; i++) {
        current = current->next;
    }

    if (current == NULL) {
        printf("잘못된 위치입니다.\n");
        free(newNode);
        return;
    }

    newNode->next = current->next;
    current->next = newNode;
}

void printList(Node* head) {
    Node* current = head;
    while (current != NULL) {
        printf("%d", current->data);
        if (current->next != NULL) printf(" -> ");
        current = current->next;
    }
    printf("\n");
}

int main() {
    Node* head = NULL;
    Node* n1 = createNode(10);
    Node* n2 = createNode(20);
    Node* n3 = createNode(30);

    n1->next = n2;
    n2->next = n3;
    head = n1;

    printf("초기 리스트: ");
    printList(head);

    int pos, value;
    printf("삽입할 위치와 값을 입력하세요: ");
    scanf("%d %d", &pos, &value);

    insertAt(&head, pos, value);

    printf("삽입 후 리스트: ");
    printList(head);

    // 메모리 해제
    Node* temp;
    while (head != NULL) {
        temp = head;
        head = head->next;
        free(temp);
    }

    return 0;
}
