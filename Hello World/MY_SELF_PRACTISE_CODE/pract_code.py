class Computer:
    
    station = 0
    laptop = 0
    
    def __init__(self, mark, processor, op_memory, video_adapter, disk_size, display_size):
        self.mark = mark
        self.processor = processor
        self.op_memory = op_memory
        self.video_adapter = video_adapter
        self.disk_size = disk_size
        self.display_size = display_size
    
    def add_machine(self, machine_type='pc'):
        return self.station if machine_type == 'pc' else self.laptop
    

class PC(Computer):
    
    def __init__(self, mark, processor, op_memory, video_adapter, disk_size, display_size):
        Computer().__init__(mark, processor, op_memory, video_adapter, disk_size, display_size)    
        print('PC is added to ' + self.station)
        
class Laptop(Computer):
    
    def __init__(self, mark, processor, op_memory, video_adapter, disk_size, display_size):
        Computer().__init__(mark, processor, op_memory, video_adapter, disk_size, display_size)
        print('Laptop is added to ' + self.laptop)
        
        
dell = PC