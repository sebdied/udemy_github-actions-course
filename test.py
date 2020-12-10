import argparse

parser = argparse.ArgumentParser(add_help=True)

parser.add_argument(
    "-u",
    "--user",
    action="store",
    dest="username",
    help="The Username for authentication.",
)

parser.add_argument(
    "-e",
    "--environment",
    help="The Environment for the Action.",
)

parser.add_argument(
    "-m",
    "--msck",
    nargs="+",
    default=[],
    help="A space separated list of style CommunicationKeys to get.",
)

#
# Test
#

args = parser.parse_args()

username = args.username
environment = args.environment
styles = args.msck


def print_parameters():
    print("# # # Python Script Start # # #")
    print('User: {}, Environment: {}, Styles: {}'.format(username, environment, styles))
    print("# # # Python Script End # # #")


print_parameters()
