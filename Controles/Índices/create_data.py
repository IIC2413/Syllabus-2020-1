from disk_sim import *
import random

def create():
    table_t = [
        (1, "La anunciación"),
        (2, "La mona lisa"),
        (3, "La primavera"),
        (4, "El nacimiento de Venus"),
        (5, "La consagración de Napoleón"),
        (6, "El David"),
        (7, "La piedad"),
        (8, "La fuente de los 4 ríos"),
        (9, "La última cena"),
        (10, "El juicio final"),
        (11, "El Moisés"),
    ]

    random.shuffle(table_t)

    create_page('o-1')
    insert_into_pos('o-1', 0, tuple_to_hexa_string(table_t[0]))
    insert_into_pos('o-1', 1, tuple_to_hexa_string(table_t[1]))
    insert_into_pos('o-1', 3, tuple_to_hexa_string(table_t[2]))
    insert_into_pos('o-1', 4, tuple_to_hexa_string(table_t[3]))
    set_next_page('o-1', 'o-2')
    create_page('o-2')
    insert_into_pos('o-2', 0, tuple_to_hexa_string(table_t[4]))
    insert_into_pos('o-2', 1, tuple_to_hexa_string(table_t[5]))
    insert_into_pos('o-2', 4, tuple_to_hexa_string(table_t[6]))
    set_next_page('o-2', 'o-3')
    create_page('o-3')
    insert_into_pos('o-3', 0, tuple_to_hexa_string(table_t[7]))
    insert_into_pos('o-3', 1, tuple_to_hexa_string(table_t[8]))
    insert_into_pos('o-3', 2, tuple_to_hexa_string(table_t[9]))
    insert_into_pos('o-3', 3, tuple_to_hexa_string(table_t[10]))

