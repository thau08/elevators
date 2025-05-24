class CentralMonitor:

    _centralMonitorInstance = None

    def __new__(cls): #class
        if(cls._centralMonitorInstance is None):
            cls._centralMonitorInstance = super().__new__(cls)
            cls._centralMonitorInstance.initialized = False
        return cls._centralMonitorInstance
  
    def __init__(self):
        if self.initialized == False:
            print("Inicializando a Central pela primeira vez")
            self.elevators = []
            self.initialized = True
        pass

    def add_elevator(self, elevator):
        self.elevators.append(elevator)
        elevator.add_observer(self)
        print(f"Central está monitorando o elevador {elevator.name}")

    def elevator_change(self, elevator, previous_state, new_state):
        print(f"Elevador {elevator.name} mudou de {previous_state} para {new_state}")
              
         # Reações específicas baseadas no novo estado
        if new_state == "Emperrado":
            self.react_stuck_elevator(elevator)
        elif new_state == "Manutenção":
            self.react_maintenance(elevator)
        elif new_state == "Normal":
            print(f"Elevador {elevator.name} voltou ao normal")
    
    def react_stuck_elevator(self, elevator):
        print(f"Elevador {elevator.name} está emperrado")
        print("Central acionando técnicos e notificando usuários!")
    
    def react_maintenance(self, elevator):
        print(f"Elevador {elevator.name} fora de serviço")
        
        working_elevators = 0
        for elev in self.elevators:
            if elev.current_state.state_name() == "Normal":
                working_elevators += 1
        
        print(f"Central informa: {working_elevators} elevadores ainda disponíveis")
    
    def general_report(self):
        print(f"\n=== RELATÓRIO DA CENTRAL ===")
        print(f"Total de elevadores: {len(self.elevators)}")
        for elevator in self.elevators:
            print(f"- Elevador {elevator.name}: {elevator.current_state.state_name()} (Andar {elevator.current_floor})")
        print("=============================\n")