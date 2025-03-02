def find_duplicates(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    seen = set()
    duplicates = set()
    
    for line in lines:
        line = line.strip()
        if line in seen:
            duplicates.add(line)
        else:
            seen.add(line)
    
    return duplicates

file_path = 'C:/Users/Admin/Desktop/my_private_work/Deglobeal/html_practics/DeGlobeal/readme.txt'
duplicates = find_duplicates(file_path)

if duplicates:
    print("Duplicate lines found:")
    for duplicate in duplicates:
        print(duplicate)
else:
    print("No duplicate lines found.")