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
	int var, i;
	PyObject *obj;

	var = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %d\n", var;
	for (i = 0; i < Py_SIZE(p); i++)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_SIZE(obj)->tp_name);
	}
}
