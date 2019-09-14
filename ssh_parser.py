"""SSH Parser"""


class SSHParser:
    def __init__(self, cmd_output, cmd_err, err):
        self._cmd_output = cmd_output
        self._cmd_err = cmd_err
        self._err = err
        self._cmd_execution_result = {}

    @staticmethod
    def parser_to_str(byte_input):
        """Parser Byte Date to sting lines.
        Args:
            byte_input: input date of byte type.
        Returns:
            lines: string lines list.
        """
        byte_input = byte_input.decode("utf-8")
        byte_input = byte_input.replace("Mounted on", "Mounted_on")
        lines = byte_input.splitlines()
        lines = list(line.split() for line in lines)
        return lines

    def parser_to_dict(self, byte_input):
        """Parser Byte Date to Dictionary.
        Args:
            byte_input: input date of byte type.
        Returns:
            data_list: a list of dicts.
        """
        lines = self.parser_to_str(byte_input)
        data_list = []
        for i in range(1, len(lines[0])):
            data_dict = dict(zip(lines[0], lines[i]))
            data_list.append(data_dict)
        return data_list
