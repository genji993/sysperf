from .inspector import AbstractInspector

__all__ = ['RAMInspector']

class RAMInspector(AbstractInspector):
    def __init__(self):
        super().__init__("RAMInspector")
