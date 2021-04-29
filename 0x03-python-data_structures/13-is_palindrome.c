#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if NOT palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	size_t len = 0, i = 0;
	listint_t *mid = *head, *trav = *head, *temp;

	if (!head || !*head)
		return (1);
	/* Get length of list */
	while (trav->next)
		trav = trav->next, len++;
	/* Move mid to middle of list */
	while (i < len / 2)
	{
		mid = mid->next;
		i++;
	}
	/* If list size is odd, skip middle node */
	if (len % 2 != 0)
		mid = mid->next;
	/* Loop through rest of list and reverse it's order */
	trav = mid;
	trav = trav->next;
	mid->next = NULL;
	while (trav)
	{
		temp = trav->next;
		trav->next = mid;
		mid = trav;
		trav = temp;
	}
	/* Compare 1st and 2nd half of list */
	for (i = 0; i < (len / 2); i++)
	{
		if ((*head)->n != mid->n)
			return (0);
		*head = (*head)->next;
		mid = mid->next;
	}
	return (1);
}
