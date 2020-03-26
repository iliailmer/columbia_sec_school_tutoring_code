class Memory:
    """Basic Memory class for others to inherit from."""

    def __init__(self, size: int):
        """Construct the class."""
        self.storage: list = []
        self.size = size

    def add(self, item):
        """Add an item to the memory."""
        raise NotImplementedError

    def get(self):
        """Retrieve an item from the memory."""
        raise NotImplementedError


class MemoryFIFO(Memory):
    """FIFO cache."""

    def __init__(self, size: int):
        """Construct of First-In-First-Out Memory instance."""
        super().__init__(size=size)

    def add(self, item):
        """Add an item to memory. Item can be anything."""
        if len(self.storage) < self.size:
            self.storage.append(item)
        else:
            raise ValueError("Cache Full!")

    def get(self):
        """Retrieve item from memory in the First-In-First-Out fashion."""
        if len(self.storage) > 0:
            return self.storage.pop(0)
        else:
            raise ValueError("Memory empty, nothing to get!")


class MemoryFIFO2(Memory):
    """FIFO cache with eviction.

    If memory is full, it evicts the top element.
    """

    def __init__(self, size: int):
        """Construct of First-In-First-Out Memory instance."""
        super().__init__(size=size)

    def add(self, item):
        """Add an item to memory. Item can be anything.

        Evict the top item if not enough space
        """
        if len(self.storage) < self.size:
            self.storage.append(item)
        else:
            self.get()
            self.storage.append(item)

    def get(self):
        """Retrieve item from memory in the First-In-First-Out fashion."""
        if len(self.storage) > 0:
            return self.storage.pop(0)
        else:
            raise ValueError("Memory empty, nothing to get!")
