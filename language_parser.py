
import time
import interface


# use tkinter for drawing
#--------------------------------------------------------------------------------------------------

def carry_out_command(command_bindings):
    meanings = {
        "P": {"instruction": "select pen", "uses_value": 1},
        "D": {"instruction": "pen down"},
        "W": {"instruction": "draw west" , "uses_value": 1},
        "N": {"instruction": "draw north", "uses_value": 1},
        "E": {"instruction": "draw east" , "uses_value": 1},
        "S": {"instruction": "draw south", "uses_value": 1},
        "U": {"instruction": "pen up"},
    }

    command = command_bindings["command"]

    if command in meanings:
        instruction = meanings[command]["instruction"]
    else:
        print("command defined in file '" + command + "' has no meaning")
        return -1;
    
    print ("command to be carried out : " + instruction)

    if "uses_value" in meanings[command]:
        if "value" in command_bindings:
            value = command_bindings["value"]
        else:
            print("value not provided for command '"+ command + "' where a value was expected")
        
        print ("value to be used : " + value)

#--------------------------------------------------------------------------------------------------

def extract_line_instructions(line):
    command_bindings = {
        "command"  : 0,
        "value"    : 2
    }

    order = ("command", "value")

    output_bindings = {}

    for binding in order:
        start = command_bindings[binding]
        end   = command_bindings[binding] + 1
        command = line[slice(start, end)]

        # only add to output if we have a value
        if command:
            output_bindings[binding] = command
    
    return output_bindings

#--------------------------------------------------------------------------------------------------

def main():

    file_name = "rectangle.draw"
    file_handle = open(file_name,"r")

    # build up the interface using knowledge obtained from the file
    myapp = interface.App()
    myapp.setup_window()
    
    for line in file_handle:
        #print(line)
        command_bindings = extract_line_instructions(line)
        carry_out_command(command_bindings)
        
    file_handle.close()

    while True:
        # todo : what's the difference between these????
        myapp.update_idletasks()
        myapp.update()

        time.sleep(1)
        myapp.add_line()
    

#--------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()