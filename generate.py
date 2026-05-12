import csv

with open("shortcuts.csv", newline='', encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile)

    print(reader.fieldnames)  # shows detected column names

    with open("base.yml", "w", encoding="utf-8") as out:
        out.write("matches:\n")

        for row in reader:
            trigger = row[reader.fieldnames[0]].strip()
            replacement = row[reader.fieldnames[1]].strip().replace('"', '\\"')

            out.write(f'  - trigger: "{trigger}"\n')
            out.write(f'    replace: "{replacement}"\n')
            out.write('    word: true\n')
            out.write('    propagate_case: true\n\n')