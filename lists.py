# Escribir un método llamado remove_elements que dado una lista
# retorne una lista después de haber removido el primer, el quinto y el sexto elemento.
# Tener en cuenta que la lista puede ser de menor o mayor tamaño que los elementos que se piden borrar
# y que del ejemplo, por lo que debe seguir funcionando sin importar el tamaño de la lista.
# Sample Input : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements) > 7:
        return list_to_remove_elements[1:4] + list_to_remove_elements[7:]
    elif len(list_to_remove_elements) > 5:
        return list_to_remove_elements[1:4]
    elif len(list_to_remove_elements) > 1:
        return list_to_remove_elements[1:]
    else:
        return []

# print(remove_elements(['1-Red', '2-Green', '3-White', '4-Black', '5-Pink', '6-Yellow']))

# Escribir un método llamado add_elements que dado una lista retorne una lista después de haber agregado el elemento ‘Pink’ al principio de la lista y el elemento ‘Yellow’ al final de la lista.
#
# Sample Input : ['Red', 'Green', 'White', 'Black']
# Expected Output : ['Pink', 'Red', 'Green', 'White', 'Black', 'Yellow']
def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0, 'Pink')
    list_to_add_elements.append('Yellow')
    return list_to_add_elements


# Escribir un método llamado is_empty que diga si una lista está vacía o no.
def is_empty(list_to_check):
    return len(list_to_check) == 0


# Escribir un método llamado check_lists que dado dos listas retorne True si ambas listas contienen el mismo 3er elemento. Tener en cuenta que la lista puede ser de menor o mayor tamaño que los elementos que se piden comparar, por lo que debe seguir funcionando sin importar el tamaño de la lista. Si una lista contiene un valor en el 3er elemento y la otra lista no, se considera que no tienen el mismo elemento y la respuesta debe ser False
#
# Sample List1 : ['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White']
# Sample List2 : ['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink']
# Expected Output : True
#
# Sample List1 : ['Black', 'Pink', 'Green', 'White']
# Sample List2 : ['Red', 'Green', 'Yellow', 'Black', 'Pink']
# Expected Output : False

def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) < 3 or len(list_to_compare2) < 3:
        return False
    return list_to_compare1[2] == list_to_compare2[2]


# Escribir un método llamado list_of_lists que dado una lista de listas, la modifique en la siguiente manera y la retorne:
#
# De la primera lista solo se quede con los primeros 2 elementos. De la segunda lista solo se quede con los elementos entre el segundo y cuarto elemento. De la tercera lista solo se quede con los últimos 2 elementos.
#
# Tener en cuenta que el tamaño de la lista externa tiene 3 elementos fijos, pero cada uno de esos 3 elementos (que son las listas internas) pueden variar sus tamaños.
#
# Sample List: [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]
# Sample Output: [[1, 2], [5, 6, 7], [11, 12]]
def list_of_lists(list_of_lists_to_modify):
    if len(list_of_lists_to_modify) != 3:
        return list_of_lists_to_modify

    # Modificar la primera lista
    if len(list_of_lists_to_modify[0]) > 2:
        list_of_lists_to_modify[0] = list_of_lists_to_modify[0][:2]

    # Modificar la segunda lista
    if len(list_of_lists_to_modify[1]) > 4:
        list_of_lists_to_modify[1] = list_of_lists_to_modify[1][1:4]
    elif len(list_of_lists_to_modify[1]) > 1:
        list_of_lists_to_modify[1] = list_of_lists_to_modify[1][1:]
    else:
        list_of_lists_to_modify[1] = []

    # Modificar la tercera lista
    if len(list_of_lists_to_modify[2]) > 2:
        list_of_lists_to_modify[2] = list_of_lists_to_modify[2][-2:]

    return list_of_lists_to_modify
