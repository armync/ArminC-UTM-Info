// SPDX-License-Identifier: BSD-3-Clause

#include "Python.h"

int main(void)
{
	PyObject *pModuleName, *pModule;
	PyObject *pFunc, *pythonArgument;
	PyObject *pValue, *pValue1, *pValue2, *pRes;

	char *msg = "Hello World!";
	char *haystack = "123456789";
	char *needle = "89";
	long substr_idx = -1;

	setenv("PYTHONPATH", "./python_modules", 1);

	Py_Initialize();

	pModuleName = PyUnicode_DecodeFSDefault("my_module");
	if (pModuleName == NULL) {
		fprintf(stderr, "pModuleName is null.\n");
		return 0;
	}
	pModule = PyImport_Import(pModuleName);

	if (pModule != NULL) {
		pythonArgument = PyTuple_New(1);
		if (pythonArgument == NULL) {
			fprintf(stderr, "pythonArgument is null.\n");
			return 0;
		}

		pValue = PyUnicode_DecodeFSDefault(msg);
		if (pValue == NULL) {
			fprintf(stderr, "pValue is null.\n");
			return 0;
		}

		if (PyTuple_SetItem(pythonArgument, 0, pValue) < 0) {
			fprintf(stderr, "PyTuple_SetItem failed.\n");
			return 0;
		}

		pFunc = PyObject_GetAttrString(pModule, "say");
		if (pFunc == NULL) {
			fprintf(stderr, "pFunc is null.\n");
			return 0;
		}
		PyObject_CallObject(pFunc, pythonArgument);

		Py_DECREF(pFunc);
		Py_DECREF(pythonArgument);

		pythonArgument = PyTuple_New(2);
		if (pythonArgument == NULL) {
			fprintf(stderr, "pythonArgument is null.\n");
			return 0;
		}

		pValue1 = PyUnicode_DecodeFSDefault(haystack);
		if (pValue1 == NULL) {
			fprintf(stderr, "pValue1 is null.\n");
			return 0;
		}
		pValue2 = PyUnicode_DecodeFSDefault(needle);
		if (pValue2 == NULL) {
			fprintf(stderr, "pValue2 is null.\n");
			return 0;
		}

		if (PyTuple_SetItem(pythonArgument, 0, pValue1) < 0) {
			fprintf(stderr, "PyTuple_SetItem failed for pValue1.\n");
			return 0;
		}
		if (PyTuple_SetItem(pythonArgument, 1, pValue2) < 0) {
			fprintf(stderr, "PyTuple_SetItem failed for pValue2.\n");
			return 0;
		}
		pFunc = PyObject_GetAttrString(pModule, "contains");
		if (pFunc == NULL) {
			fprintf(stderr, "pFunc is null.\n");
			return 0;
		}
		pRes = PyObject_CallObject(pFunc, pythonArgument);
		if (pRes == NULL) {
			fprintf(stderr, "pRes is null.\n");
			return 0;
		}
		substr_idx = PyLong_AsLong(pRes);
		if (substr_idx > -1) {
			printf("First occurence of %s in %s is at index %ld.\n", needle, haystack, substr_idx);
		} else {
			printf("%s does not contain %s.\n", haystack, needle);
		}
	} else {
		fprintf(stderr, "pModule is null.\n");
		return 0;
	}

	Py_DECREF(pModuleName);
	Py_DECREF(pModule);
	Py_DECREF(pFunc);
	Py_DECREF(pythonArgument);
	Py_DECREF(pRes);

	Py_Finalize();

	return 0;
}
