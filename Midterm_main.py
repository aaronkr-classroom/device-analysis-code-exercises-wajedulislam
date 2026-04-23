from lib.room_sensor import RoomSensor

# Part 3: Create and Store Multiple Objects
sensors = [
    RoomSensor("Kitchen", 31, 72, 180),  
    RoomSensor("Bedroom", 22, 50, 250), 
    RoomSensor("Balcony", 25, 65, 500)   
]

# Part 5: Initialize counters for the Bonus Challenge
stats = {
    "Comfortable": 0,
    "Normal": 0,
    "Warning": 0
}

# Part 4: Loop Through the List
for sensor in sensors:
    # Print the sensor info using the method
    sensor.show_info()
    
    # Get and print status strings
    comfort = sensor.comfort_level()
    light = sensor.light_status()
    
    print(f"Comfort Level: {comfort}")
    print(f"Light Status: {light}")
    print("-" * 20) # Visual separator
    
    # Part 5: Update the totals
    stats[comfort] += 1

# Print the totals for the Extra Challenge
print("Final Summary:")
for category, count in stats.items():
    print(f"{category}: {count}")