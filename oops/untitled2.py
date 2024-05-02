events = {}

def add_event():
    event_name = input("Enter the event name: ")
    event_date = input("Enter the event date (MM/DD/YYYY): ")
    event_details = input("Enter the event details: ")
    events[event_name] = {"date": event_date, "details": event_details}
    print("Event added successfully!")

def view_events():
    if not events:
        print("No events scheduled yet.")
    else:
        print("Upcoming Events:")
        for event_name, event_data in events.items():
            print(f"\nEvent Name: {event_name}")
            print(f"Date: {event_data['date']}")
            def remove_event():
               event_name = input("Enter the event name to remove: ")
    if event_name in events:
        del events[event_name]
        print("Event removed successfully!")
    else:
        print("Event not found.")

while True:
    print("\nPremiere Event Planner")
    print("1. Add Event")
    print("2. View Events")
    print("3. Remove Event")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        add_event()
    elif choice == "2":
        view_events()
    elif choice == "3":
        remove_event()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")