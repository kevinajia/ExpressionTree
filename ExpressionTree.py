#  File: ExpressionTree.py

#  Description: Take a valid infix expression and evaluate it and print the result

#  Student Name: Kevin Jia

#  Date Created: 4/19/19

#  Date Last Modified: 4/19/19

class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def is_Empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


class Node(object):
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None


class Tree(object):
    def __init__(self):
        self.root = Node(None)

    def create_tree(self, expr):
        expression = expr.split()
        parent = Stack()
        current = self.root

        for token in expression:
            if token == '(':
                parent.push(current)
                current.lChild = Node(None)
                current = current.lChild
            elif token in ['+', '-', '*', '/','//','%','**']:
                current.data = token
                parent.push(current)
                current.rChild = Node(None)
                current = current.rChild
            elif token.isdigit() or '.' in token:
                current.data = token
                current = parent.pop()
            elif token == ')':
                if not parent.is_Empty():
                    current = parent.pop()
                else:
                    break
                    
    def evaluate(self, aNode):
        if aNode.data == '+':
            return self.evaluate(aNode.lChild) + self.evaluate(aNode.rChild)
        elif aNode.data == '-':
            return self.evaluate(aNode.lChild) - self.evaluate(aNode.rChild)
        elif aNode.data == '*':
            return self.evaluate(aNode.lChild) * self.evaluate(aNode.rChild)
        elif aNode.data == '/':
            return self.evaluate(aNode.lChild) / self.evaluate(aNode.rChild)
        elif aNode.data == '//':
            return self.evaluate(aNode.lChild) // self.evaluate(aNode.rChild)
        elif aNode.data == '%':
            return self.evaluate(aNode.lChild) % self.evaluate(aNode.rChild)
        elif aNode.data == '**':
            return self.evaluate(aNode.lChild) ** self.evaluate(aNode.rChild)
        elif aNode.data.isdigit() or '.' in aNode.data:
            return eval(aNode.data)

    def pre_order(self, aNode):
        if aNode is not None:
            print(aNode.data, end=' ')
            self.pre_order(aNode.lChild)
            self.pre_order(aNode.rChild)

    def post_order(self, aNode):
        if aNode is not None:
            self.post_order(aNode.lChild)
            self.post_order(aNode.rChild)
            print(aNode.data, end=' ')


def main():
    in_file = open("expression.txt", "r")

    expression = in_file.readline()
    new_tree = Tree()
    new_tree.create_tree(expression)
    print(expression.rstrip(), '=', new_tree.evaluate(new_tree.root), "\n")

    # Print prefix and postfix versions of the expression
    print("Prefix Expression:", end=' ')
    new_tree.pre_order(new_tree.root)
    print("\n")
    print("Postfix Expression:", end=' ')
    new_tree.post_order(new_tree.root)

    in_file.close()

main()

