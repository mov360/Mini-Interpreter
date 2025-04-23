from interpreter import *

def main():
    evaluator = Evaluator()

    print("Welcome to the Mini Interpreter. Type 'exit' to quit.")

    while True:
        try:
            text = input(">>> ").strip()
            
            if text == 'exit':
                print("Goodbye!")
                break

            if not text:
                continue

            tokens = list(tokenize(text))
            parser = Parser(tokens)
            ast = parser.parse()
            result = evaluator.eval(ast)
            print("Result:", result)

        except Exception as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
