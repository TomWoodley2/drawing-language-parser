
import time
import Interface
import FileReader

# use tkinter for drawing

def select_pen(command, pen_type):
    print("pen selected : "+ pen_type)

def toggle_pen(command):
    print("toggling pen : " + command)

def draw(command, size):
    print("drawing : "+ command + "," + size)

#--------------------------------------------------------------------------------------------------

def main():

    meanings = {
        "P": {"instruction": "select_pen","function": select_pen,"uses_value": 1},
        "D": {"instruction": "pen_down","function": toggle_pen},
        "W": {"instruction": "draw_west" ,"function": draw, "uses_value": 1},
        "N": {"instruction": "draw_north","function": draw, "uses_value": 1},
        "E": {"instruction": "draw_east" ,"function": draw, "uses_value": 1},
        "S": {"instruction": "draw_south","function": draw, "uses_value": 1},
        "U": {"instruction": "pen_up","function": toggle_pen},
    }

    file_handler = FileReader.FileReader(meanings)
    command_meaning_list = file_handler.read_file()

    print(command_meaning_list)
    # rendering

    # build up the interface using knowledge obtained from the file
    myapp = Interface.App()

    start_pos = (10,10)
    myapp.setup_window(start_pos)

    for command in command_meaning_list:
        #todo : what's the difference between these????
        myapp.update()
        time.sleep(1)
        myapp.add_line('E', 50)
        meanings[command[0]]["function"](*command)

    # add keep window open here
    myapp.mainloop()
#--------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()