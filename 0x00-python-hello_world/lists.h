#ifndef _LISTS_H_
#define _LISTS_H_
#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>

/*
 * struct listint_s - singly linked list
 *@n: int
 *@next: node
 * Description: singly linked structure
 *
 */

typedef struct listint_s{
	int n;
	struct listint_s *next;
} listint_t;

int check_cycle(listint_t *list);
