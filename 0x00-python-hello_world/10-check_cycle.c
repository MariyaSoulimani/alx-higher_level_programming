#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/**
 * check_cycle - Checks if a linked list has a cycle
 * @list: Pointer to the head of the linked list
 *
 * Return: 1 if a cycle exists, 0 otherwise
 */
int check_cycle(listint_t *list)
{
    listint_t *node1;
    listint_t *node2;

    node1 = list;
    node2 = list;

    while (node1 && node2 && node1->next)
    {
        node2 = node2->next;
        node1 = node1->next->next;
        if (node2 == node1)
            return (1);
    }
    return (0);
}
