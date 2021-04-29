#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * revArray - reverses an array
 * @arr: the array to reverse
 * Return: New reversed array
 */
int *revArray(int *arr)
{
	int *newArr = NULL, i = 0, ii = 0, len = 0;

	while (arr[i])
		len++, i++;
/*	newArr = malloc(sizeof(int) * len);
	if (!newArr)
		return (NULL);
*/	ii = len - 1;
	for (i = 0; i < len; i++, ii--)
	{
		newArr[i] = arr[ii];
	}
/*	free(arr);
*/	return (newArr);
}
/**
 * listint_len - returns the length of a linked list
 * @h: pointer to head of list
 * Return: the number of nodes
 */
size_t listint_len(const listint_t *h)
{
	size_t count = 0;

	if (!h)
		return (count);
	while (h->next)
	{
		count++;
		h = h->next;
	}
	count++;
	return (count);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if NOT palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	size_t len = listint_len(*head), i = 0, halfLen = len / 2;
	listint_t *mid = *head;
	int arr1[halfLen], arr2[halfLen];

	if (!head || !*head)
		return (1);
/*	arr1 = malloc(sizeof(int) * (len / 2));
	if (!arr1)
		return (0);
	arr2 = malloc(sizeof(int) * (len / 2));
	if (!arr2)
		return (0);
*/	/* Loop to middle of list and populate arr1 */
	printf("before first while\n");
	while (i < len / 2)
	{
		printf("loop #%ld\n", i);
		arr1[i] = mid->n;
		mid = mid->next;
		i++;
	}
	printf("After first while\n");
	/* If list size is odd, skip middle node */
	if (len % 2 != 0)
		mid = mid->next;
	/* Loop through rest of list and populate arr2 */
	i = 0;
	while (mid)
	{
		arr2[i] = mid->n;
		mid = mid->next;
		i++;
	}
	/* Reverse arr2 and compare arrays*/
	arr2 = revArray(arr2);
	for (i = 0; arr1[i] && arr2[i]; i++)
	{
		if (arr1[i] != arr2[i])
		{
/*			free(arr1), free(arr2);
*/			return (0);
		}
	}
	/* Free arrays */
/*	free(arr1), free(arr2);
*/	return (1);
}
