def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        total = 0
        count = 0
        
        for line in lines:
            _, salary = line.strip().split(',')
            total += int(salary)
            count += 1
        
        average = total / count if count > 0 else 0
        return total, average
    
    except FileNotFoundError:
        print(f"Cannot find file by path - {path}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")