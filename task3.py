import json
import sys

def fill_values(tests_data, values_dict):
    if isinstance(tests_data, list):
        for item in tests_data:
            fill_values(item, values_dict)
    elif isinstance(tests_data, dict):
        if 'id' in tests_data and tests_data['id'] in values_dict:
            tests_data['value'] = values_dict[tests_data['id']]
        if 'values' in tests_data:
            fill_values(tests_data['values'], values_dict)

def generate_report(values_path, tests_path, report_path):
    try:
        # Чтение файлов
        with open(values_path, 'r') as f:
            values_data = json.load(f)
        
        with open(tests_path, 'r') as f:
            tests_data = json.load(f)
        
        # Создание словаря значений
        values_dict = {item['id']: item['value'] for item in values_data['values']}
        
        # Заполнение значений
        fill_values(tests_data, values_dict)
        
        # Сохранение отчета
        with open(report_path, 'w') as f:
            json.dump(tests_data, f, indent=2)
        
        print(f"Report successfully generated at {report_path}")
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python report_generator.py <values.json> <tests.json> <report.json>")
        sys.exit(1)
    
    generate_report(sys.argv[1], sys.argv[2], sys.argv[3])
