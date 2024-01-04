class User:
    def __init__(self, name, chat_id):
        self.id = None
        self.name = name
        self.chat_id = chat_id
        self.today_points = 0
        self.total_points = 0
        self.today_requests = 0
        self.total_requests = 0
        self.meloman_count = 0
