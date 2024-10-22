from multiprocessing import Process, Value
from subprocess import call
import time

class Ascend_Descend:
    def __init__(self, shared_memory_object):
        self.shared_memory_object = shared_memory_object


    def run_loop(self):
        while self.shared_memory_object.running.value:
            #write code here
            if (self.shared_memory_object.move_up_down.value == 1):
                # print statement
                print("move up")
                # motor command
                self.shared_memory_object.can_wrapper.move_up(20)
                self.shared_memory_object.can_wrapper.send_command()
            else:
                # print statement
                print("move down")
                # motor command
                self.shared_memory_object.can_wrapper.move_down(20)
                self.shared_memory_object.can_wrapper.send_command()
                
            time.sleep(1)   # move alternatively up or down every 1 second
            #end
            pass
