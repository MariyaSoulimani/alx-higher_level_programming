#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about a Python list
 * @p: pointer to the Python object
 */
void print_python_list_info(PyObject *p)
{
    long int size = Py_SIZE(p);
    int i;
    PyListObject *obj;
    PyObject *list_item;

    size = Py_SIZE(p);
    printf("[*] Size of the Python List = %li\n", size);

    obj = (PyListObject *)p;
    printf("[*] Allocated = %li\n", obj->allocated);

    for (i = 0; i < size; i++)
    {
        list_item = PyList_GetItem(p, i);
        printf("Element %i: %s\n", i, Py_TYPE(list_item)->tp_name);
    }
}
