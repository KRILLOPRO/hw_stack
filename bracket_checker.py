from stack import Stack


def is_balanced(brackets_string):
    """
    Проверяет сбалансированность скобок в строке
    
    Args:
        brackets_string (str): строка со скобками для проверки
        
    Returns:
        bool: True если скобки сбалансированы, False если нет
    """
    # Словарь соответствия открывающих и закрывающих скобок
    matching_brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    # Множество открывающих скобок
    opening_brackets = {'(', '[', '{'}
    
    # Создаем стек для хранения открывающих скобок
    stack = Stack()
    
    # Проходим по каждому символу в строке
    for char in brackets_string:
        # Если символ - открывающая скобка, добавляем в стек
        if char in opening_brackets:
            stack.push(char)
        # Если символ - закрывающая скобка
        elif char in matching_brackets:
            # Проверяем, что стек не пуст
            if stack.is_empty():
                return False
            
            # Получаем верхний элемент стека
            top_bracket = stack.pop()
            
            # Проверяем, что открывающая скобка соответствует закрывающей
            if top_bracket != matching_brackets[char]:
                return False
    
    # Проверяем, что все скобки были закрыты (стек должен быть пуст)
    return stack.is_empty()


def check_brackets(brackets_string):
    """
    Проверяет сбалансированность скобок и возвращает результат в текстовом виде
    
    Args:
        brackets_string (str): строка со скобками для проверки
        
    Returns:
        str: "Сбалансированно" или "Несбалансированно"
    """
    if is_balanced(brackets_string):
        return "Сбалансированно"
    else:
        return "Несбалансированно" 