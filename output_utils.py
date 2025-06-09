import csv
import json
import logging

def save_to_csv(data, filename="quotes.csv"):
    if not data:
        logging.warning("No data to write to CSV.")
        return

    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["text", "author", "tags"])
        writer.writeheader()
        for row in data:
            row['tags'] = ", ".join(row['tags'])  # convert list to string
            writer.writerow(row)

    logging.info(f"Saved {len(data)} quotes to {filename}")

def save_to_json(data, filename="quotes.json"):
    if not data:
        logging.warning("No data to write to JSON.")
        return

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    logging.info(f"Saved {len(data)} quotes to {filename}")
