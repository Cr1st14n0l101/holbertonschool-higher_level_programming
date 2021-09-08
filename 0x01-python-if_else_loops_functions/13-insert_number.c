#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Function in C that inserts a number
 * into a sorted singly linked list.
 * @head: the first node
 * @number: the number to insert
 * Return: A pointer with the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *copy = *head;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	if (!copy)
	{
		new_node->next = copy->next;
		copy->next = new_node;
		return (new_node);
	}
	
	while(copy && copy->next)
	{
		if (copy->next->n > number)
		{
			new_node->next = copy->next;
			copy->next = new_node;
			return (new_node);
		}
		copy = copy->next;
	}
	return (NULL);
}
