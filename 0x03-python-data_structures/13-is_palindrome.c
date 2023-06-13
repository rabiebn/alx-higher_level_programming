#include "lists.h"

/**
 * is_palindrome - checks if a list is a palindrome
 * @head: head of a listint_t linked list
 *
 * Return: 0 if it's not a palindrome, 1 if it is.
 */
int is_palindrome(listint_t **head)
{
	size_t i = 0, j = 0;
	listint_t *tmp;
	int arr[64];

	if (!head)
		return (0);

	if (!*head || !(*head)->next)
		return (1);

	tmp = *head;
	while (tmp)
	{
		arr[j] = tmp->n;
		tmp = tmp->next;
		j++;
	}
	j--;
	while (i <= (j / 2))
	{
		if (arr[i] != arr[j - i])
			return (0);
		i++;
	}
	return (1);
}
