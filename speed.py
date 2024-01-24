def speeding_ticket(speed, is_birthday):
    # Define speed limits
    no_ticket_limit = 60
    small_ticket_limit = 80

    # Increase speed limits by 5 mph on the birthday
    if is_birthday:
        no_ticket_limit += 5
        small_ticket_limit += 5

    # Evaluate speeding conditions
    if speed <= no_ticket_limit:
        return "No Ticket"
    elif no_ticket_limit < speed <= small_ticket_limit:
        return "Small Ticket"
    else:
        return "Big Ticket"

# Test cases
print(speeding_ticket(60, False))  # Expected output: "No Ticket"
print(speeding_ticket(75, False))  # Expected output: "Small Ticket"
print(speeding_ticket(85, False))  # Expected output: "Big Ticket"
print(speeding_ticket(65, True))   # Expected output: "No Ticket"
print(speeding_ticket(85, True))   # Expected output: "Small Ticket"