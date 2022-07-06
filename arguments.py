import argparse


def parseList(string):
    return string.split(",")


def getArguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("--source",
                        default="./allNYWords.txt",
                        type=str,
                        required=False,
                        help="Path to file with all data.")
    parser.add_argument("--train",
                        default="./trainWords.txt",
                        type=str,
                        required=False,
                        help="Path to file with train data.")
    parser.add_argument("--test",
                        default="./testWords.txt",
                        type=str,
                        required=False,
                        help="Path to file with test stats.")

    args = parser.parse_args()
    return args
