#include"lists.h"
#include <stdlib.h>

int is_palindrome(listint_t **head)
{
    listint_t *current = *head;
    static listint_t *tmp;

    if (current == NULL)
        return (1);

    if (tmp == NULL)
        tmp = current;

    if (is_palindrome(&current->next) && tmp->n == current->n)
    {
        tmp = tmp->next;
        return (1);
    }
    else
        return (0);
}
