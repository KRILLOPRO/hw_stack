class Stack:
    """
    Класс Stack реализует структуру данных стек по принципу LIFO
    (Last In - First Out, последним пришёл - первым вышел)
    """
    
    def __init__(self):
        """Инициализация пустого стека"""
        self._items = []
    
    def is_empty(self):
        """
        Проверяет стек на пустоту
        
        Returns:
            bool: True если стек пуст, False если содержит элементы
        """
        return len(self._items) == 0
    
    def push(self, item):
        """
        Добавляет новый элемент на вершину стека
        
        Args:
            item: элемент для добавления в стек
        """
        self._items.append(item)
    
    def pop(self):
        """
        Удаляет и возвращает верхний элемент стека
        
        Returns:
            Верхний элемент стека
            
        Raises:
            IndexError: если стек пуст
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()
    
    def peek(self):
        """
        Возвращает верхний элемент стека без его удаления
        
        Returns:
            Верхний элемент стека
            
        Raises:
            IndexError: если стек пуст
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]
    
    def size(self):
        """
        Возвращает количество элементов в стеке
        
        Returns:
            int: количество элементов в стеке
        """
        return len(self._items)
    
    def __str__(self):
        """Строковое представление стека для отладки"""
        return f"Stack({self._items})" 