class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if not self.stack:
            return False
        return self.stack.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return False
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.stack:
            return False
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    print(minStack.pop())
    print(minStack.top())
    print(minStack.getMin())
