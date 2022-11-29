import argparse
from file_analyzer import *

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('input_path')
    parser.add_argument('output_path')
    parser.add_argument('--mfip', help='Most frequent IP', action='store_true')
    parser.add_argument('--lfip', help='Least frequent IP', action='store_true')
    parser.add_argument('--eps', help='Events per second', action='store_true')
    parser.add_argument('--bytes', help='Total amount of bytes exchanged', action='store_true')
    args = parser.parse_args()

    print('Arguments: ', args)

    analyze_command = AnalyzeCommand()
    analyze_command.most_frequent_ip = args.mfip
    analyze_command.least_frequent_ip = args.lfip
    analyze_command.events_per_second = args.eps
    analyze_command.total_bytes_exchanged = args.bytes

    path_analyzer = PathAnalyser(input_path=args.input_path, output_path=args.output_path, command=analyze_command)
    path_analyzer.analyze_path()



