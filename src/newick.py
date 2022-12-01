"""A Newick parser."""

from __future__ import annotations
from dataclasses import dataclass
from typing import Union, cast, Generic, Optional, TypeVar
import re


def tokenize(tree: str) -> list[str]:
    """
    Extract the tokens from the text representation of a tree.

    >>> tokenize("A")
    ['A']
    >>> tokenize("(A, (B, C))")
    ['(', 'A', '(', 'B', 'C', ')', ')']
    """
    return re.findall(r'[()]|\w+', tree)

T = TypeVar('T')

@dataclass
class Link(Generic[T]):
    """A link in a linked list."""

    head: T
    tail: List[T]

    def __init__(self, head):
        self.head = head
        self.next = None


List = Optional[Link[T]]


class Stack(Generic[T]):
    """A stack of elements of (generic) type T."""

    def __init__(self) -> None:
        """Create a new stack of values of type T."""
        # FIXME: code here
        self.stack = None

    def push(self, x: T) -> None:
        """Push x on the top of this stack."""
        # FIXME: code here
        if self.stack == None:
            self.stack = Link(x)
        else:
            new_node = Link(x)
            new_node.next = self.stack
            self.stack = new_node

    def top(self) -> T:
        """Return the top of the stack."""
        # FIXME: code here
        if self.is_empty():
            return None
        else:
            return self.stack.head

    def pop(self) -> T:
        """Pop the top element off the stack and return it."""
        # FIXME: code here
        if self.is_empty():
            return None
        else:
            pop_node = self.stack.head
            self.stack = self.stack.next
            return pop_node

    def is_empty(self) -> bool:
        """Test if the stack is empty."""
        # FIXME: code here
        return True if self.stack == None else False


@dataclass(repr=False)
class Leaf:
    """
    A leaf in a tree.

    This will just be a string for our application.
    """

    name: str

    def __str__(self) -> str:
        """Simplified text representation."""
        return self.name
    __repr__ = __str__


@dataclass(repr=False)
class Node:
    """An inner node."""

    children: list[Tree]

    def __str__(self) -> str:
        """Simplified text representation."""
        pass
        return f"({','.join(str(child) for child in self.children)})"
    __repr__ = __str__


# A tree is either a leaf or an inner node with sub-trees
Tree = Union[Leaf, Node]


def parse(tree: str) -> Tree:
    """
    Parse a string into a tree.

    >>> parse("(A, (B, C))")
    (A,(B,C))
    """
    stack = Stack()

    tree = tokenize(tree)
    for ele in tree:
        match ele:
            case ')':
                node = Stack()
                node.push(ele)
                while stack.top() != '(':
                    node.push(stack.pop())
                node.push(stack.pop())

                children = Stack()
                while node.is_empty() == False:
                    children.push(node.pop())
                
                stack.push(Node(node))
            case '(':
                stack.push(ele)
            case _:
                stack.push(Leaf(ele))
    
    return cast(Tree, stack.pop())

def main():
    print(parse("(A, (B, C))"))
    

if __name__ == "__main__":
    main()
