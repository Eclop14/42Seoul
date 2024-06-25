import json

def read_log_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f'Error: File {filename} not found.')
    except IOError:
        print(f'Error: Unable to read file {filename}.')
    return []

def parse_log_to_list(log_lines):
    parsed_list = []
    for line in log_lines[1:]:  # Skip header
        timestamp, event, message = line.strip().split(',')
        parsed_list.append([timestamp, event, message])
    return parsed_list

def sort_list_reverse(parsed_list):
    return sorted(parsed_list, key=lambda x: x[0], reverse=True)

def list_to_dict(sorted_list):
    return [{'timestamp': item[0], 'event': item[1], 'message': item[2]} for item in sorted_list]

def save_to_json(data, filename):
    try:
        with open(filename, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=2)
        print(f'Data saved to {filename}')
    except IOError:
        print(f'Error: Unable to write to file {filename}.')

def search_in_dict(data, search_term):
    return [item for item in data if search_term.lower() in item['message'].lower()]

def main():
    log_filename = 'mission_computer_main.log'
    log_lines = read_log_file(log_filename)
    
    if log_lines:
        parsed_list = parse_log_to_list(log_lines)
        print('Parsed list:')
        print(parsed_list)
        
        sorted_list = sort_list_reverse(parsed_list)
        print('\nSorted list (reverse chronological order):')
        print(sorted_list)
        
        dict_data = list_to_dict(sorted_list)
        print('\nConverted to dictionary:')
        print(dict_data)
        
        json_filename = 'mission_computer_main.json'
        save_to_json(dict_data, json_filename)
        
        search_term = input('\nEnter a search term (Ex:Oxygen): ')
        search_results = search_in_dict(dict_data, search_term)
        if search_results:
            print(f'\nSearch results for "{search_term}":')
            for result in search_results:
                print(f"{result['timestamp']}: {result['event']} - {result['message']}")
        else:
            print(f'No results found for "{search_term}"')

if __name__ == '__main__':
    main()
