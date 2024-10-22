from multiprocessing import Process, Value
from subprocess import call
import time


class Move_Forward:
    def __init__(self, shared_memory_object):
        self.shared_memory_object = shared_memory_object


    def run_loop(self):
        while self.shared_memory_object.running.value:
            #  write code here
            #  print statement
            print("move forward")
            
            # motor command
            self.shared_memory_object.can_wrapper.move_forward(20)
            self.shared_memory_object.can_wrapper.send_command()
            # toggle between for move forward value
            if (self.shared_memory_object.move_up_down.value == 1):
                self.shared_memory_object.move_up_down.value = 0
            else:

                self.shared_memory_object.move_up_down.value = 1

            #end
            time.sleep(1/3)     # move forward every 1/3 second
            
            pass
