import argparse


def take_apart_params():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f',
        '--format',
        type=str,
        default='stylish',
        help='set format of output',
    )
    return parser.parse_args()
