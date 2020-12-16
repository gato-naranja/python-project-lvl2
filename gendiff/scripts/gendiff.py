from gendiff.generate_diff import generate_diff
from gendiff.cli import take_apart_params


def main():
    args = take_apart_params()
    print(
        generate_diff(
            args.first_file,
            args.second_file,
            args.format,
        )
    )


if __name__ == '__main__':
    main()
