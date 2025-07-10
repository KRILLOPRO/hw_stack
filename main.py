from stack import Stack
from bracket_checker import check_brackets


def test_stack():
    """Тестирование функциональности класса Stack"""
    print("=== Тестирование класса Stack ===")
    
    # Создаем новый стек
    stack = Stack()
    
    # Проверяем пустой стек
    print(f"Пустой стек: {stack.is_empty()}")  # True
    print(f"Размер пустого стека: {stack.size()}")  # 0
    
    # Добавляем элементы
    print("\nДобавляем элементы: 1, 2, 3")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    print(f"Стек пуст: {stack.is_empty()}")  # False
    print(f"Размер стека: {stack.size()}")  # 3
    print(f"Верхний элемент (peek): {stack.peek()}")  # 3
    print(f"Размер после peek: {stack.size()}")  # 3 (не изменился)
    
    # Удаляем элементы
    print(f"\nУдаляем элемент: {stack.pop()}")  # 3
    print(f"Удаляем элемент: {stack.pop()}")  # 2
    print(f"Размер стека: {stack.size()}")  # 1
    print(f"Верхний элемент: {stack.peek()}")  # 1
    
    print(f"\nУдаляем последний элемент: {stack.pop()}")  # 1
    print(f"Стек пуст: {stack.is_empty()}")  # True
    
    print("\n" + "="*50)


def test_bracket_checker():
    """Тестирование проверки сбалансированности скобок"""
    print("\n=== Тестирование проверки скобок ===")
    
    # Сбалансированные примеры из задания
    balanced_examples = [
        "(((([{}]))))",
        "[([])((([[[]]])))]{()}",
        "{{[()]}}"
    ]
    
    # Несбалансированные примеры из задания
    unbalanced_examples = [
        "}{}",
        "{{[(])]}}",
        "[[{())}]"
    ]
    
    print("\nСбалансированные последовательности:")
    for example in balanced_examples:
        result = check_brackets(example)
        print(f"'{example}' -> {result}")
    
    print("\nНесбалансированные последовательности:")
    for example in unbalanced_examples:
        result = check_brackets(example)
        print(f"'{example}' -> {result}")
    
    print("\n" + "="*50)


def interactive_mode():
    """Интерактивный режим для проверки скобок"""
    print("\n=== Интерактивная проверка скобок ===")
    print("Введите строку со скобками для проверки (или 'exit' для выхода):")
    
    while True:
        user_input = input("\nВведите строку: ").strip()
        
        if user_input.lower() == 'exit':
            print("До свидания!")
            break
        
        if not user_input:
            print("Пустая строка. Попробуйте еще раз.")
            continue
        
        result = check_brackets(user_input)
        print(f"Результат: {result}")


if __name__ == "__main__":
    # Тестируем класс Stack
    test_stack()
    
    # Тестируем проверку скобок
    test_bracket_checker()
    
    # Запускаем интерактивный режим
    interactive_mode() 