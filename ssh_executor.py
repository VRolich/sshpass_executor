"""SSH Executor"""

import subprocess
import ssh_parser


class Executor:

    def __init__(self, cmd, password, subcmd, user):
        self.cmd = cmd + ' ' + password + ' ' + subcmd + ' ' + user

    def receive_data(self):
        """Process Linux 'ssh' Commands.

        Returns:
            ssh_dicts: list of data dicts.
        """
        p = subprocess.Popen(args=self.cmd.split(),
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        cmd_output, cmd_err = p.communicate()
        err = p.returncode

        ssh_dicts = ssh_parser.SSHParser(cmd_output, cmd_err, err).parser_to_dict()
        return ssh_dicts
