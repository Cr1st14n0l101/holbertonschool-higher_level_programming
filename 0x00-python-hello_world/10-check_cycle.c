#include "lists.h"

/**
 * check_cycle - verify if the lists have a cycle
 * @list: list to verify
 * Return: 1 if have a cycle or 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *before = list, *after = list;

	while (after && after->next)
	{
		before = before->next;
		after = after->next->next;
		if (before == after)
			return (1);
	}
	return (0);
}
