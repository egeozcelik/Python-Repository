from enum import Enum
class DiskEvent(Enum):
    DISKEVENT_FIRST_CMD=1
    DISKEVENT_SECOND_CMD=2
    DISKEVENT_THIRD_CMD=3
    DISKEVENT_FORTH_CMD=4
    DISKEVENT_FIFTH_CMD=5
   

DiskEvents = {
    DiskEvent.DISKEVENT_FIRST_CMD.value: "1st info",
    DiskEvent.DISKEVENT_SECOND_CMD.value: "2nd info",
    DiskEvent.DISKEVENT_THIRD_CMD.value: "3nd info",
}




# def generate_disk_event_enum_and_dict(limit: int):
#     # Dynamically create the DiskEvent Enum class
#     enum_dict = {}
#     disk_events = {}
    
#     for i in range(1, limit + 1):
#         # Create the name for the enum member
#         member_name = f"DISKEVENT_{i:02d}_CMD"
        
#         # Add the member to the enum dictionary
#         enum_dict[member_name] = i
        
#         # Add the corresponding entry to the DiskEvents dictionary
#         disk_events[i] = f"{i}th info"
    
#     # Create the Enum class dynamically
#     DiskEvent = Enum('DiskEvent', enum_dict)
    
#     return DiskEvent, disk_events

# # Example usage
# limit = 17
# DiskEvent, DiskEvents = generate_disk_event_enum_and_dict(limit)

for event in DiskEvent:
    print(f"{event.name} - {event.value}")

for events, desc in DiskEvents.items():
    print(f"{events} - {desc}")