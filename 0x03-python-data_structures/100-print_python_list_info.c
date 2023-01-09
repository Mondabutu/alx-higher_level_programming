#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
* print_python_list_info - this prints some basic info about pytohn list
* @p: the python object
**/

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int k;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %lk\n", size);
	printf("[*] Allocated = %lk\n", obj->allocated);
	for (k = 0; k < size; k++)
		printf("Element %k: %s\n", k, Py_TYPE(obj->ob_item[k])->tp_name);
}
