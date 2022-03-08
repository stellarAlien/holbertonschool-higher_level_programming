#include<stdlib.h>
#include<stddef.h>
/**
 * is_palindrome - determines if a linked list is a palindrome list
 * @head : pointer to head of list
 * Return: 1 if palindrome else 0
 */
int is_palindrome(listint_t** head)
{
	int i = 0, j, arr[256];

	if (head == NULL)
	{
		return (0);
	}
	if (*head == NULL)
	{
		return (0);
	}
	if (*head->next == NULL)
	{
		return (1);
	}
	listint_t *p = (listint_s *)malloc(sizeof(listint_t))

	while (*p)
	{
		p = p->next;
		arr[i++] = p->n;
	}
	if (i % 2 == 0)
	{
		return (0);
	}
	for (j = 0; j < (i / 2); j++)
	{
		if (arr[i] != arr[i - j - 1])
			return (0)
	}
	free(p);
	return (1);
}

