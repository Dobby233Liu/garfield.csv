"""
CLI for the convert module based on argparse.

Usage:

give -h as an argument while running this file
"""

from argparse import ArgumentParser, ArgumentTypeError
import sys
from garfieldcsv import convert


class FileTypeMine(object):
    """Factory for creating file object types

    Instances of FileType are typically passed as type= arguments to the
    ArgumentParser add_argument() method.
    """

    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs

    def __call__(self, string):
        # the special argument "-" means sys.std{in,out}
        if string == "-":
            if "r" in self._kwargs["mode"]:
                return sys.stdin
            elif "w" in self._kwargs["mode"]:
                return sys.stdout
            else:
                msg = 'argument "-" with mode %r' % self._kwargs["mode"]
                raise ValueError(msg)

        # all other arguments are used as file names
        try:
            return open(string, *self._args, **self._kwargs)
        except OSError as e:
            args = {"filename": string, "error": e}
            message = "can't open '%(filename)s': %(error)s"
            raise ArgumentTypeError(message % args)

    def __repr__(self):
        args_str = ", ".join(
            [repr(arg) for arg in self._args if arg != -1]
            + [
                "%s=%r" % (kw, arg)
                for kw, arg in self._kwargs.items()
                if arg is not None
            ]
        )
        return "%s(%s)" % (type(self).__name__, args_str)


parser = ArgumentParser(
    description="Translates comic transcripts from john.ccac.rwth-aachen.de to CSV files.",
    epilog="For such transcript in 'data', please see http://john.ccac.rwth-aachen.de:8000/ftp/dilbert/",
)
parser.add_argument(
    "data",
    type=FileTypeMine(mode="r", encoding="utf-8"),
    help="Filename for the original transcript",
)
parser.add_argument(
    "output",
    type=FileTypeMine(mode="w", encoding="utf-8", newline=""),
    help="Filename for the CSV output",
)

if __name__ == "__main__":
    args = parser.parse_args()
    convert(args.data, args.output)
