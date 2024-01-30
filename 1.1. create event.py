class EventDatabase:
    def __init__(self):
        """
        Initialize the EventDatabase with an empty dictionary to store events.
        """
        self.events = {}

    def add_event(self, event_id, event_name, speaker_name=None, date=None, capacity=None):
        """
        Add a new event to the database.

        Parameters:
        - event_id: Unique identifier for the event.
        - event_name: Name of the event.
        - speaker_name: (Optional) Name of the speaker.
        - date: (Optional) Date of the event.
        - capacity: (Optional) Maximum capacity of the event.
        """
        if event_id not in self.events:
            # Create a new entry for the event in the dictionary
            self.events[event_id] = {
                'event_name': event_name,
                'speaker_name': speaker_name,
                'date': date,
                'capacity': capacity,
                'attendees': []
            }
            print(f"Event '{event_name}' added to the database.")
        else:
            print(f"Event with ID '{event_id}' already exists in the database.")

    def add_attendee(self, event_id, attendee_name):
        """
        Add an attendee to a specific event.

        Parameters:
        - event_id: Identifier of the event.
        - attendee_name: Name of the attendee to be added.
        """
        if event_id in self.events:
            if len(self.events[event_id]['attendees']) < self.events[event_id]['capacity']:
                # Add the attendee to the list of attendees for the event
                self.events[event_id]['attendees'].append(attendee_name)
                print(f"{attendee_name} added to the attendees list for event '{self.events[event_id]['event_name']}'.")
            else:
                print(f"Event '{self.events[event_id]['event_name']}' is at full capacity. Cannot add more attendees.")
        else:
            print(f"Event with ID '{event_id}' not found in the database.")

    def display_event_info(self, event_id):
        """
        Display information about a specific event.

        Parameters:
        - event_id: Identifier of the event to display.
        """
        if event_id in self.events:
            event_info = self.events[event_id]
            print(f"Event ID: {event_id}")
            print(f"Event Name: {event_info['event_name']}")
            print(f"Speaker Name: {event_info['speaker_name']}")
            print(f"Date: {event_info['date']}")
            print(f"Capacity: {event_info['capacity']}")
            print(f"Attendees: {', '.join(event_info['attendees'])}")
        else:
            print(f"Event with ID '{event_id}' not found in the database.")

    def create_event(self):
        """
        Allow users to create event details including event ID, event name, date, speaker (optional), and capacity.
        """
        event_id = int(input("Enter Event ID: "))
        event_name = input("Enter Event Name: ")
        date = input("Enter Date: ")
        capacity = int(input("Enter Capacity: "))
        speaker_name = input("Enter Speaker Name (Optional): ")

        self.add_event(event_id, event_name, speaker_name, date, capacity)


# Text-based interface
event_db = EventDatabase()

while True:
    print("\nSelect an option:")
    print("1. Create Event")
    print("2. Add Attendee")
    print("3. Display Event Info")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        # Create Event
        event_db.create_event()
    elif choice == '2':
        # Add Attendee
        event_id = int(input("Enter Event ID: "))
        attendee_name = input("Enter Attendee Name: ")
        event_db.add_attendee(event_id, attendee_name)
    elif choice == '3':
        # Display Event Info
        event_id = int(input("Enter Event ID: "))
        event_db.display_event_info(event_id)
    elif choice == '4':
        # Exit
        print("Exiting the Event Database. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
