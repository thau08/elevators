class NormalState:
    
    def handle_request(self, elevator, floor):

        print(f"Elevador {elevator.name} indo para andar {floor}")
        elevator.current_floor = floor
    
    def state_name(self):
        return "Normal"