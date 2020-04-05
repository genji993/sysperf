from .inspector import AbstractInspector


class RAMInspector(AbstractInspector):
    def __init__(self):
        super().__init__("RAMInspector")
