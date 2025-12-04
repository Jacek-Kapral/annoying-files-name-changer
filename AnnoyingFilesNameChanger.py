import os
import re

folder = "."

pattern_paren = re.compile(r"\((\d+)\)")


pattern_number = re.compile(r'(?<!\d)(\d{1,3})(?!\d)')

changes = []

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    if not os.path.isfile(filepath):
        continue

    new_name = filename

    match_paren = pattern_paren.search(new_name)
    if match_paren:
        num = int(match_paren.group(1))
        new_num = f"({num:03d})"
        new_name = pattern_paren.sub(new_num, new_name)

    name_only, ext = os.path.splitext(new_name)

    def repl(m):
        num = int(m.group(1))
        return f"{num:03d}"

    name_only_new = pattern_number.sub(repl, name_only)

    new_name = name_only_new + ext

    if new_name != filename:
        new_path = os.path.join(folder, new_name)
        changes.append((filepath, new_path))


if not changes:
    print("Nie znaleziono plików do zmiany.")
    exit()

print("\nProponowane zmiany:\n")
for old, new in changes:
    print(f"{os.path.basename(old)}  ->  {os.path.basename(new)}")

response = input("\nZaakceptować zmiany? (y/n): ").strip().lower()

if response == "y":
    for old, new in changes:
        if not os.path.exists(new):
            os.rename(old, new)
            print(f"Zmieniono: {os.path.basename(old)} -> {os.path.basename(new)}")
        else:
            print(f"⚠️ Pominięto (już istnieje): {os.path.basename(new)}")
    print("\n✅ Gotowe.")
else:
    print("\n❎ Anulowano – nie dokonano żadnych zmian.")
