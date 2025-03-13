from abc import ABC, abstractmethod
from collections import defaultdict
from typing import Dict, List

# Абстрактный базовый класс для устройств
class Device(ABC):
    def __init__(self, name: str):
        self._name = name  # Инкапсуляция: приватный атрибут

    @property
    def name(self) -> str:  # Getter для имени
        return self._name

    @name.setter
    def name(self, new_name: str):  # Setter для имени
        if not new_name:
            raise ValueError("Имя устройства не может быть пустым!")
        self._name = new_name

    @abstractmethod
    def turn_on(self) -> str:  # Абстрактный метод (должен быть реализован в подклассах)
        pass

    @abstractmethod
    def turn_off(self) -> str:  # Абстрактный метод
        pass

    def __str__(self) -> str:  # Магический метод для строкового представления
        return f"{self.__class__.__name__}: {self._name}"

# Устройство: Умная лампа
class SmartLight(Device):
    def turn_on(self) -> str:
        return f"{self._name} включена. Свет яркий!"

    def turn_off(self) -> str:
        return f"{self._name} выключена. Темнота."

# Устройство: Умный термостат
class SmartThermostat(Device):
    def turn_on(self) -> str:
        return f"{self._name} включен. Температура регулируется."

    def turn_off(self) -> str:
        return f"{self._name} выключен. Температура не контролируется."

# Фабрика для создания устройств
class DeviceFactory:
    @staticmethod
    def create_device(device_type: str, name: str) -> Device:
        if device_type == "Light":
            return SmartLight(name)
        elif device_type == "Thermostat":
            return SmartThermostat(name)
        else:
            raise ValueError("Неизвестный тип устройства")

# Система управления умным домом (Singleton)
class SmartHomeSystem:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.devices: Dict[str, List[Device]] = defaultdict(list)  # Используем defaultdict
        return cls._instance

    def add_device(self, device: Device):  # Добавление устройства
        self.devices[device.__class__.__name__].append(device)

    def turn_on_all_devices(self) -> List[str]:  #Включение всех устройств
        results = []
        for device_type, devices in self.devices.items():
            for device in devices:
                results.append(device.turn_on())
        return results

    def turn_off_all_devices(self) -> List[str]:  #Выключение всех устройств
        results = []
        for device_type, devices in self.devices.items():
            for device in devices:
                results.append(device.turn_off())
        return results

    def __str__(self) -> str:  #Магический метод для строкового представления
        return f"Умный дом: {len(self.devices)} типов устройств, всего {sum(len(devices) for devices in self.devices.values())} устройств"

#Пример использования
if __name__ == "__main__":
    #Создаем устройства с помощью фабрики
    light1 = DeviceFactory.create_device("Light", "Гостиная лампа")
    light2 = DeviceFactory.create_device("Light", "Кухонная лампа")
    thermostat = DeviceFactory.create_device("Thermostat", "Термостат в зале")

    #Создаем систему умного дома (Singleton)
    smart_home = SmartHomeSystem()

    #Добавляем устройства в систему
    smart_home.add_device(light1)
    smart_home.add_device(light2)
    smart_home.add_device(thermostat)


    print("Включаем все устройства:")
    for result in smart_home.turn_on_all_devices():    #Включаем все 
        print(result)

     
    print("\nИнформация о системе:")
    print(smart_home)
      #Информация о системе