class EventDatabase:
    def __init__(self):
        """
        Initialize the EventDatabase with an empty dictionary to store events.
        """
        self.events = {}

    def add_event(self, event_id, event_name, speaker_name=None, date=None, capacity=None):
        if event_id not in self.events:
            self.events[event_id] = {
                'event_name': event_name,
                'speaker_name': speaker_name,
                'date': date,
                'capacity': capacity,
                'attendees': [],
                'feedback': {
                    'event_rating': None,
                    'additional_comment': None
                }
            }
            print(f"Event '{event_name}' added to the database.")
        else:
            print(f"Event with ID '{event_id}' already exists in the database.")

    def modify_event(self, event_id):
        if event_id in self.events:
            print(f"Modifying event with ID '{event_id}':")

            self.events[event_id]['event_name'] = input("Enter Event Name: ")
            self.events[event_id]['speaker_name'] = input("Enter Speaker Name (Optional): ")
            self.events[event_id]['date'] = input("Enter Date: ")
            self.events[event_id]['time'] = input("Enter Time: ")
            self.events[event_id]['capacity'] = int(input("Enter Capacity: "))

            print(f"Event with ID '{event_id}' has been modified.")
        else:
            print(f"Event with ID '{event_id}' not found in the database.")

    def display_event_info(self, event_id):
        if event_id in self.events:
            event_info = self.events[event_id]
            print(f"Event ID: {event_id}")
            print(f"Event Name: {event_info['event_name']}")
            print(f"Speaker Name: {event_info['speaker_name']}")
            print(f"Date: {event_info['date']}")
            print(f"Time: {event_info.get('time', 'N/A')}")
            print(f"Capacity: {event_info['capacity']}")
            print(f"Attendees: {', '.join(event_info['attendees'])}")
            feedback_info = event_info['feedback']
            print(f"Event Rating: {feedback_info['event_rating']}")
            print(f"Additional Comment: {feedback_info['additional_comment']}")
        else:
            print(f"Event with ID '{event_id}' not found in the database.")

    def create_event(self):
        event_id = int(input("Enter Event ID: "))
        event_name = input("Enter Event Name: ")
        date = input("Enter Date: ")
        time = input("Enter Time: ")
        capacity = int(input("Enter Capacity: "))
        speaker_name = input("Enter Speaker Name (Optional): ")

        self.add_event(event_id, event_name, speaker_name, f"{date} {time}", capacity)

    def register_event(self):
        event_id = int(input("Enter Event ID to register: "))

        if event_id in self.events:
            event_info = self.events[event_id]
            attendee_name = input("Enter Your Name: ")
            num_attendees = int(input("Enter the Number of Attendees: "))
            latest_capacity = event_info['capacity'] - len(event_info['attendees'])

            if num_attendees <= latest_capacity and num_attendees > 0:
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
        event_id = int(input("Enter Event ID to view capacity: "))

        if event_id in self.events:
            event_info = self.events[event_id]
            latest_capacity = event_info['capacity'] - len(event_info['attendees'])
            print(f"The latest capacity for event '{event_info['event_name']}' is {latest_capacity}.")
        else:
            print(f"Event with ID '{event_id}' not found in the database.")

    def customer_feedback(self):
        event_id = int(input("Enter Event ID for feedback: "))

        if event_id in self.events:
            event_info = self.events[event_id]
            event_rating = int(input("Enter Event Rating (from 1 to 10): "))
            additional_comment = input("Enter Additional Comment (up to 150 words): ")

            if 1 <= event_rating <= 10:
                event_info['feedback']['event_rating'] = event_rating
                event_info['feedback']['additional_comment'] = additional_comment[:150]
                print("Thank you for your feedback!")
            else:
                print("Please enter a valid event rating between 1 and 10.")
        else:
            print(f"Event with ID '{event_id}' not found in the database.")

    def customer_loyalty(self):
        customer_name = input("Enter Your Name: ")

        total_registered_events = 0
        total_loyalty_points = 0

        for event_info in self.events.values():
            total_registered_events += event_info['attendees'].count(customer_name)
            total_loyalty_points += event_info['loyalty_points']

        print(f"{customer_name}, you have registered for {total_registered_events} events.")
        print(f"Total Loyalty Points: {total_loyalty_points}")

    def generate_report(self):
        event_id = int(input("Enter Event ID to generate a report: "))

        if event_id in self.events:
            event_info = self.events[event_id]
            latest_capacity = event_info['capacity']
            total_capacity = latest_capacity
            unique_attendees = set(event_info['attendees'])

            print(f"Report for Event '{event_info['event_name']}' (Event ID: {event_id}):")
            print(f"Latest Event Capacity: {latest_capacity}")
            print("Attendees:")
            for idx, attendee in enumerate(unique_attendees):
                print(f"- {attendee}")
            print(f"\nTotal Capacity of Event Attendees: {total_capacity}")
            print("\nCustomer Feedback:")
            for idx, attendee in enumerate(unique_attendees):
                feedback_info = event_info['feedback']
                print(f"{idx + 1}. Attendee: {attendee}")
                print(f"   Event Rating: {feedback_info['event_rating']}")
                print(f"   Additional Comment: {feedback_info['additional_comment']}")
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
    print("6. Customer Feedback")
    print("7. Customer Loyalty")
    print("8. Generate Report")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

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
        # Customer Feedback
        event_db.customer_feedback()
    elif choice == '7':
        # Customer Loyalty
        event_db.customer_loyalty()
    elif choice == '8':
        # Generate Report
        event_db.generate_report()
    elif choice == '9':
        # Exit
        print("Exiting the Event Database. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 9.")
