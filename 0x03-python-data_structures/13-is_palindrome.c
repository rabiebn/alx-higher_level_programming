#include "lists.h"

/**
 * node_at - returns node of a list at an index;
 * @head: head of the singly linked list;
 * @idx: index of the node to return;
 *
 * Return: the node at index idx, NULL at failure.
 */
listint_t *node_at(listint_t *head, size_t idx)
{
	listint_t *tmp;
	size_t count = 0;

	if (!head)
		return (NULL);
	tmp = head;

	while (count < idx)
	{
		if (!tmp)
			return (NULL);
		count++;
		tmp = tmp->next;
	}
	return (tmp);
}

/**
 * is_palindrome - checks if a list is a palindrome
 * @head: head of a listint_t linked list
 *
 * Return: 0 if it's not a palindrome, 1 if it is.
 */
int is_palindrome(listint_t **head)
{
	size_t count = 0, idx, i = 0, j = 0, half;
	listint_t *tmp1, *tmp2;
	int arr[1024];

	if (!*head || !(*head)->next)
		return (1);


	tmp1 = *head;
	while (tmp1)
	{
		count++;
		tmp1 = tmp1->next;
	}
	count--;
	half = count / 2;

	idx = count;
	while (idx > half)
	{
		if (!node_at(*head, idx))
			return (0);

		arr[j] = (node_at(*head, idx))->n;
		idx--, j++;
	}

	tmp2 = *head;
	while (i <= half)
	{
		if (tmp2->n != arr[i])
			return (0);

		i++, tmp2 = tmp2->next;
	}

	return (1);
}
