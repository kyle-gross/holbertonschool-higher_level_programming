#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - inserts a node somewhere in the middle of a linked list
 * @head: pointer to head of list
 * @number: the number to add
 * Return: ptr to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *old, *trav, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	if (!*head)
	{
		*head = new_node;
		new_node->next = NULL;
		return (new_node);
	}
	old = *head;
	if (number <= old->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	trav = old->next;
	while (trav)
	{
		if (number <= trav->n)
		{
			old->next = new_node;
			new_node->next = trav;
			return (new_node);
		}
		old = trav;
		trav = trav->next;
	}
	new_node = add_nodeint_end(head, number);
	return (new_node);
}
