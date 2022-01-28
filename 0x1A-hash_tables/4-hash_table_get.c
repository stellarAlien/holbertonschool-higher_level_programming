#include "hash.h"
/**
 *hash_table_get - returns value associated with key
 *@ht: hash table
 *@key: key that i am looking for
 *Return: value associated with key or null
 */
char *hash_table_get(const hash_table_t *ht, const char *key)
{
	int i;

	if(!(ht) ||!(*ht))
	{
		return(NULL);
	}
	for(i = 0; i < (*ht).size; i++)
	{
	if(strcmp((*ht)[i].key, key) == 0)
	{
	return((*ht)[i].value);
	}
	}
	return(NULL);
}	
