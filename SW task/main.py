import json
import time
from database import create_table, insert_message  
from interpreter import Interpreter
from utils import construct_message

class MessageProcessor:
    def __init__(self, interpreter, insert_function):
        self.interpreter = interpreter
        self.insert_function = insert_function

    def read_messages(self, file_path):
        with open(file_path, 'r') as f:
            for line in f:
                yield json.loads(line.strip())

    def process_messages(self, file_path, equations):
        for message in self.read_messages(file_path):
            asset_id = message['asset_id']
            attribute_id = message['attribute_id']
            timestamp = message['timestamp']
            value = message['value']

            try:
                numeric_value = float(value)
                numeric_value_processed = True
            except ValueError:
                print(f"Non-numeric value encountered: {value}. Proceeding with regex evaluation.")
                numeric_value_processed = False

            for equation in equations:
                eq_expression = equation["equation"]
                try:
                    if "Regex" in eq_expression:
                        result = self.interpreter.evaluate(eq_expression, value)
                    else:
                        result = self.interpreter.evaluate(eq_expression, numeric_value)

                    output_message = construct_message(asset_id, f"output_{attribute_id}", result)
                    time.sleep(5)
                    self.insert_function(asset_id, f"output_{attribute_id}", timestamp, output_message)
                    print(output_message)
                except Exception as e:
                    print(f"Error evaluating expression '{eq_expression}' with value {value}: {e}")

def main():
    config_file = 'equation_config.json'
    message_file = 'messages.txt'
    interpreter = Interpreter()
    create_table()

    with open(config_file, 'r') as f:
        config = json.load(f)
        equations = config.get("equations", [])

    processor = MessageProcessor(interpreter=interpreter, insert_function=insert_message)
    processor.process_messages(message_file, equations)

if __name__ == "__main__":
    main()

# SOLID Principles used:

# --->Single Responsibility Principle: This script primarily handles processing messages and applying equations,
# staying mostly aligned with SRP.
# --->Dependency Inversion Principle: the file mainly depend on abstractions (e.g., Interpreter, insert_message), 
# which allows for better modularity.

# Design Patterns:

# --->Factory Pattern: A basic Factory Pattern is implicitly used by the configuration setup, where different equation types
# are passed to the interpreter.
#--->dependency injection: MessageProcessor accepts Interpreter and insert_message as dependencies via its constructor.
# This allows easy testing or swapping of implementations if required.