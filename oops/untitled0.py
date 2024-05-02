class PremiereEvent:
    def __init__(self, event_id, name, date, location):
        self.event_id = event_id
        self.name = name
        self.date = date
        self.location = location
        self.celebrities = []

    def add_celebrity(self, celebrity):
        self.celebrities.append(celebrity)

    def remove_celebrity(self, celebrity):
        self.celebrities.remove(celebrity)

class CelebrityAppearance:
    def __init__(self, appearance_id, celebrity_name, event):
        self.appearance_id = appearance_id
        self.celebrity_name = celebrity_name
        self.event = event
        event.add_celebrity(self)

    
class PremiereEventPlanner:
    def __init__(self):
        self.events = []
        self.appearances = []

    def create_event(self, event_id, name, date, location):
        event = PremiereEvent(event_id, name, date, location)
        self.events.append(event)
        return event

    def delete_event(self, event_id):
        event = next((e for e in self.events if e.event_id == event_id), None)
        if event:
            self.events.remove(event)
            for appearance in self.appearances[:]:
                if appearance.event == event:
                    self.appearances.remove(appearance)

    def organize_movie_premiere(self, premiere_id):
        event = next((e for e in self.events if e.event_id == premiere_id), None)
        if event:
            
     
