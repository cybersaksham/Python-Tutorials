"""
lru_cache start storing values till given maxsize & after maxsize it deletes first value & store next & so on.
In main function :-
1. work(3) is stored
2. work(4) is stored
3. work(5) is stored
4. work(6) is stored & work (3) is deleted
5. work(3) is stored & work (4) is deleted
5. work(5) is stored & work (5) is deleted
"""

import time
from functools import lru_cache


@lru_cache(maxsize=3)  # If we not use this then whenever function was called, the time lag would appear
def work(n):
    time.sleep(n)
    return n


if __name__ == '__main__':
    print("Calling work")
    work(3)  # This take delay of 3 seconds
    print("Again calling work")
    work(4)  # This value will be stored & does not take time
    print("Again calling work")
    work(5)  # This value will be stored & does not take time
    print("Again calling work")
    work(6)  # This value will be stored & does not take time
    print("Again calling work")
    # Since maxsize is three in decorator so three values [work(4), work(5), work(6)] before it would stored
    # So first i.e. work(3) would not stored hence this will take time lag
    work(3)
    print("Done.....Calling Again")
    # Since maxsize is three in decorator so three values [work(5), work(6), work(3)] before it would stored
    # So work(5) would be stored hence this will not take time lag
    work(5)
    print("Done")
