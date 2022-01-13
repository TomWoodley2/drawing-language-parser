
import time
import Interface
import FileReader

# use tkinter for drawing

#--------------------------------------------------------------------------------------------------

def main():

    meanings = {
        "P": {"instruction": "select_pen", "uses_value": 1},
        "D": {"instruction": "pen_down"},
        "W": {"instruction": "draw_west" , "uses_value": 1},
        "N": {"instruction": "draw_north", "uses_value": 1},
        "E": {"instruction": "draw_east" , "uses_value": 1},
        "S": {"instruction": "draw_south", "uses_value": 1},
        "U": {"instruction": "pen_up"},
    }

    file_handler = FileReader.FileReader(meanings)
    instruction_meaning_list = file_handler.read_file()

    print(instruction_meaning_list)
    # rendering

    # build up the interface using knowledge obtained from the file
    myapp = Interface.App()

    start_pos = (10,10)
    myapp.setup_window(start_pos)


    while True:
        #todo : what's the difference between these????
        myapp.update_idletasks()
        myapp.update()

        time.sleep(1)
        myapp.add_line('E', 50)
        myapp.add_line('S', 50)
    

#--------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()