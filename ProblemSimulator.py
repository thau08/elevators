# Importa os estados que o simulador pode aplicar
from StuckState import StuckState
from MaintenanceState import MaintenanceState
from NormalState import NormalState

class ProblemSimulator:

    def __init__(self, central_monitor):
        self.central = central_monitor
    
    def simulate_stuck(self, elevator_name):
        for elevator in self.central.elevators:
            if elevator.name == elevator_name:
                print(f"SIMULAÇÃO: Emperrando elevador {elevator_name}")
                elevator.change_state(StuckState())
                return
        print(f"Elevador {elevator_name} não encontrado")
    
    def simulate_maintenance(self, elevator_name):
        for elevator in self.central.elevators:
            if elevator.name == elevator_name:
                print(f"SIMULAÇÃO: Colocando elevador {elevator_name} em manutenção")
                elevator.change_state(MaintenanceState())
                return
        print(f"Elevador {elevator_name} não encontrado")
    
    def fix_elevator(self, elevator_name):
        for elevator in self.central.elevators:
            if elevator.name == elevator_name:
                print(f"SIMULAÇÃO: Consertando elevador {elevator_name}")
                elevator.change_state(NormalState())
                return
        print(f"Elevador {elevator_name} não encontrado")