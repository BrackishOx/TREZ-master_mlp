import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from errors import TrezRuntimeError


class TrezQueue:
    """FIFO queue — pure Python lists, zero external deps."""
    def __init__(self):
        self._data = []

    def enqueue(self, val):
        self._data = self._data + [val]
        return self

    def dequeue(self):
        if not self._data:
            raise TrezRuntimeError("Queue vacía: dequeue() en cola vacía.")
        return self._data[0], TrezQueue._from(self._data[1:])

    def peek(self):
        if not self._data:
            raise TrezRuntimeError("Queue vacía: peek() en cola vacía.")
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def to_list(self):
        return list(self._data)

    @staticmethod
    def _from(lst):
        q = TrezQueue()
        q._data = list(lst)
        return q

    def __repr__(self):
        return f"Queue{self._data}"


class TrezStack:
    """LIFO stack — pure Python lists, zero external deps."""
    def __init__(self):
        self._data = []

    def push(self, val):
        self._data = self._data + [val]
        return self

    def pop(self):
        if not self._data:
            raise TrezRuntimeError("Stack vacío: pop() en pila vacía.")
        top = self._data[-1]
        new_stack = TrezStack._from(self._data[:-1])
        return top, new_stack

    def peek(self):
        if not self._data:
            raise TrezRuntimeError("Stack vacío: peek() en pila vacía.")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def to_list(self):
        return list(self._data)

    @staticmethod
    def _from(lst):
        s = TrezStack()
        s._data = list(lst)
        return s

    def __repr__(self):
        return f"Stack{self._data}"


def make_queue():
    return TrezQueue()

def make_stack():
    return TrezStack()
