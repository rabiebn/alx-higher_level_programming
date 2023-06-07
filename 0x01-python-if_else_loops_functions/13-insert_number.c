#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: head of the singly linked list;
 * @number: integer;
 *
 * Return: adress of the new inserted node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *fast, *slow;
	int count;

	count = 0;
	fast = slow = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = *head;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	while (fast != NULL)
	{
		count++;
		if (fast->n >= number)
		{
			if (count == 1)
				*head = new;
			else
				slow->next = new;
			new->next = fast;
			return (new);
		}
		slow = fast;
		fast = fast->next;
	}
	slow->next = new;
	new->next = NULL;
	return (new);
}
