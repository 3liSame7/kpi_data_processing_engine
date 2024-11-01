import re
import json
import datetime
from nodes import UnaryOp, BinOp, Num, RegexOp 
from operations import ArithmeticOperation, RegexOperation

class Interpreter:
    def __init__(self):
        self.arithmetic_op = ArithmeticOperation()
        self.regex_op = RegexOperation()

    def evaluate(self, equation, value):
        self.current_value = value
        if "Regex" not in equation:
            equation = equation.replace("ATTR", str(value))

        tokens = self.tokenize(equation)
        self.tokens = iter(tokens)
        self.current_token = next(self.tokens, None)

        if "Regex" in tokens:
            regex_result = self.parse_regex_expression()
            return self.regex_op.compute(regex_result, value)

        ast = self.parse_expression()
        return self.arithmetic_op.compute(ast, value)

    def tokenize(self, equation):
        tokens = re.findall(r'\d+\.?\d*|[+\-*/()^]|Regex|ATTR|\'[^\']*\'|[a-zA-Z_]\w*', equation.replace(' ', ''))
        return tokens

    def parse_regex_expression(self):
        self.eat('Regex')
        self.eat('(')
        if self.current_token == 'ATTR':
            self.eat('ATTR')
        else:
            self.eat(self.current_token)
        
        pattern_token = self.current_token
        if pattern_token.startswith("'") and pattern_token.endswith("'"):
            self.eat(pattern_token)
        else:
            raise ValueError("Expected regex pattern in single quotes")
        
        self.eat(')')
        return RegexOp(attr='ATTR', pattern=pattern_token[1:-1])  

    def eat(self, token_type):
        if self.current_token == token_type:
            self.current_token = next(self.tokens, None)
        else:
            raise ValueError(f"Unexpected token: {self.current_token}, expected: {token_type}")

    def parse_expression(self):
        node = self.parse_term()
        while self.current_token in ('+', '-'):
            op = self.current_token
            self.eat(op)
            node = BinOp(left=node, op=op, right=self.parse_term())
        return node

    def parse_term(self):
        node = self.parse_factor()
        while self.current_token in ('*', '/'):
            op = self.current_token
            self.eat(op)
            node = BinOp(left=node, op=op, right=self.parse_factor())
        return node

    def parse_factor(self):
        node = self.parse_base()
        while self.current_token == '^':
            op = self.current_token
            self.eat(op)
            node = BinOp(left=node, op=op, right=self.parse_base())
        return node
    
    def visit_RegexOp(self, regex_node, value):
        """Process regex node separately, as expected in test."""
        return bool(re.match(regex_node.pattern, str(value)))

    def parse_base(self):
        token = self.current_token

        if token is None:
            raise ValueError("Unexpected end of input")

        if token == '(':
            self.eat('(')
            node = self.parse_expression()
            self.eat(')')
            return node
        elif re.match(r'^\d+\.?\d*$', token):
            self.eat(token)
            return Num(float(token))
        elif token in ('+', '-'):
            self.eat(token)
            expr = self.parse_base()
            return UnaryOp(op=token, expr=expr)
        elif token == 'ATTR':
            self.eat(token)
            return Num(float(self.current_value))
        else:
            raise ValueError(f"Unexpected token: {token}")

    def json_response(self, asset_id, attribute_id, value):
        try:
            response = {
                "asset_id": asset_id,
                "attribute_id": attribute_id,
                "timestamp": datetime.datetime.now().isoformat() + "Z",
                "value": value
            }
            return json.dumps(response)
        except TypeError as e:
            print(f"Error evaluating expression '{value}' with value {value}: {e}")
            return None

# SOLID Principles used:

#---->Single Responsibility Principle : The Interpreter class has a single responsibility, focusing on parsing and evaluating expressions.
# --->Open-Closed Principle : The design is open to extension, with ArithmeticOperation and RegexOperation operations managed 
# through composition.
# --->Dependency Inversion Principle: The interpreter depends on OperationInterface, an abstraction for arithmetic and regex operations, 
# which improves flexibility.

# Design Patterns used:

# --->Interpreter Pattern: The Interpreter class follows the Interpreter pattern, parsing and interpreting different components of an equation.
# --->Abstract Factory Pattern: Used in operations.py to decouple operation types by defining interfaces, enhancing modularity.