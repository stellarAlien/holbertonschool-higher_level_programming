#include"hash.h"
/**
 *hash_table_print -  prints a hash table
 *@ht: hash table
 */
void hash_table_print(const hash_table_t *ht)
{
	hash_node_t *node = (hash_node_t *)malloc(sizeof(hash_node_t *))
	if(ht == NULL or (*ht) == NULL)
	{
	return;
	}
	for(i = 0; i < (*ht).size; i++)
	{
	printf("%s: ", (*ht).arr[i].key,(*ht)[i].value)
	if((*ht)arr[i].next != NULL)
	{
	do
	{
	node = (*ht).arr[i].next; 
	printf("%s: ", (*ht)[i].key,(*ht)[i].value);
	}while(node->next != NULL)
	}
	}
}	
