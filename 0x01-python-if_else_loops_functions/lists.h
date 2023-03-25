#ifndef LISTS_H
#define LISTS_H
#include <stddef.h>
/*
 * struct listint_t - singly linked list
 * @next: poinys to the nezt node
 * Description: singly list structure
 */

typedef struct listint_t
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint_(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

listint_t *insert_node(listint_t **head, int number);

#endif
