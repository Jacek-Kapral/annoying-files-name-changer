import os
import re

# folder do przeszukania
folder = "."

# rozpoznanie wzorca w nazwach plików
pattern = re.compile(r"\((\d+)\)")

changes = []

# iteracja po plikach w folderze
for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    if not os.path.isfile(filepath):
        continue  # pominięcie folderów

    match = pattern.search(filename)
    if match:
        num = int(match.group(1))
        new_num = f"({num:03d})"  # format 3-cyfrowy, może w następnej wersji dodam obsługę większych liczb w nazwach plików
        new_name = pattern.sub(new_num, filename)
        if new_name != filename:
            new_path = os.path.join(folder, new_name)
            changes.append((filepath, new_path))

if not changes:
    print("Nie znaleziono plików do zmiany.")
    exit()

print("\nProponowane zmiany:\n")
for old, new in changes:
    print(f"{os.path.basename(old)}  ->  {os.path.basename(new)}")

# zapytanie o potwierdzenie
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