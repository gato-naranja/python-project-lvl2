import argparse
from generate_diff.generate_diff import gendiff


def main():
    gendiff(
            args.first_file,
            args.second_file,
            )


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument(
        '-f',
        '--format',
        type=str,
        default='FORMAT',
        help='set format of output',
)
args = parser.parse_args()
if __name__ == '__main__':
    main()
