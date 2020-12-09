from generate_diff.gendiff import generate_diff
from generate_diff.cli import take_apart_params


def main():
    print(
        generate_diff(
            args.first_file,
            args.second_file,
            args.format,
            )
    )


args = take_apart_params()
if __name__ == '__main__':
    main()
