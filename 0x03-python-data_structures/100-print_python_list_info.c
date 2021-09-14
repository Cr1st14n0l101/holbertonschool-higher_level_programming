#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - Prints some basic info about Python lists.
 * @p: Pointer to the struct PyObject
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int i;

	printf("[*] Size of the Python List = %lu\n", SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < Py_SIZE; i++)
	{
		printf("Element %d: %s\n", PyTYPE(PyList_GetItem(p, i))->tp_name;
	}
}
