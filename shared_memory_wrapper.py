from multiprocessing    import Value, Array
from MotorWrapper       import Can_Wrapper



class SharedMemoryWrapper:
    def __init__(self):
        # add properties here
        # self.example_array          = Array('i', [1, 2, 3, 4, 5])
        self.running                = Value('i', 1)
        self.move_up_down           = Value('i', True)  # true - move up, false - move down
        
        # can object
        self.can_wrapper            =  Can_Wrapper()