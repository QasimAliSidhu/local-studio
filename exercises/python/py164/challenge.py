from dataclasses import dataclass

@dataclass(frozen=True)
class Notice:
    recipient: str
    text: str

class Dispatcher:
    def __init__(self, transport):
        pass
    def deliver(self, notice):
        pass
