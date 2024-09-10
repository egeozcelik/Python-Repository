from typing import Callable


class DiskUtils:
    notify_cb = Callable[[int, any], None] = lambda p,_: print(p)


DiskUtils.notify_cb(20, "denemedir")


