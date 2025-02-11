from tinydb import TinyDB, Query
class DeviceInformation_CPU:
    def __init__(self, name, core_count, clock_speed):
        self.name = name
        self.core_count = core_count
        self.clock_speed = clock_speed
db = TinyDB('CPUs.json')
CPUs = Query()

db.insert({'name':'Intel i3', 'core_count': 4,'clock_speed': 3.0})
db.insert({'name':'Intel i5', 'core_count': 6,'clock_speed': 4.1})
db.insert({'name':'Intel i7', 'core_count': 8,'clock_speed': 4.1})
db.insert({'name':'Intel i9', 'core_count': 12,'clock_speed': 5.1})

class DeviceInformation_GPU:
    def __init__(self, name, graphics_processor, cores, memory_capy, memory_bw):
        self.name = name
        self. grpahics_processor = graphics_processor
        self.cores = cores
        self.memory_capy = memory_capy

db.insert({'name':'Nvidia RTX 1050', 'core count':768 ,'memory capacity':'2048 MB', 'memory bandwith': '112 GB per second'})
db.insert({'name':'Nvidia RTX 2060', 'core count':1920 ,'memory capacity':'12 GB', 'memory bandwith':'336GB/s' })
db.insert({'name':'Nvidia RTX 3060', 'core count': 3584,'memory capacity': '12 GB', 'memory bandwith':'360.0 GB/s' })
db.insert({'name':'Nvidia RTX 4060', 'core count': 3072 ,'memory capacity':'8 GB', 'memory bandwith': '272 GB/s'})
#shop 
class Shop:
    def __init__(self, name, type, price):
        self.name = name
        self.type = type
        self.price = price

    def __repr__(self):
        return f"{self.name} ({self.type}) - £{self.price}"
cpu_shop = [
    Shop("Intel i3", "CPU", 70),
    Shop("Intel i5", "CPU", 120),
    Shop("Intel i7", "CPU", 200),
    Shop("Intel i9", "CPU", 300)
]

gpu_shop = [
    Shop("Nvidia RTX 1050", "GPU", 70),
    Shop("Nvidia RTX 2060", "GPU", 120),
    Shop("Nvidia RTX 3060", "GPU", 200),
    Shop("Nvidia RTX 4060", "GPU", 700)
]

ans3 = input("\nPlease type which of the following options you want to see:\n - CPU\n - GPU\n").strip().upper()

if ans3 == "CPU":
    print(cpu_shop)
elif ans3 == "GPU":
    print(gpu_shop)

def homepage():
    """Main homepage menu."""
    while True:
        print("\nHomepage Menu")
        print("1. Shop")
        print("2. Settings")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            ans3 = input("\nPlease type which of the following options you want to see:\n - CPU\n - GPU\n").strip().upper()
            if ans3 == "CPU":
                print("\nAvailable CPUs:")
                for cpu in cpu_shop:
                    print(cpu)
            elif ans3 == "GPU":
                print("\nAvailable GPUs:")
                for gpu in gpu_shop:
                    print(gpu)
            else:
                print("Invalid option. Please choose 'CPU' or 'GPU'.")

        elif choice == "2":
            print("Settings page (not implemented yet).")

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid input. Please enter 1, 2, or 3.")

