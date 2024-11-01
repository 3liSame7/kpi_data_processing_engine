import re
from nodes import Num, UnaryOp, BinOp, RegexOp

class OperationInterface:
    def compute(self, node, value):
        raise NotImplementedError("Must implement compute method")

class ArithmeticOperation(OperationInterface):
    def compute(self, node, value):
        if isinstance(node, Num):
            return self.compute_num(node)
        elif isinstance(node, UnaryOp):
            return self.compute_unary(node)
        elif isinstance(node, BinOp):
            return self.compute_binary(node)
        else:
            raise ValueError(f"Unsupported node type: {type(node)}")

    def compute_num(self, node):
        return node.value

    def compute_unary(self, node):
        if node.op == '+':
            return +self.compute(node.expr, None)
        elif node.op == '-':
            return -self.compute(node.expr, None)
        else:
            raise ValueError(f"Unsupported unary operator: {node.op}")

    def compute_binary(self, node):
        left = self.compute(node.left, None)
        right = self.compute(node.right, None)

        if node.op == '+':
            return left + right
        elif node.op == '-':
            return left - right
        elif node.op == '*':
            return left * right
        elif node.op == '/':
            if right == 0:
                raise ValueError("Division by zero")
            return left / right
        elif node.op == '^':
            return left ** right
        else:
            raise ValueError(f"Unsupported binary operator: {node.op}")

class RegexOperation(OperationInterface):
    def compute(self, node, value):
        if isinstance(node, RegexOp):
            pattern = node.pattern
            match = re.match(pattern, str(value))
            return match is not None
        else:
            raise ValueError("Expected a RegexOp node for regex operation")


# SOLID Principles used:

# --->Single Responsibility Principle: Each class (ArithmeticOperation, RegexOperation) has a clear responsibility:
# one for numeric calculations and the other for regex evaluation.
# --->Liskov Substitution Principle: ArithmeticOperation and RegexOperation both adhere to the interface defined by 
# OperationInterface, allowing for flexible substitution.

# Design Patterns:

# --->Strategy Pattern: ArithmeticOperation and RegexOperation implement different strategies for computation,
# allowing the Interpreter to switch based on the node type.