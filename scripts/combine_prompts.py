import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPTS_CSV = ROOT / 'prompts.csv'
VIBE_CSV = ROOT / 'vibeprompts.csv'
OUTPUT_CSV = ROOT / 'master_prompts.csv'

FIELDS = [
    'source',
    'act',
    'app',
    'prompt',
    'for_devs',
    'contributor',
    'techstack',
]

def load_csv(path: Path):
    with path.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield {k: row.get(k, '').strip() for k in reader.fieldnames}


def main():
    rows = []
    for row in load_csv(PROMPTS_CSV):
        rows.append({
            'source': 'prompts.csv',
            'act': row.get('act', ''),
            'app': '',
            'prompt': row.get('prompt', ''),
            'for_devs': row.get('for_devs', ''),
            'contributor': '',
            'techstack': '',
        })
    for row in load_csv(VIBE_CSV):
        rows.append({
            'source': 'vibeprompts.csv',
            'act': '',
            'app': row.get('app', ''),
            'prompt': row.get('prompt', ''),
            'for_devs': '',
            'contributor': row.get('contributor', ''),
            'techstack': row.get('techstack', ''),
        })

    with OUTPUT_CSV.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    print(f'Wrote {len(rows)} records to {OUTPUT_CSV}')

if __name__ == '__main__':
    main()
