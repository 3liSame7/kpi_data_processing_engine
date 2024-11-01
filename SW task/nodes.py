class ASTNode:
    pass

class UnaryOp(ASTNode):
    def __init__(self, op, expr):
        self.op = op
        self.expr = expr

class BinOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Num(ASTNode):
    def __init__(self, value):
        self.value = value

class RegexOp(ASTNode):
    def __init__(self, attr, pattern):
        self.attr = attr
        self.pattern = pattern



# SOLID Principles used:

# --->Single Responsibility Principle (SRP): Each node class (UnaryOp, BinOp, Num, RegexOp) is solely responsible for holding specific
# types of expressions or operations, keeping responsibilities distinct.

# Design Patterns used:

# --->Composite Pattern: The nodes follow a composite-like structure, where complex expressions can be composed of simpler ones,
# such as UnaryOp or BinOp, which encapsulate sub-expressions.