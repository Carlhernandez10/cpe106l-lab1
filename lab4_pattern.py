class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance
    
Logger1 = Logger()
Logger2 = Logger()

# Testing the singleton behavior
print("Logger1 ID:", id(Logger1)) 
print("Logger2 ID:", id(Logger2)) 
print("Same instance:", Logger1 is Logger2)