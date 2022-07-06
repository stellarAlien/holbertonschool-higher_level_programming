#include "lists.h"
/**
 * check_cycle - checks if linked list has a cycle
 * @list: head of list
 * Return: 1 if exists cycle else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *p;

	p = list;
	while (p)
	{
		if (p->next == list)
			return (1);
		p = p->next;
	}
	return (0);
}

