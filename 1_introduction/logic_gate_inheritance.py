class LogicGate():
    def __init__(self, name):
        self.name = name
        self.output = None

        def get_name(self):
            return self.name
        
        def get_output(self):
            self.output = self.perform_gate_logic()
            return self.output

class BinaryGate(LogicGate):
    def __init__(self, name):
        super().__init__(name)
        self.pin_a = None
        self.pin_b = None

    def set_pin_a(self, pin_a):
        self.pin_a = pin_a

    def set_pin_b(self, pin_b):
        self.pin_b = pin_b

class UnaryGate(LogicGate):
    def __init__(self, name):
        super().__init__(name)
        self.pin = None
    def get_pin(self):
        return int(input(f"Enter Pin input for gate {self.get_name()}-->"))
    
class AndGate(BinaryGate):
    def __init__(self, name):
        super().__init__(name)
    def perform_gate_logic(self):
        a = self.pin_a.get_output()
        b = self.pin_b.get_output()
        return 1 if a == 1 and b == 1 else 0
    