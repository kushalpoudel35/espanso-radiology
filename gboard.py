import csv

with open("shortcuts.csv", newline='', encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile)

    with open("dictionary.txt", "w", encoding="utf-8") as out:
        out.write("# Gboard Dictionary version:1\n")

        for row in reader:
            trigger = row[reader.fieldnames[0]].strip()
            replacement = row[reader.fieldnames[1]].strip()

            out.write(f"{trigger}\t{replacement}\ten-US\n")