from functions_cast256 import function1, function2, function3
from utils import extract_32bit_bloc_from_256, sum_mod_232, build_256_bit_bloc_from_32_bit_blocs


def forward_octave(abcdefgh, tr, tm):
    """
      Cette fonction correspond à la forward_octave du cast-256. Elle décompose le bloc d'entrée 256bits en
      blocs de 32bits. Ces blocs sont transformés par l'utilisation des fonctions f1, f2 et f3 du cast-256 en utilisant
      les clés de rotation et de masque. Les blocs obtenus sont recomposés en un bloc de 256bits.
      !!! ATTENTION A L'ORDRE DES OPERATIONS INDIQUE DANS LA DOCUMENTATION !!!
      :param abcdefgh: le bloc à traité (256bits)
      :param tr: tableau de 8 clés de rotation (8bits)
      :param tm: tableau de 8 clés de masque (32bits)
      :return: le résultat des opérations (256bits)
      """
    # Décomposition du bloc 256 en bloc de 32 bits KAPPA <- Wi(KAPPA)
    a, b, c, d, e, f, g, h = extract_32bit_bloc_from_256(abcdefgh)

    G = g ^ function1(h, tr[0], tm[0])
    F = f ^ function2(G, tr[1], tm[1])
    E = e ^ function3(F, tr[2], tm[2])
    D = d ^ function1(E, tr[3], tm[3])
    C = c ^ function2(D, tr[4], tm[4])
    B = b ^ function3(C, tr[5], tm[5])
    A = a ^ function1(B, tr[6], tm[6])
    H = h ^ function2(A, tr[7], tm[7])

    return build_256_bit_bloc_from_32_bit_blocs(A, B, C, D, E, F, G, H)


def initialization():
    """
    Cette fonction crée les clés de rotation tr et de masque tm utiles à la génération des clés du cast-256.
    :return: deux tableaux à deux dimensions 8x24 (24 lignes et 8 colonnes) contenant respectivement
    les clés de rotation tr et de masque tm.
    """
    Cm = 0x5A827999
    Mm = 0x6ED9EBA1
    Cr = 19
    Mr = 17

    # Initialisation des tableaux pour les clés de rotation et de masque
    tr = [[0 for _ in range(8)] for _ in range(24)]
    tm = [[0 for _ in range(8)] for _ in range(24)]

    for i in range(24):
        for j in range(8):
            tm[i][j] = Cm
            Cm = sum_mod_232(Cm, Mm)
            tr[i][j] = Cr
            Cr = sum_mod_232(Cr, Mr)

    return tr, tm


def key_generator(key):
    """
    Cette fonction génère les clés de rotation kr et de masque km pour le chiffrement cast-256 à partir de la clé 256bits
    de chiffrement et des clés de rotation tr et de masque tm.
    :param key: la clé de chiffrement (256bits)
    :return: deux tableaux à deux dimensions 12x4 (12 lignes et 4 colonnes) contenant respectivement
    les clés de rotation kr et de masque km.
    """
    # Appele à la fonction initialise pour récupérer les listes tr et tm
    tr, tm = initialization()

    kr = [[0] * 4 for _ in range(12)]
    km = [[0] * 4 for _ in range(12)]
    for i in range(12):
        premier_forward = forward_octave(key, tr[i * 2], tm[i * 2])
        deuxieme_forward = forward_octave(premier_forward, tr[i * 2 + 1], tm[i * 2 + 1])

        key = deuxieme_forward
        a, b, c, d, e, f, g, h = extract_32bit_bloc_from_256(key)

        kr[i][0] = a & 0b11111
        kr[i][1] = c & 0b11111
        kr[i][2] = e & 0b11111
        kr[i][3] = g & 0b11111

        km[i][0] = h
        km[i][1] = f
        km[i][2] = d
        km[i][3] = b
    return kr, km
