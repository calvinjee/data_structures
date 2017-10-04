# 3.1
# Three in One
# Describe how you could use a single array to implement three stacks.


class TripleStack(object):
    def __init__(self, stacksize):
        self.numstacks = 3
        self.stack = [None] * (self.numstacks * stacksize)
        self.stacksizes = [0] * self.numstacks
        self.stacksize = stacksize

    def top_index(self, stack):
        offset = stack * self.stacksize
        return offset + self.stacksizes[stack] - 1

    def is_empty(self, stack):
        if self.stacksizes[stack] == 0:
            return True

        return False

    def is_full(self, stack):
        if self.stacksizes[stack] == self.stacksize:
            return True

        return False

    def peek(self, stack):
        if self.is_empty(stack):
            raise Exception('Stack is empty')

        return self.stack[self.top_index(stack)]

    def push(self, val, stack):
        if self.is_full(stack):
            raise Exception('Stack is full')

        self.stacksizes[stack] += 1
        self.stack[self.top_index(stack)] = val
        
        return val

    def pop(self, stack):
        if self.is_empty(stack):
            raise Exception('Stack is empty')

        val = self.stack[self.top_index(stack)]
        self.stack[self.top_index(stack)] = None
        self.stacksizes[stack] -= 1

        return val


if __name__ == "__main__":
    s = TripleStack(3)

    print(s.is_empty(0))
    print(s.is_full(1))

    s.push(3, 1)
    s.push(4, 2)
    print(s.stack)

    s.push(1, 1)
    print(s.peek(1))
    print(s.stack)
    print(s.pop(1))
    print(s.stack)
    print(s.pop(0))

