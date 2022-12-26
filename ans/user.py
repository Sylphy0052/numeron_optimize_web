

class User:
    def __init__(self, name: str = "test", user_id: int = 0) -> None:
        self.name = name
        self.user_id = user_id
        
    def __repr__(self) -> str:
        return f"User{self.user_id}: {self.name}"
