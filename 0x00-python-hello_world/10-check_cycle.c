#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a listint_t singly linked list a cycle
 * @list: head of the listint_t singly linked list ????
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *hare, *tortoise;


	if (list == NULL)
		return (0);

	tortoise = list;
	hare = list->next;

	if (hare == NULL)
		return (0);

	while (tortoise != hare)
	{
		if (hare->next == NULL || hare->next->next == NULL)
			return (0);
		tortoise = tortoise->next;
		hare = hare->next->next;
	}
	return (1);
}
