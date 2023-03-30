class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, element) -> None:
        self.stack.append(element)

    def pop(self) -> str | None:
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def peek(self) -> str | None:
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None


def correct_bracket_sequence(string: str) -> bool:
    stack = Stack()
    for br in string:
        if br in "([{":
            stack.push(br)
        elif br in "}])":
            if stack.is_empty():
                return False
            if (br == ")" and stack.peek() == "(") or \
               (br == "}" and stack.peek() == "{") or \
               (br == "]" and stack.peek() == "["):
                stack.pop()
            else:
                return False

    return stack.is_empty()


print(correct_bracket_sequence("([]){}"))
