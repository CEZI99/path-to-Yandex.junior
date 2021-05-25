# Stack
class Stack:

    def __init__(self):
        self.stack = []

    def add(self, dataval):
        # Используем метод добавления списка для добавления элемента
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

# Используем метод всплывающего списка для удаления элемента
    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()

# Используем функцию peek, чтобы посмотреть на верхнюю часть стопки
    def peek(self): # Данная функция возвращает последний индекс списка
        return self.stack[-1]

AStack = Stack()
AStack.add("Sun")
print(AStack.peek())
AStack.add("Mon")
print(AStack.peek())
AStack.add("Tue")
print(AStack.peek())
AStack.add("Wed")
print(AStack.peek())
AStack.add("Thu")
AStack.remove()
print(AStack.peek())