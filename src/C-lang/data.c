#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
};

int main(int argc, char **argv) {
  if (argc != 2) {
    printf("Usage: %s <number>\n", argv[0]);
    exit(1);
  }

  int size = atoi(argv[1]);

  struct node*HEAD = NULL;
  for (int i = 1; i <= size; i++) {
    struct node *new_node = malloc(sizeof(struct node));
    new_node->data = size - i + 1; 
    new_node->next = HEAD;
    HEAD = new_node;
  }

  for (struct node *cur = HEAD; cur != NULL; cur = cur->next) {
    printf("%d\n", cur->data);
  }
}
