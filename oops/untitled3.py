class PremiereEvent:
    def __init__(self, event_id, title, date, location):
        self.event_id = event_id
        self.title = title
        self.date = date
        self.location = location
        self.celebrities = []

    def add_celebrity(self, celebrity):
        self.celebrities.append(celebrity)

    def remove_celebrity(self, celebrity):
        if celebrity in self.celebrities:
            self.celebrities.remove(celebrity)

    def __str__(self):
        return f"{self.title} ({self.date}) at {self.location}"


class PremiereEventManager:
    def __init__(self):
        self.events = {}

    def create_event(self, event_id, title, date, location):
        if event_id in self.events:
            raise ValueError(f"Event with ID {event_id} already exists.")
        event = PremiereEvent(event_id, title, date, location)
        self.events[event_id] = event
        return event

    def read_event(self, event_id):
        return self.events.get(event_id)

    def update_event(self, event_id, title=None, date=None, location=None):
        event = self.read_event(event_id)
        if event:
            if title:
                event.title = title
            if date:
                event.date = date
            if location:
                event.location = location

    def delete_event(self, event_id):
        if event_id in self.events:
            del self.events[event_id]

    def organize_movie_premieres(self, premiere_id):
        event = self.read_event(premiere_id)
        if event:
            print(f"Organizing movie premiere event: {event}")

    def coordinate_celebrity_appearances(self, appearance_id):
        event = self.read_event(appearance_id)
        if event:
            print(f"Coordinating celebrity appearances for event: {event}")
            for celebrity in event.celebrities:
                print(f"Coordinating appearance for {celebrity}")

# Example usage
manager = PremiereEventManager()

# Create events
event1 = manager.create_event(1, "Movie Premiere A", "2024-05-01", "Los Angeles")
event2 = manager.create_event(2, "Movie Premiere B", "2024-06-15", "New York")

# Add celebrities to events
event1.add_celebrity("Celebrity 1")
event1.add_celebrity("Celebrity 2")
event2.add_celebrity("Celebrity 3")

# Organize movie premiere
manager.organize_movie_premieres(1)

# Coordinate celebrity appearances
manager.coordinate_celebrity_appearances(2)

# Update event
manager.update_event(1, date="2024-05-10")

# Delete event
manager.delete_event(2)
