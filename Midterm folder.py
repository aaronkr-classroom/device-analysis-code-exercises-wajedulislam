class RoomSensor:
    """
    Consolidated Room Sensor class for the Midterm Task.
    """
    def __init__(self, name, temperature, humidity, light):
        # Part 1: Constructor receiving all 4 values
        self.name = name
        self.temperature = temperature
        self.humidity = humidity
        self.light = light

    # Part 2: Methods
    def show_info(self):
        """Prints all sensor information in the required format."""
        print(f"Sensor: {self.name}")
        print(f"Temperature: {self.temperature}")
        print(f"Humidity: {self.humidity}")
        print(f"Light: {self.light}")

    def comfort_level(self):
        """Logic for Comfortable, Warning, or Normal status."""
        if 20 <= self.temperature <= 26 and 40 <= self.humidity <= 60:
            return "Comfortable"
        elif self.temperature >= 30 or self.humidity >= 70:
            return "Warning"
        else:
            return "Normal"

    def light_status(self):
        """Logic for light intensity levels."""
        if self.light < 200:
            return "Dark"
        else:
            return "Bright"