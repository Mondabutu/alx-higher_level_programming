#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - This Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: 0  If there is no cycle 
 *         1 If there is a cycle 
 */
int check_cycle(listint_t *list)
{
	listint_t *k, *f;

	if (list == NULL || list->next == NULL)
		return (0);

	k = list->next;
	f = list->next->next;

	while (k && f && f->next)
	{
		if (k == f)
			return (1);

		k = k->next;
		f = f->next->next;
	}

	return (0);
}
