class Engine:
    def __init__(self, horsepower: int, fuel_type: str, **kwargs):
        super().__init__(**kwargs)
        self.horsepower = horsepower
        self.fuel_type = fuel_type

    def start_engine(self):
        return f"Двигун запущено. Потужність: {self.horsepower} к.с., тип палива: {self.fuel_type}."

class Electronics:
    def __init__(self, screen_resolution: str, has_autopilot: bool, **kwargs):
        super().__init__(**kwargs)
        self.screen_resolution = screen_resolution
        self.has_autopilot = has_autopilot

    def diagnostic_system(self):
        return f"Електроніка активована. Роздільна здатність екрана: {self.screen_resolution}, автопілот: {self.has_autopilot}."

class SmartCar(Engine, Electronics):
    def __init__(self, brand: str, horsepower: int, fuel_type: str, screen_resolution: str, has_autopilot: bool):
        super().__init__(
            horsepower=horsepower,
            fuel_type=fuel_type,
            screen_resolution=screen_resolution,
            has_autopilot=has_autopilot
        )
        self.brand = brand

    def car_info(self):
        return f"Автомобіль: {self.brand}"

# Проверка работы:
car = SmartCar(
    brand="Tesla Model S",
    horsepower=670,
    fuel_type="Електрика",
    screen_resolution="4K",
    has_autopilot=True
)

print(car.car_info())
print(car.start_engine())
print(car.diagnostic_system())