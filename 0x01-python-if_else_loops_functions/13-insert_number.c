#include <stdio.h>
#include <stdlib.h>

/* Definition for singly-linked list */
typedef struct listint {
    int data;
    struct listint *next;
} listint_t;

/* Function to insert a number into a sorted singly linked list */
listint_t *insert_node(listint_t **head, int number) {
    listint_t *new_node = malloc(sizeof(listint_t));
    if (new_node == NULL) {
        return NULL;  // Allocation failure
    }

    new_node->data = number;
    new_node->next = NULL;

    if (*head == NULL || number < (*head)->data) {
        new_node->next = *head;
        *head = new_node;
    } else {
        listint_t *current = *head;
        while (current->next != NULL && current->next->data < number) {
            current = current->next;
        }

        new_node->next = current->next;
        current->next = new_node;
    }

    return new_node;
}

/* Function to print the linked list */
void print_list(listint_t *head) {
    listint_t *current = head;
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}

/* Example usage */
int main() {
    listint_t *head = NULL;

    insert_node(&head, 5);
    insert_node(&head, 10);
    insert_node(&head, 7);
    insert_node(&head, 3);

    printf("Original Linked List: ");
    print_list(head);

    return 0;
}

