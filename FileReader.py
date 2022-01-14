class FileReader():

#--------------------------------------------------------------------------------------------------

    def __init__(self, meanings):
        self.meanings = meanings
        self.command_file_positions = {
            "command" : 0,
            "value"   : 2
        }
        self.order = ("command", "value")

#--------------------------------------------------------------------------------------------------

    def read_file(self):
        file_name = "rectangle.draw"
        file_handle = open(file_name, "r")

        command_meaning_list = []

        for line in file_handle:
            command_bindings = self._extract_line_instructions(line)
            command_meaning_list.append(self._convert_command_to_meaning(command_bindings))

        file_handle.close()

        return command_meaning_list
#--------------------------------------------------------------------------------------------------
    # bind the data in the file based on file position
    def _extract_line_instructions(self, line):
        command_data_mapping = {}

        for binding in self.order:
            start = self.command_file_positions[binding]
            end   = self.command_file_positions[binding] + 1
            command = line[slice(start, end)]

            # only add to output if we have a value
            if command:
                command_data_mapping[binding] = command

        return command_data_mapping

#--------------------------------------------------------------------------------------------------

    def _convert_command_to_meaning(self, command_bindings):
        instruction_value_storage = []

        command = command_bindings["command"]

        if command not in self.meanings:
            print("command defined in file '" + command + "' has no meaning")
            return -1;

        instruction_value_storage.append(command)

        if "uses_value" in self.meanings[command]:
            if "value" in command_bindings:
                value = command_bindings["value"]
                instruction_value_storage.append(value)
            else:
                print("value not provided for command '"+ command + "' where a value was expected")
                
        return instruction_value_storage

#--------------------------------------------------------------------------------------------------