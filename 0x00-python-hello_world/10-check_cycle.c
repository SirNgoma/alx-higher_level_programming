#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/*
 *check_cycle - check if a singly linked list has a cycle
 *@list: lists
 *Return: 0 if there is no cycle , else 1
 */

int check_cycle(listint_t *list)
{
	listint_t *f_ptr = list;
	listint_t *s_ptr = list;

	while (f_ptr && s_ptr && s_ptr->next)
	{
		f_ptr = f_ptr->next;
		s_ptr = s_ptr->next->next;

		if (f_ptr == s_ptr)
		{
			return (1);
		}
	}
	return (0);
}

