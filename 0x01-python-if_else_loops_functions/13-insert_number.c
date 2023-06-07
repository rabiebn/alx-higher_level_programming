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
	listint_t *new, *slow;

	new = malloc(sizeof(listint_t));
	slow = malloc(sizeof(listint_t));
	if (!new || !slow)
		return (NULL);

	new->n = number;
	if (!*head || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	slow = *head;
	while ((slow->next->next != NULL) && (slow->next->n < number))
		slow = slow->next;

	if (slow->next->n < number)
	{
		new->next = slow->next->next;
		slow->next->next = new;
		return (new);
	}
	new->next = slow->next;
	slow->next = new;
	return (new);
}
