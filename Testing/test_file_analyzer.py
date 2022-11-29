from file_analyzer import FileAnalyzer
from file_analyzer import AnalyzeCommand


def test_analyze_most_frequent_ip():
    # Arrange
    file_analyzer = FileAnalyzer('input_files/access2.log')
    analyze_command = AnalyzeCommand()
    analyze_command.most_frequent_ip = True

    # Act
    result = file_analyzer.analyze(analyze_command=analyze_command)

    # Assert
    assert result == '{"file_name": "input_files/access2.log", ' \
                     '"most_frequent_ip": [{"10.105.23.145": 332}], ' \
                     '"least_frequent_ip": null, ' \
                     '"events_per_second": null, ' \
                     '"total_bytes_exchanged": null}'


