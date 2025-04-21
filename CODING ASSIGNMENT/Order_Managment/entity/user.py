class User:
    def __init__(self, userid=None, username=None, password=None, role=None):
        self.userid = userid
        self.username = username
        self.password = password
        self.role = role

    def __str__(self):
        return f"UserID: {self.userid}, Username: {self.username}, Role: {self.role}"
