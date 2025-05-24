class MaintenanceState:

    def handle_request(self, elevator, floor):

        print(f"Elevador {elevator.name} está em manutenção.")
        print(f"Não pode atender solicitação para andar {floor}")
    
    def state_name(self):
        return "Manutenção"