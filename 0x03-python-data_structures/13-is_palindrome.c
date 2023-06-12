#include "lists.h"

/**
 * is_palindrome - checks if a list is a palindrome
 * @head: head of a listint_t linked list
 *
 * Return: 0 if it's not a palindrome, 1 if it is.
 */
int is_palindrome(listint_t **head)
{
	size_t i, j = 0;
	listint_t *tmp = *head;
	int arr[1024];

	if (!*head || !(*head)->next)
		return (1);

	while (tmp)
	{
		arr[j] = tmp->n;
		tmp = tmp->next;
		j++;
	}
	j--;
	for (i = 0; i<= (j / 2); i++)
	{
		if (arr[i] != arr[j - i])
			return (0);
	}
	return (1);
}
