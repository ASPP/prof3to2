import argparse
import marshal


def convert_prof_3_to_2(prof3_filename, prof2_filename):
    """ Read a Python3 profile file and output a Python2 profile file. """

    with open(prof3_filename, 'rb') as f:
        prof3 = marshal.load(f)

    with open(prof2_filename, 'wb') as f:
        marshal.dump(prof3, f, 2)


def main():
    """`prof3to2` entry point."""
    parser = argparse.ArgumentParser(
        description='Transform a Python3 profile file in a Python2 profile '
                    'file, so you can use ancient tools like RunSnakeRun.'
    )
    parser.add_argument('prof3_filename', type=str,
                        help='filename of the input Python3 profile file')
    parser.add_argument('prof2_filename', type=str,
                        help='filename of the output Python2 profile file')
    args = parser.parse_args()

    convert_prof_3_to_2(args.prof3_filename, args.prof2_filename)
