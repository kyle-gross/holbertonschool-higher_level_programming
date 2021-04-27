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
	listint_t *trav, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	trav = *head;
	while (number > trav->next->n)
	{
		trav = trav->next;
		if (trav->next == NULL && number < trav->n)
		{
			new_node = add_nodeint_end(head, number);
			return (new_node);
		}
	}
	new_node->n = number;
	new_node->next = trav->next;
	trav->next = new_node;
	return (new_node);
}
