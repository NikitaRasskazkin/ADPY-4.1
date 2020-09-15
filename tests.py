from main import Library
import unittest
import json


class Tests(unittest.TestCase):
    def setUp(self):
        print()

    def test_document_owner_func(self):
        library = Library()
        with open('fixture/test_document_owner_func.json', encoding='utf-8') as f:
            tests = json.load(f)
        for param, result in tests:
            self.assertEqual(library.document_owner_func(param), result)

    def test_shelf_number_func(self):
        library = Library()
        with open('fixture/test_shelf_number_func.json', encoding='utf-8') as f:
            tests = json.load(f)
        for param, result in tests:
            self.assertEqual(library.shelf_number_func(param), result)

    def test_add_doc_func(self):
        library = Library()
        with open('fixture/test_add_doc_func.json', encoding='utf-8') as f:
            tests = json.load(f)
        for data in tests["new_data"]:
            library.add_doc_func(data['doc_number'], data['doc_type'], data['name'], data['shelf_number'])
        self.assertEqual(tests['expected_value']['documents'], library.documents)
        self.assertEqual(tests['expected_value']['directories'], library.directories)

    def test_delete_doc_func(self):
        library = Library()
        with open('fixture/test_delete_doc_func.json', encoding='utf-8') as f:
            tests = json.load(f)
        for data in tests["del_data"]:
            library.delete_doc_func(data)
        self.assertEqual(tests['expected_value']['documents'], library.documents)
        self.assertEqual(tests['expected_value']['directories'], library.directories)


if __name__ == '__main__':
    unittest.main()
