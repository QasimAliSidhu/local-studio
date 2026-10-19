class JobQueue:
    def __init__(self):
        raise NotImplementedError

    def push(self, job):
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError
