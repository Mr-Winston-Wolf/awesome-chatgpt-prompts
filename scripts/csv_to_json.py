import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPTS_CSV = ROOT / 'prompts.csv'
VIBE_CSV = ROOT / 'vibeprompts.csv'
PROMPTS_JSON = ROOT / 'prompts.json'
VIBE_JSON = ROOT / 'vibeprompts.json'

def parse_bool(value: str) -> bool:
    return str(value).strip().lower() == 'true'

def prompts_to_json():
    developers = []
    general = []
    with PROMPTS_CSV.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            entry = {
                'act': row.get('act', ''),
                'prompt': row.get('prompt', ''),
            }
            if parse_bool(row.get('for_devs', '')):
                developers.append(entry)
            else:
                general.append(entry)
    data = {'developer': developers, 'general': general}
    with PROMPTS_JSON.open('w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def vibeprompts_to_json():
    vibes = []
    with VIBE_CSV.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            vibes.append({
                'app': row.get('app', ''),
                'prompt': row.get('prompt', ''),
                'contributor': row.get('contributor', ''),
                'techstack': row.get('techstack', ''),
            })
    with VIBE_JSON.open('w', encoding='utf-8') as f:
        json.dump(vibes, f, ensure_ascii=False, indent=2)

def main():
    prompts_to_json()
    vibeprompts_to_json()
    print(f'Wrote {PROMPTS_JSON} and {VIBE_JSON}')

if __name__ == '__main__':
    main()
