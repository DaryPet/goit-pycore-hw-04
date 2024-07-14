def total_salary(path):
    try:
        with open (path, 'r', encoding='utf-8') as file:
            lines= file.readlines()
            
        total = 0
        count = 0

        for line in lines:
            name, salary = line.strip().split(',')
            total += int(salary)
            count += 1
        
        average = int(total / count)
        return total, average
    
    except FileNotFoundError:
        print ('File not found')
    except Exception as e:
        print("There is an error")


path = "task-1/salaries.txt"

total, average = total_salary(path)

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
