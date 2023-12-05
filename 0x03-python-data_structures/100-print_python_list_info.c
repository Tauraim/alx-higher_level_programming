#include <object.h>
#include <listobject.h>
#include <Python.h>
/**
 * print_python_list_info -  function that prints some basic
 *							info about Python lists
 * @p: python list
 */
void print_python_list_info(PyObject *p)
{
	long int size = PyList_size(p);
	int i;
	PylistObject *obj = (PyListObject *)p;

	printf("[*] size of the python list = %li\n" , size);
	printf("[*] Allocated = %li\n" , obj->allocated);
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_Type(obj->ob_item[i])->type_name);
}
