from random import randint

def isEven(value):  # Task 1
    """
    Checking if number is even using AND operation.
    Bit operrations performed faster by processor, which is pro.
    however, in my opinion, the function in the case is less readable which is con.
    You can also convert the argument and check if the last character of the binary representation is "0":
    The name of function is not lowercase which is not according to PEP8, but was taken from test task example.
    """
    return value & 1 == 0


def isEven_str(value):
    """
    Also, you can convert the argument and check if the last character of the binary representation is "0".
    The name of function is not lowercase which is not according to PEP8, but was taken from test task example.
    """
    return str(bin(value))[len(bin(value)) - 1] == '0'


class QueueSimple:  # Task 2
    """
    Very simple realisation of queue using list, allowing only appending, popping and checking size of queue.
    Pros: simple, only necessary actions are possible, lists are built-in, so should be faster.
    Cons: theoretically, it is more time complex -- 0(1).
    """

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)


class QueueLinkedList:
    """
    Python implementation of Linked List.
    Pros: theoretically, it is less time complex -- 0(N).
    Cons: not as simple, as previous realisation, only allows pop and append, without checking size.
    """

    def __init__(self):
        self.first = None
        self.last = None

    def append(self, data):
        node = [data, None]  # [payload, 'pointer'] "pair"
        if self.first is None:
            self.first = node
        else:
            self.last[1] = node
        self.last = node

    def pop(self):
        if self.first is None:
            raise IndexError
        node = self.first
        self.first = node[1]
        return node[0]


def quicksort(nums):  # Task 3
    """
    As we don't know the size of array, it is hard to say, which sorting algorithm will be faster.
    I realised Hoare quicksort with random choice of pivot. This sorting has guaranteed n*logn time.
    but in some cases Timsort, which is used by default in Python, can be faster.
    So, in conclusion, it is hard to realise FASTEST realisation with data from task.
    """
    if len(nums) <= 1:
        return nums
    else:
        q = nums[randint(0, len(nums) - 1)]
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quicksort(s_nums) + e_nums + quicksort(m_nums)
