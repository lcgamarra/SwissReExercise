import os
import json
from helper import *


class AnalyzeCommand:
    # Command class so we don´t need to use several input parameters
    def __init__(self):
        self.most_frequent_ip = False
        self.least_frequent_ip = False
        self.events_per_second = False
        self.total_bytes_exchanged = False


class AnalyzeResultSet:
    # Result set class to execute to an easy json dump execute
    def __init__(self):
        self.file_name = None
        self.most_frequent_ip = None
        self.least_frequent_ip = None
        self.events_per_second = None
        self.total_bytes_exchanged = None


class FileAnalyzer:
    # FinaAnalyzer class that will execute the one time analysis of the file
    def __init__(self, file_path):
        self.path = file_path
        self.filename = os.path.basename(self.path)
        self.analyze_result_set = AnalyzeResultSet()
        self.ip_dictionary = {}

    def analyze(self, analyze_command: AnalyzeCommand):
        # Main method to analyze one file
        print('File size: %f MB' % (os.stat(self.path).st_size / (1024 * 1024)))
        self.analyze_result_set.file_name = self.path

        event_counter = 0
        first_event_timespan = 0.0
        last_event_timespan = 0.0
        total_bytes_exchanged = 0.0

        with open(self.path) as log_file:
            for line in log_file:
                line_array = line.split()
                if len(line_array) > 0:
                    # print(line_array)
                    first_ip = line_array[2]
                    if validate_ip_address_string(first_ip):
                        self.ip_dictionary.setdefault(first_ip, 0)
                        self.ip_dictionary[line_array[2]] += 1

                        event_time_span = float(line_array[0])
                        first_event_timespan = event_time_span if event_counter == 0 else event_time_span if event_time_span < first_event_timespan else first_event_timespan
                        last_event_timespan = event_time_span if event_counter == 0 else event_time_span if event_time_span > last_event_timespan else last_event_timespan
                        event_counter += 1

                        header_bytes = int(line_array[1])
                        response_bytes = int(line_array[4])
                        total_bytes_exchanged += (header_bytes + response_bytes)

                    second_ip = line_array[8].split('/')[1]
                    if validate_ip_address_string(second_ip):
                        self.ip_dictionary.setdefault(second_ip, 0)
                        self.ip_dictionary[second_ip] += 1

                    # count += 1
                    # if count >= 100:
                    #     break

        maximum_frequency = self.ip_dictionary[max(self.ip_dictionary, key=self.ip_dictionary.get)]
        self.analyze_result_set.most_frequent_ip = [{ip: freq} for ip, freq in self.ip_dictionary.items() if freq == maximum_frequency]
        minimum_frequency = self.ip_dictionary[min(self.ip_dictionary, key=self.ip_dictionary.get)]
        self.analyze_result_set.least_frequent_ip = [{ip: freq} for ip, freq in self.ip_dictionary.items() if freq == minimum_frequency]

        # print("first: ", first_event_timespan)
        # print("last: ", last_event_timespan)

        self.analyze_result_set.events_per_second = (last_event_timespan - first_event_timespan) / event_counter

        self.analyze_result_set.total_bytes_exchanged = total_bytes_exchanged

        self.analyze_result_set.most_frequent_ip = self.analyze_result_set.most_frequent_ip if analyze_command.most_frequent_ip else None
        self.analyze_result_set.least_frequent_ip = self.analyze_result_set.least_frequent_ip if analyze_command.least_frequent_ip else None
        self.analyze_result_set.events_per_second = self.analyze_result_set.events_per_second if analyze_command.events_per_second else None
        self.analyze_result_set.total_bytes_exchanged = self.analyze_result_set.total_bytes_exchanged if analyze_command.total_bytes_exchanged else None

        # print(self.ip_dictionary)

        return json.dumps(self.analyze_result_set.__dict__)


class PathAnalyser:
    # General class that will cover the analysis of a folder or a file path
    def __init__(self, input_path: str, output_path: str, command: AnalyzeCommand):
        self.input_path = input_path
        self.output_path = output_path
        self.command = command

        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

    def analyze_path(self):
        if os.path.isfile(self.input_path):
            file_analyzer = FileAnalyzer(self.input_path)
            result = file_analyzer.analyze(self.command)
            print("Result: ", result)

            with open(self.output_path + '/' + file_analyzer.filename.split('.')[0] + '_result.txt', 'w') as outfile:
                outfile.write(result)

        elif os.path.isdir(self.input_path):
            for filename in os.listdir(self.input_path):
                file_analyzer = FileAnalyzer(file_path=self.input_path + '/' + filename)
                result = file_analyzer.analyze(self.command)
                print("Result: ", result)

                with open(self.output_path + '/' + file_analyzer.filename.split('.')[0] + '_result.txt', 'w') as outfile:
                    outfile.write(result)

        else:
            # TODO The case where there is an empty directory as the input_path argument
            raise NotImplementedError
