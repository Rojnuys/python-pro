class DictMap:
    class DictIterator:
        def __init__(self, iterator: iter, key_func: callable, value_func: callable):
            self.iterator = iterator
            self.key_func = key_func
            self.value_func = value_func

        def __next__(self):
            k, v = next(self.iterator)
            return self.key_func(k), self.value_func(v)

    def __init__(self, collection: dict, key_func: callable, value_func: callable):
        self.collection = collection
        self.key_func = key_func
        self.value_func = value_func

    def __iter__(self):
        return self.DictIterator(iter(self.collection.items()), self.key_func, self.value_func)
