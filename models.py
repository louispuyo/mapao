# // MODELS


class mymodel():
    def __init__(self, *args, **kwargs):
        super(mymodel).__init__()

    def create(self) -> str:
        return "a model have been created"

    def delete(self) -> int:
        return 0
    
    def upgrade(self, element: int) -> int:
        return element + 1


