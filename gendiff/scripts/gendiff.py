from gendiff.generate_diff import gendiff
from gendiff.cli import take_apart_params


def main():
    print(
        gendiff(
            args.first_file,
            args.second_file,
            args.format,
            )
    )


args = take_apart_params()
if __name__ == '__main__':
    main()
