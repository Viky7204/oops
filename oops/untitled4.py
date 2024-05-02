# Database for storing events
events = []

# Database for storing celebrity appearances
appearances = []

# CRUD operations for premiere events
def create_event(name, date, location):
    event = {
        "id": len(events) + 1,
        "name": name,
        "date": date,
        "location": location
    }
    events.append(event)
    return event["id"]

def read_event(event_id):
    for event in events:
        if event["id"] == event_id:
            return event
    return None

def update_event(event_id, name=None, date=None, location=None):
    event = read_event(event_id)
    if event:
        if name:
            event["name"] = name
        if date:
            event["date"] = date
        if location:
            event["location"] = location
        return True
    return False

def delete_event(event_id):
    event = read_event(event_id)
    if event:
        events.remove(event)
        return True
    return False

# Organize and manage movie premiere events
def organize_movie_premieres(premiere_id):
    premiere = read_event(premiere_id)
    if premiere:
        # Implement premiere organization logic here
        print(f"Organizing movie premiere '{premiere['name']}' on {premiere['date']} at {premiere['location']}")
    else:
        print(f"Premiere event with ID {premiere_id} not found.")

# Coordinate appearances and logistics for celebrities
def coordinate_celebrity_appearances(appearance_id):
    appearance = None
    for app in appearances:
        if app["id"] == appearance_id:
            appearance = app
            break
    if appearance:
        # Implement celebrity appearance coordination logic here
        print(f"Coordinating appearance of '{appearance['celebrity']}' for event '{appearance['event']['name']}'")
    else:
        print(f"Celebrity appearance with ID {appearance_id} not found.")
       
        # Creating an event
        event_id = create_event("Movie Premiere", "2024-05-01", "Los Angeles")

        # Reading an event
        event = read_event(event_id)
        print(event)  # Output: {'id': 1, 'name': 'Movie Premiere', 'date': '2024-05-01', 'location': 'Los Angeles'}

        # Updating an event
        update_event(event_id, name="Updated Premiere Name")
        updated_event = read_event(event_id)
        print(updated_event)  # Output: {'id': 1, 'name': 'Updated Premiere Name', 'date': '2024-05-01', 'location': 'Los Angeles'}

        # Organizing a movie premiere
        organize_movie_premieres(event_id)  # Output: "Organizing movie premiere 'Updated Premiere Name' on 2024-05-01 at Los Angeles"

        # Deleting an event
        delete_event(event_id)

        # Coordinating celebrity appearances
        # Assuming there's an appearance with ID 1 for an event
        appearances.append({"id": 1, "celebrity": "Actor X", "event": event})
        coordinate_celebrity_appearances(1)  # Output: "Coordinating appearance of 'Actor X' for event 'Updated Premiere Name'"
