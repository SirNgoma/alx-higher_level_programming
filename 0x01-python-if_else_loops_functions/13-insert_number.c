#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/*
 * insert_node - Insert a number into a sorted list
 * @head: a poiter to a pointer
 * @number: number to be inserted
 * Return: The adress of th new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current;

	if (head == NULL):
		return(NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL):
		return(NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || (*head)->n >= number) 
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	current = *head;
	while (current->next != NULL && current->next->n < number)
		current = current->next;

	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
