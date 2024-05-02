# Event Planner

events = {}

def add_event():
    event_name = input("Enter the event name: ")
    event_date = input("Enter the event date (MM/DD/YYYY): ")
    event_guests = int(input("Enter the number of celebrities: "))
    events[event_name] = {"date": event_date, "guests": event_guests}
    print(f"Event '{event_name}' added successfully.")

def view_events():
    if not events:
        print("No events found.")
    else:
        print("Upcoming Events:")
        for event, details in events.items():
            print(f"Event: {event}")
            print(f"Date: {details['date']}")
            print(f"Number of celebrities: {details['guests']}")
            print("-" * 2)

while True:
    choice = input("Enter 'add' to add a new event, 'view' to view upcoming events, or 'quit' to exit: ")
    if choice.lower() == 'add':
        add_event()
    elif choice.lower() == 'view':
        view_events()
    elif choice.lower() == 'quit':
        break
    else:
        print("Invalid choice. Please try again.")


