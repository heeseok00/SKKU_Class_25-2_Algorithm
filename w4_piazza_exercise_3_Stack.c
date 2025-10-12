#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 100

typedef struct {
    char data[MAX];
    int top;
} Stack;

void init(Stack *s) {
    s->top = -1;
}

int isFull(Stack *s) {
    return s->top == MAX - 1;
}

int isEmpty(Stack *s) {
    return s->top == -1;
}

void push(Stack *s, char ch) {
    if (isFull(s)) {
        printf("스택이 가득 찼습니다.\n");
        return;
    }
    s->data[++(s->top)] = ch;
}

char pop(Stack *s) {
    if (isEmpty(s)) {
        printf("스택이 비었습니다.\n");
        return '\0';
    }
    return s->data[(s->top)--];
}

int main() {
    Stack s;
    init(&s);

    char str[MAX];
    printf("문자열을 입력하세요: ");
    scanf("%s", str);

    for (int i = 0; i < strlen(str); i++) {
        push(&s, str[i]);
    }

    printf("뒤집은 문자열: ");
    while (!isEmpty(&s)) {
        printf("%c", pop(&s));
    }
    printf("\n");

    return 0;
}
