#include"hash.h"
/**
 *hash_table_set - adds element to hash table
 *@ht: hash table 
 *@key: key of the element
 *@value: value to be duplicated
 *Return: 1 if success else 0
 */
int hash_table_set(hash_table_t *ht, const char *key, const char *value)
{
	unsigned long int idx;

	if(!(ht) || !(*ht))
		return(0);
	if(!(value))
		return(0);
	idx = key_index(key, (*ht).size);
	if(idx >0)
	{
		if((*ht).array[idx].value != NULL)
		{
			hash_node_t* arr = (hash_node_s *)malloc(sizeof(hash_node_s));
			if (!arr)
			{
				return(0);
				free(arr);
			}
			strcpy(arr->key, key);
			strcpy(arr->value, value);
			arr->next = (array + idx);
			(array + idx) = arr;
			return (1);
		}
		else
		{
			strcpy((*ht).arr[idx].value, value);
			strcpy((*ht).arr[idx].key, key);
			return(1);
		}
		return(1);
	}
}
