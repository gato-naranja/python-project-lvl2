from generate_diff.generate_diff import get_diff
from generate_diff.cli import parse


def main():
    print(
        get_diff(
            args.first_file,
            args.second_file,
            args.format,
            )
    )


args = parse()
if __name__ == '__main__':
    main()
