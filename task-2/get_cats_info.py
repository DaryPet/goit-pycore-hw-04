def get_cats_info(path):
    try:
        cats_list =[]
        with open('task-2/cats_file.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                id, name, age = line.strip().split(',')
                # print (id, name, age)
                cat_info = {
                    "id": id,
                    "name": name,
                    "age": age
                }
                cats_list.append(cat_info)
    except FileNotFoundError:
        print ("File not found")
    except Exception as e:
        print ("There is an error")
    
    return cats_list





path = 'task-2/cats_file.txt'
# get_cats_info(path)
print (get_cats_info(path))



