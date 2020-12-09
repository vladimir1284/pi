# -*-  encoding:utf8 -*-
import sys
import argparse

from acction_interface import load_config_file, TMatcher


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", default="resources.xml", help="Config XML file path")

    argument = parser.parse_args(sys.argv[1:])
    matcher = TMatcher(load_config_file(argument.input))
    input_string = input("Action [empty for exit]: ")
    while input_string:
        target = matcher.process(input_string)
        if target:
            print(target)
        else:
            print("   ERROR: Unknown command.")
        input_string = input("Action [empty for exit]: ")
    print("Bye!!")
