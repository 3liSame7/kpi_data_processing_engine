import unittest
from interpreter import Interpreter, RegexOp

class TestInterpreter(unittest.TestCase):
    def setUp(self):
        self.interpreter = Interpreter()
    
    def test_addition(self):
        self.assertEqual(self.interpreter.evaluate("2 + 3", 0), 5)
    
    def test_subtraction(self):
        self.assertEqual(self.interpreter.evaluate("5 - 2", 0), 3)
    
    def test_multiplication(self):
        self.assertEqual(self.interpreter.evaluate("4 * 3", 0), 12)
    
    def test_division(self):
        self.assertEqual(self.interpreter.evaluate("10 / 2", 0), 5)
    
    def test_exponentiation(self):
        self.assertEqual(self.interpreter.evaluate("2 ^ 3", 0), 8)
    
    def test_nested_operations(self):
        self.assertEqual(self.interpreter.evaluate("(2 + 3) * 4", 0), 20)
    
    def test_complex_expression(self):
        self.assertEqual(self.interpreter.evaluate("3 + 5 * (2 ^ 3) - 8 / 2", 0), 39)

    def test_regex_match(self):
        regex_node = RegexOp(attr='ATTR', pattern='^dog')
        test_values = ['doghouse', 'cat', 'dog', '100.0', '150.0']
        
        results = [self.interpreter.visit_RegexOp(regex_node, value) for value in test_values]
        
        expected_results = [True, False, True, False, False]
        self.assertEqual(results, expected_results)

    def test_non_numeric_value_regex(self):
        value = 'doghouse'
        equation = "Regex(ATTR, '^dog')"
        result = self.interpreter.evaluate(equation, value)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
