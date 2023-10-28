#!/usr/bin/env python3

from rearrange import rearrange_name
import unittest

# Crear una clase de pruebas que herede de TestCase.
# Para heredar una clase, basta con recibirla como parámetro.
class TestRearrange(unittest.TestCase):

    # El prefijo test convierte el método en pruebas
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase),expected)

    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase),expected)
        
    def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(rearrange_name(testcase),expected)

# Iniciar las pruebas
unittest.main()