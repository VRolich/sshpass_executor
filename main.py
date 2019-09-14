"""Main module to run the program"""

import argparse
import ssh_executor


def create_cmd_line_interface():
    parser = argparse.ArgumentParser(description='Please choose one SSHPASS Linux command')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-f', '--file', help='Take password to use from file', action='store_true')
    group.add_argument('-p', '--password', help='Provide password as argument', action='store_true')
    parser.add_argument('password', type=str, help='Enter password')

    option_group = parser.add_mutually_exclusive_group()
    option_group.add_argument('--ssh', action='store_true')
    option_group.add_argument('--scp', action='store_true')
    parser.add_argument('--user', type=str, help='Enter user')

    args = parser.parse_args()
    return args


def main():
    args = create_cmd_line_interface()
    if args.f:
        if args.scp:
            executor = ssh_executor.Executor('sshpass -f', args.password, 'scp', args.user)
        else:
            executor = ssh_executor.Executor('sshpass -f', args.password, 'ssh', args.user)
    else:
        if args.scp:
            executor = ssh_executor.Executor('sshpass -p', args.password, 'scp', args.user)
        else:
            executor = ssh_executor.Executor('sshpass -p', args.password, 'ssh', args.user)
    output = executor.receive_data()
    print(output)


if __name__ == '__main__':
    main()
