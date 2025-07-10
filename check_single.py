from bracket_checker import check_brackets
import sys


def main():
    """Проверяет одну строку со скобками"""
    if len(sys.argv) != 2:
        print("Использование: python3 check_single.py 'строка_со_скобками'")
        print("Пример: python3 check_single.py '(((([{}]))))'")
        return
    
    brackets_string = sys.argv[1]
    result = check_brackets(brackets_string)
    print(f"Строка: '{brackets_string}'")
    print(f"Результат: {result}")


if __name__ == "__main__":
    main() 