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

    def modify_event(self, event_id):
        """
        Allow users to modify event details including event name, speaker, date, time, and capacity.

        Parameters:
        - event_id: Identifier of the event to modify.
        """
        if event_id in self.events:
            print(f"Modifying event with ID '{event_id}':")

            # Prompt the user for modifications
            self.events[event_id]['event_name'] = input("Enter Event Name: ")
            self.events[event_id]['speaker_name'] = input("Enter Speaker Name (Optional): ")
            self.events[event_id]['date'] = input("Enter Date: ")
            self.events[event_id]['time'] = input("Enter Time: ")
            self.events[event_id]['capacity'] = int(input("Enter Capacity: "))

            print(f"Event with ID '{event_id}' has been modified.")
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
            print(f"Time: {event_info.get('time', 'N/A')}")
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
        time = input("Enter Time: ")
        capacity = int(input("Enter Capacity: "))
        speaker_name = input("Enter Speaker Name (Optional): ")

        self.add_event(event_id, event_name, speaker_name, f"{date} {time}", capacity)  # Combining date and time

    def register_event(self):
        """
        Allow users to register for an event by providing their name, event ID, and the number of attendees.
        """
        event_id = int(input("Enter Event ID to register: "))

        if event_id in self.events:
            event_info = self.events[event_id]
            attendee_name = input("Enter Your Name: ")
            num_attendees = int(input("Enter the Number of Attendees: "))
            latest_capacity = event_info['capacity'] - len(event_info['attendees'])

            if num_attendees <= latest_capacity and num_attendees > 0:
                # Check if there is enough capacity for the attendees
                for _ in range(num_attendees):
                    event_info['attendees'].append(attendee_name)
                print(f"Congratulations, {attendee_name}! You are registered for event '{event_info['event_name']}'.")
            elif num_attendees <= 0:
                print("Please enter a valid number of attendees (greater than zero).")
            else:
                print(f"Sorry, {attendee_name}. The event '{event_info['event_name']}' is fully booked.")
        else:
            print(f"Event with ID '{event_id}' not found in the database.")

    def view_event_capacity(self):
        """
        Allow users to view the latest capacity of an event by providing the event ID.
        """
        event_id = int(input("Enter Event ID to view capacity: "))

        if event_id in self.events:
            event_info = self.events[event_id]
            latest_capacity = event_info['capacity'] - len(event_info['attendees'])
            print(f"The latest capacity for event '{event_info['event_name']}' is {latest_capacity}.")
        else:
            print(f"Event with ID '{event_id}' not found in the database.")

# Text-based interface
event_db = EventDatabase()

while True:
    print("\nSelect an option:")
    print("1. Create Event")
    print("2. Modify Event")
    print("3. Display Event Info")
    print("4. Register Event")
    print("5. View Event Capacity")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        # Create Event
        event_db.create_event()
    elif choice == '2':
        # Modify Event
        event_id = int(input("Enter Event ID to modify: "))
        event_db.modify_event(event_id)
    elif choice == '3':
        # Display Event Info
        event_id = int(input("Enter Event ID: "))
        event_db.display_event_info(event_id)
    elif choice == '4':
        # Register Event
        event_db.register_event()
    elif choice == '5':
        # View Event Capacity
        event_db.view_event_capacity()
    elif choice == '6':
        # Exit
        print("Exiting the Event Database. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
