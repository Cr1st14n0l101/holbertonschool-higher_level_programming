#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints some basic info about Python lists.
 * @p: Pointer to the struct PyObject
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int i = 0;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %i: %s\n", PyTYPE(obj->ob_item[i])->tp_name);
	}
}
