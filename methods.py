class Remainder:
    def __init__(self,event,remind_date = None,remind_time = None,priority=None,notes=None):
        self.event = event
        self.remind_date = remind_date
        self.remind_time = remind_time
        self.priority = priority
        self.notes = notes