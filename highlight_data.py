
def insert_1(surname):
    with open('data_1.csv', 'r') as f:
        data_insert = f.readlines()
        surname = surname + '\n'
        if surname in data_insert:
            index = data_insert.index(surname)
            return index
        else:
            return "Такой фамилии в справочнике нет."

def insert_2(surname):
    with open('data_2.csv', 'r') as f:
        data_insert = f.readlines()
        insert_index = 0
        for i in range(len(data_insert)):
            if surname in data_insert[i].split(';'):
                insert_index = i
    if insert_index != 0:
        return insert_index
    else:
        return "Такой фамилии в справочнике нет."
