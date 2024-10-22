from multiprocessing                import Process, Value
from ascend_descend                 import Ascend_Descend
from move_forward                   import Move_Forward
from kill_button_interface          import Kill_Button_Interface
from shared_memory_wrapper          import SharedMemoryWrapper
from MotorWrapper                   import Can_Wrapper

"""
    discord: @kialli
    github: @kchan5071
    
    This is the main file that will be run to start the program.
    
"""
def main():

    # create shared memory
    shared_memory_object = SharedMemoryWrapper()

    # can object

    # create objects
    kill_button_listener = Kill_Button_Interface(running = shared_memory_object.running)
    move_forward_obj = Move_Forward(shared_memory_object)
    ascend_descend_obj = Ascend_Descend(shared_memory_object) 
 

    #ADD OBJECTS HERE   

    #create processes
    kill_button_listener_process = Process(target=kill_button_listener.run_loop)
  
    move_forward_process = Process(target=move_forward_obj.run_loop)
    ascend_descend_process = Process(target=ascend_descend_obj.run_loop)

    #ADD PROCESSES HERE
    
    # start processes
    kill_button_listener_process.start()
    move_forward_process.start()
    ascend_descend_process.start()

    #ADD START PROCESSES HERE

    # wait for processes to finish
    kill_button_listener_process.join()
    move_forward_process.join()
    ascend_descend_process.join()

    #ADD JOIN PROCESSES HERE



    #END
    print("Program has finished")

if __name__ == '__main__':
    print("RUN FROM LAUNCH")
    main()
