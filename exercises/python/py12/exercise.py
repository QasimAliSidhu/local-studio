class Cache:
    def __init__(self):
        raise NotImplementedError

    def set(self, key, value, ttl, now):
        raise NotImplementedError

    def get(self, key, now):
        raise NotImplementedError
