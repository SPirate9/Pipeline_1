import json
import os
from datetime import datetime

def load_sample(path):
    with open(path, 'r') as file:
        for line in file:
            if line.strip():
                yield line.strip()

def generate_json(transactions):
    total_sent = sum(int(line.split()[2].replace('€', '')) for line in transactions)
    name = transactions[0].split()[0] 
    return {"name": name, "total_sent": total_sent}

def save_result(path, result, filename):
    base_name = os.path.splitext(filename)[0]
    timestamp = datetime.now().strftime('%Y-%m-%d')
    output_filename = f"result_{base_name}_{timestamp}.json"
    with open(os.path.join(path, output_filename), 'w') as file:
        json.dump(result, file, indent=4)

def process_files(source, result, archived):
    for filename in os.listdir(source):
        if filename.endswith('.txt'):
            transactions = list(load_sample(os.path.join(source, filename)))
            result_data = generate_json(transactions)
            save_result(result, result_data, filename)
            os.rename(os.path.join(source, filename), os.path.join(archived, filename))

if __name__ == "__main__":
    process_files('source', 'result', 'archived')