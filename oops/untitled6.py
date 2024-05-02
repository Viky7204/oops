class Event:
    def __init__(self, event_id, event_name, event_date):
        self.event_id = event_id
        self.event_name = event_name
        self.event_date = event_date

    def __str__(self):
        return f"Event: {self.event_name} (ID: {self.event_id}, Date: {self.event_date})"

class MoviePremiere(Event):
    def __init__(self, event_id, event_name, event_date, movie_title):
        super().__init__(event_id, event_name, event_date)
        self.movie_title = movie_title

    def organize_premiere(self):
        print(f"Organizing movie premiere for '{self.movie_title}'...")
        # Add logic to organize the movie premiere event

class Celebrity:
    def __init__(self, name, appearance_id):
        self.name = name
        self.appearance_id = appearance_id

    def __str__(self):
        return f"Celebrity: {self.name} (Appearance ID: {self.appearance_id})"

class EventManager:
    def __init__(self):
        self.events = []
        self.celebrities = []

    def add_event(self, event):
        self.events.append(event)
        print(f"Added event: {event}")

    def remove_event(self, event_id):
        for event in self.events:
            if event.event_id == event_id:
                self.events.remove(event)
                print(f"Removed event with ID: {event_id}")
                return
        print(f"No event found with ID: {event_id}")

    def organize_movie_premiere(self, premiere_id):
        for event in self.events:
            if isinstance(event, MoviePremiere) and event.event_id == premiere_id:
                event.organize_premiere()
                return
        print(f"No movie premiere found with ID: {premiere_id}")

    def add_celebrity(self, celebrity):
        self.celebrities.append(celebrity)
        print(f"Added celebrity: {celebrity}")

    def coordinate_celebrity_appearance(self, appearance_id):
        for celebrity in self.celebrities:
            if celebrity.appearance_id == appearance_id:
                print(f"Coordinating appearance for {celebrity.name}...")
                # Add logic to coordinate the celebrity appearance
                return
        print(f"No celebrity found with appearance ID: {appearance_id}")

# Example usage
event_manager = EventManager()

# Create and add events
premiere1 = MoviePremiere(1, "Movie A Premiere", "2024-06-15", "Movie A")
event_manager.add_event(premiere1)

event2 = Event(2, "Launch Event", "2024-07-01")
event_manager.add_event(event2)

# Remove an event
event_manager.remove_event(2)

# Organize a movie premiere
event_manager.organize_movie_premiere(1)

# Add celebrities
celebrity1 = Celebrity("John Doe", 101)
celebrity2 = Celebrity("Jane Smith", 102)
event_manager.add_celebrity(celebrity1)
event_manager.add_celebrity(celebrity2)

# Coordinate a celebrity appearance
event_manager.coordinate_celebrity_appearance(101)
