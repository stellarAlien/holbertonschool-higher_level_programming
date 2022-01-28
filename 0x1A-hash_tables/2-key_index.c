#include "hash.h"
/**
 *key_index: calculates the index of the key passed
 *@key: key passed
 *size: size of array of hashtable
  */
unsigned long int key_index(const unsigned char *key, unsigned long int size)
{
	unsigned long int ind;

	if(key == NULL)
	{
		exit(0);
	}
	ind = hash_djb2(key);
	if(ind > size)
	{
		return(-1);
	}
	return (idx);
}


