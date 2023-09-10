"""
QUESTIONABLE Object Creation Patterns in Python
https://youtu.be/Rm4JP7JfsKY?t=413
"""


from typing import List


class Reusable(object):
    def test(self):
        print("object: %s" % hex(id(self)))


class ReusablePool:
    def __init__(self, size: int) -> None:
        self._size = size
        self._free = []
        self._used = []
        # add objects to the free list
        for i in range(size):
            self._free.append(Reusable())

    def acquire(self) -> Reusable:
        """Get available instances from pool"""
        if len(self._free) <= 0:
            raise Exception("no free objects")
        # get a reference of the first object
        r = self._free[0]
        # remove that object from free
        self._free.remove(r)
        # add it to the use list
        self._used.append(r)
        # return the instance object
        return r

    def release(self, r: Reusable):
        """Release used instance and return it to free"""
        self._used.remove(r)
        self._free.append(r)


class PoolManager(object):
    def __init__(self, pool: ReusablePool) -> None:
        self._pool = pool

    def __enter__(self):
        self._obj = self._pool.acquire()
        return self._obj

    def __exit__(self, type, value, traceback):
        self._pool.release(self._obj)


def test_reusable():
    """single instance"""
    r = Reusable()
    r.test()


def test_pool():
    """Pool of limited instances"""
    # create pool of 2 objects only
    pool = ReusablePool(2)
    # acquire object
    r = pool.acquire()
    # use it
    r.test()

    # 2nd object
    r2 = pool.acquire()
    r2.test()

    # 3rd object
    try:
        r3 = pool.acquire()
    except:
        pool.release(r2)
        r3 = pool.acquire()
        r3.test()
        pass


def test_manager():
    """
    Manager of pool
    this makes sure objects are acquired and released.

    Creation patterns:
        - As a singleton: access every where|time
        - As a module: we simply import the functions for release and acquire
    """
    # create pool
    pool = Reusable()
    # with the manager
    with PoolManager(pool) as r:
        r.test()
    # run multiple times
    with PoolManager(pool) as r:
        r.test()
    with PoolManager(pool) as r:
        r.test()
    with PoolManager(pool) as r:
        r.test()
