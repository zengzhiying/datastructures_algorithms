#!/usr/bin/env python3
# coding=utf-8

class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    """采用链表法实现简单的哈希表
    这里只是简单的悬挂链表, 并没有进行红黑树的演变
    目前只适用于小规模数据, 当数据量超过10万时, 扩容搬迁数据速度会比较慢
    """

    def __init__(self, capicity=16, load_factor=0.75):
        self._capicity = capicity
        self._load_factor = load_factor
        self._size = 0
        self._data = [None] * capicity

    def size(self):
        return self._size

    def _hash(self, key: str):
        value = 0
        for c in key:
            value = 31 * value + ord(c)
        value =  value & 0xffffffff
        return value ^ (value >> 16)

    def set(self, key: str, value):
        if self._size / self._capicity > self._load_factor:
            self._capicity <<= 1
            new_data = [None] * self._capicity
            self._transfer(new_data)

        index = self._hash(key) & (self._capicity - 1)
        e = Element(key, value)
        if self._data[index] is None:
            self._data[index] = [e]
            self._size += 1
            return
        for old_e in self._data[index]:
            if old_e.key == key:
                old_e.value = value
                return

        self._data[index].append(e)
        self._size += 1

    def get(self, key: str):
        index = self._hash(key) & (self._capicity - 1)
        if self._data[index]:
            for e in self._data[index]:
                if e.key == key:
                    return e.value

        raise KeyError(key)

    def contains_key(self, key: str):
        index = self._hash(key) & (self._capicity - 1)
        if self._data[index]:
            for e in self._data[index]:
                if e.key == key:
                    return True

        return False

    def get_default(self, key: str, default_value=None):
        index = self._hash(key) & (self._capicity - 1)
        if self._data[index]:
            for e in self._data[index]:
                if e.key == key:
                    return e.value

        return default_value



    def _transfer(self, new_data):
        for elements in self._data:
            if elements:
                for e in elements:
                    index = self._hash(e.key) & (self._capicity - 1)
                    if new_data[index] is None:
                        new_data[index] = [e]
                    else:
                        new_data[index].append(e)

        self._data = new_data


if __name__ == '__main__':
    hash_table = HashTable()
    hash_table.set("abc", 82)
    hash_table.set("abcbd", 93)
    print(hash_table.size())
    print(hash_table.get("abc"))
    print(hash_table.get("absc"))


