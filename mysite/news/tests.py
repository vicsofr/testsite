from django.test import TestCase


class TestStringMethods(TestCase):
    def test_length(self):
        self.assertEqual(len('news'), 4)

    def test_show_msg(self):
        # действительно ли первый аргумент — True?
        self.assertTrue(False, msg="Важная проверка на истинность")