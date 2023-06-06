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

	new = malloc(sizeof(listint_t));
	fast = malloc(sizeof(listint_t));
	slow = malloc(sizeof(listint_t));
	if (!new || !fast || !slow)
		return (NULL);

	new->n = number;
	if (!*head)
	{
		new->next = NULL;
		*head = new;
		return (*head);
	}
	if ((*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	slow = *head;
	fast = (*head)->next;
	while ((fast->next != NULL) && (fast->n < number))
	{
		slow = slow->next;
		fast = fast->next;
	}
	if (fast->n < number)
	{
		new->next = fast->next;
		fast->next = new;
		return (new);
	}
	new->next = fast;
	slow->next = new;
	return (new);
}
