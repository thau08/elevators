from NormalState import NormalState

class Elevator:
    
    def __init__(self, elevator_name):

        self.name = elevator_name
        self.current_floor = 0
        self.current_state = NormalState()
        self.observers = []
    
    def add_observer(self, observer):

        self.observers.append(observer)
    
    def notify_observers(self, previous_state, new_state):
        for observer in self.observers:
            observer.elevator_change(self, previous_state, new_state)
    
    def change_state(self, new_state):
        previous_state = self.current_state.state_name()
        self.current_state = new_state
        new_state_name = self.current_state.state_name()
        self.notify_observers(previous_state, new_state_name)
    
    def request_elevator(self, floor):
        self.current_state.handle_request(self, floor)