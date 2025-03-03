def remove_duplicates(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    seen = set()
    unique_lines = []
    
    for line in lines:
        if line not in seen:
            unique_lines.append(line)
            seen.add(line)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(unique_lines)

file_path = 'C:/Users/Admin/Desktop/my_private_work/Deglobeal/html_practics/DeGlobeal/task.txt'
remove_duplicates(file_path)
print("Duplicates removed.")