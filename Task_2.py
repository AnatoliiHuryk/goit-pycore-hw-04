def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        cats_info = []
        
        for line in lines:
            cat_id, name, age = line.strip().split(',')
            cats_info.append({"id": cat_id, "name": name, "age": age})
        
        return cats_info
    
    except FileNotFoundError:
        return f"Cannot find file by path - {path}"
    except Exception as e:
        return f"Error: {e}"

cats_info = get_cats_info("cats_file.txt")
print(cats_info)