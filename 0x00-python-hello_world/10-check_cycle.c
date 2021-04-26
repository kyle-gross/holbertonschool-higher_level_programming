#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - checks if there is a cycle in a linked list
 * @list: the head of the list to check
 * Return: 0 if no cycle, 1 if cycle
 */
int check_cycle(listint_t *list)
{
	const listint_t *slow, *fast;

	slow = list;
	fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
