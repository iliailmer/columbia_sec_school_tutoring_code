import pytest
from memory import MemoryFIFO, MemoryFIFO2, Memory
from numpy.random import randint
from typing import Union


def fill(M: MemoryFIFO) -> MemoryFIFO:
    vals = randint(-10, 10, size=M.size)
    for v in vals:
        M.add(v)
    return M


@pytest.mark.parametrize("size", [10, 20, 50])
def testFIFO(size):
    fifo = MemoryFIFO(5)
    fifo.storage = [1, 2, 3, 4, 5]
    item = fifo.get()
    assert item == 1
    assert fifo.storage == [2, 3, 4, 5]
    fifo = MemoryFIFO(size)  # no eviction
    fifo = fill(fifo)
    with pytest.raises(ValueError):
        fifo.add(10)
    with pytest.raises(ValueError):
        fifo = MemoryFIFO(size)
        fifo.get()


# def testFIFO2():
#     fifo = MemoryFIFO2
