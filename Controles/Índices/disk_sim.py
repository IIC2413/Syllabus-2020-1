def create_page(pname, size=5):
    '''
    Crea una página nueva de nombre pname y con size bloques disponibles.
    '''
    page = open(pname, 'w', encoding='utf-8')
    for _ in range(size):
        page.write('<EMPTY>\n')
    page.write('<NEXT> <NULL>')
    page.close()

def has_empty(pname):
    '''
    Recibe como parámetro el nombre de una página.
    Retorna la posición de un bloque vacío para guardar una tupla y si no hay espacio retorna -1.
    '''
    page = open(pname, 'r', encoding='utf-8')
    lines = page.readlines()
    page.close()
    
    lines = map(lambda x: x.strip(), lines)
    
    count = 0
    for line in lines:
        if line == '<EMPTY>':
            return count
        count += 1
    return -1

def insert_into_pos(pname, pos, value):
    '''
    Inserta en la página pname, en el casillero pos el string con valor value.
    Si se ingresa una posición no válida la función no hace nada
    '''
    page = open(pname, 'r', encoding='utf-8')
    lines = page.readlines()
    page.close()
    
    if pos >= len(lines) - 1:
        print('Posición no válida')
        return
    
    if '<EMPTY>' not in lines[pos]:
        print('Posición no vacía')
        return
    
    lines[pos] = f'{value}\n'
    
    page = open(pname, 'w', encoding='utf-8')  
    for line in lines:
        page.write(line)   
    page.close()
    
def delete_from_pos(pname, pos):
    '''
    Setea el valor <EMPTY> en la posición indicada.
    '''
    page = open(pname, 'r', encoding='utf-8')
    lines = page.readlines()
    page.close()
    
    if pos >= len(lines) - 1:
        print('Posición no válida')
        return
    
    if '<EMPTY>' in lines[pos]:
        print('Posición ya vacía')
        return
    
    lines[pos] = '<EMPTY>\n'
    
    page = open(pname, 'w', encoding='utf-8')  
    for line in lines:
        page.write(line)   
    page.close()
    
def tuple_to_hexa_string(row):
    '''
    Convierte una tupla row de la forma (int, string) en un string hexadecimal.
    El texto solo puede tener espacios y caracteres alfabéticos.
    '''
    
    tuple_string = ''
    for element in row:
        tuple_string += str(element) + ','
    
    
    hexa_string = ''
    for c in tuple_string[:-1]:
        hexa_string += str(hex(ord(c))) + ' '
        
    return hexa_string.strip()
    
def read_hexa_tuple(pname, pos):
    '''
    Trae el valor de de la tupla en el casillero pos de la página pname.
    '''
    page = open(pname, 'r', encoding='utf-8')
    lines = page.readlines()
    page.close()
    
    if pos >= len(lines) - 1:
        print('Posición no válida')
        return
    
    hexa_string = lines[pos].strip()
    elements = hexa_string.split()
    
    row_string = ''
    for element in elements:
        row_string += chr(int(element, 16))
        
    return tuple(row_string.split(','))

def get_element_from_page(pname, pos):
    page = open(pname, 'r', encoding='utf-8')
    lines = page.readlines()
    page.close()
    
    lines = list(map(lambda x: x.strip(), lines))
    
    if pos > len(lines) - 1:
        print('Posición no valida')
        return
    
    if lines[pos] == '<EMPTY>':
        return None
    
    return read_hexa_tuple(pname, pos)
    

def read_next_page(pname):
    '''
    Trae el nombre de la página siguiente a pname si existe.
    '''
    page = open(pname, 'r', encoding='utf-8')
    lines = page.readlines()
    page.close()
    
    next_page = (lines[len(lines) - 1]).strip()
    
    next_page = next_page.split()[1]
    
    if next_page == '<NULL>':
        return None
        
    return next_page

def set_next_page(pname, next_pname):
    '''
    Define el nombre de la página siguiente a pname.
    '''
    page = open(pname, 'r', encoding='utf-8')
    lines = page.readlines()
    page.close()
    
    lines[len(lines) - 1] = f'<NEXT> {next_pname}'
    
    page = open(pname, 'w', encoding='utf-8')  
    for line in lines:
        page.write(line)   
    page.close()