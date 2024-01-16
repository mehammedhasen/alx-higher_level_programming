#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

typedef struct listint_s
{
int n;
struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
int check_cycle(listint_t *list);
listint_t *add_nodeint();
void free_listint();

#endif
