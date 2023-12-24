"""
Ce fichier comprend une série de fonctions utiles qui effectuent des opérations basiques arithmétiques et binaires
"""


def sum_mod_232(a, b):
    """
    Cette fonction effectue une somme dans un espace modulo 2 puissance 32
    :param a: premier terme
    :param b: second terme
    :return: la somme modulo 2 puissance 32
    """
    return (a + b) % (2 ** 32)


def diff_mod_232(a, b):
    """
    Cette fonction effectue une différence dans un espace modulo 2 puissance 32
    :param a: premier terme
    :param b: second terme
    :return: la différence entre me premier et le second terme modulo 2 puissance 32
    """
    return (a - b) % (2 ** 32)


def build_128_bit_bloc_from_32_bit_blocs(a, b, c, d):
    """
    Cette fonction assemble des blocs de 32bits en un seul bloc de 128 bit. Les blocs en paramètres sont ordonnées
    du plus fort au plus faible, c'est-à-dire, dans l'odre d'apparition final de gauche à droite
    :param a: 1er bloc de 32bits
    :param b: 2ème bloc de 32bits
    :param c: 3ème bloc de 32 bits
    :param d: 4ème bloc de 32bits
    :return: un bloc de 128 bits correspondant à l'ordre 'abcd'
    """
    # Utilisation des opérations de décalage et de masquage pour construire le bloc de 128 bits
    return (a << 96) | (b << 64) | (c << 32) | d


def extract_32bit_bloc_from_128(abcd):
    """
    Cette fonction décompose un bloc de 128 bits en 4 blocs de 32bits. Les blocs de sortie sont sont ordonnées
    du plus fort au plus faible, c'est-à-dire, dans l'odre d'apparition de départ de gauche à droite
    :param abcd: bloc de 128 bits
    :return: 4 blocs de 32 bits a, b, c, d tel que abcd soit le bloc de départ
    """
    # Masque pour extraire les 32 bits les plus bas
    mask = ((1 << 32) - 1)

    # Extraction des blocs de 32 bits en utilisant des opérations de masquage
    d = abcd & mask
    c = (abcd >> 32) & mask
    b = (abcd >> 64) & mask
    a = (abcd >> 96) & mask

    return a, b, c, d


def extract_32bit_bloc_from_256(abcdefgh):
    """
    Cette fonction décompose un bloc de 256 bits en 8 blocs de 32bits. Les blocs de sortie sont sont ordonnées
    du plus fort au plus faible, c'est-à-dire, dans l'odre d'apparition de départ de gauche à droite
    :param abcdefgh: bloc de 128 bits
    :return: 4 blocs de 32 bits a, b, c, d, e, f, g, h tel que abcdefgh soit le bloc de départ
    """
    # Masque pour extraire les 32 bits les plus bas
    mask = ((1 << 32) - 1)

    h = abcdefgh & mask
    g = (abcdefgh >> 32) & mask
    f = (abcdefgh >> 64) & mask
    e = (abcdefgh >> 96) & mask
    d = (abcdefgh >> 128) & mask
    c = (abcdefgh >> 160) & mask
    b = (abcdefgh >> 192) & mask
    a = (abcdefgh >> 224) & mask

    return a, b, c, d, e, f, g, h


def build_256_bit_bloc_from_32_bit_blocs(a, b, c, d, e, f, g, h):
    """
    Cette fonction assemble des blocs de 32bits en un seul bloc de 256 bit. Les blocs en paramètres sont ordonnées
    du plus fort au plus faible, c'est-à-dire, dans l'odre d'apparition final de gauche à droite
    :param a: 1er bloc de 32bits
    :param b: 2ème bloc de 32bits
    :param c: 3ème bloc de 32 bits
    :param d: 4ème bloc de 32bits
    :param e: 5ème bloc de 32bits
    :param f: 6ème bloc de 32bits
    :param g: 7ème bloc de 32 bits
    :param h: 8ème bloc de 32bits
    :return: un bloc de 128 bits correspondant à l'ordre 'abcdefgh'
    """
    return (a << 224) | (b << 192) | (c << 160) | (d << 128) | (e << 96) | (f << 64) | (g << 32) | h


def extract_8bit_blocs_from_32(abcd):
    """
    Cette fonction décompose un bloc de 32 bits en 4 blocs de 8bits. Les blocs de sortie sont sont ordonnées
    du plus fort au plus faible, c'est-à-dire, dans l'odre d'apparition de départ de gauche à droite
    :param abcd: bloc de 32 bits
    :return: 4 blocs de 8 bits a, b, c, d tel que abcd soit le bloc de départ
    """
    # Masque pour extraire les 8 bits les plus bas
    mask = ((1 << 8) - 1)

    # Extraction des blocs de 8 bits en utilisant des opérations de masquage
    d = abcd & mask
    c = (abcd >> 8) & mask
    b = (abcd >> 16) & mask
    a = (abcd >> 24) & mask

    return a, b, c, d


def shift_left(data, input_size, n_bit):
    """
    Cette fonction doit être capable de barrel-shifter vers la gauche de n_bit éléments
    l'argument data de taille input_size
    :param data: L'entier à shifter.
    :param input_size: La taille en bits de data.
    :param n_bit: nombre de bit à shifter
    :return: L'entier data shifté de n-bit vers la gauche
    """
    # Utilisation de l'opérateur modulo pour s'assurer que n_bit ne dépasse pas la plage
    n_bit = n_bit % input_size

    # Décalage du data vers la gauche de n_bits positions
    data_shift_left = data << n_bit

    # Décalage du data vers la droite de (input_size - n_bit) positions
    # Pour s'assurer que les bits qui sortent du côté droit
    # vers la gauche sont réinsérés du côté gauche
    data_shift_right = data >> (input_size - n_bit)

    # Combinaison des résultats des décalages pour prendre les bits résultants du décalage vers la gauche
    # et les bits résultants du décalage vers la droite pour former le résultat final du décalage circulaire
    shifted_data = data_shift_left | data_shift_right

    # Utilisation d'un masque pour conserver uniquement les input_size bits de poids faible
    shift_left_result = shifted_data & ((1 << input_size) - 1)

    return shift_left_result
