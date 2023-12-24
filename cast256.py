from key_generator import key_generator
from functions_cast256 import forward_quad_round, reverse_quad_round


def encrypt_block(message, key):
    """
    Cette fonction effectue le chiffrement d'un bloc de 128bits en exécutant les rounds successifs du cast-256
    :param message: le bloc à chiffrer (128bits)
    :param key: la clé de chiffrement (256bits)
    :return: le cryptogramme (128bits)
    """
    # Génération des sous-clés de chiffrement
    kr, km = key_generator(key)

    # Exécution des 6 premiers rounds (forward_quad_round)
    for i in range(6):
        message = forward_quad_round(message, kr[i], km[i])

    # Exécution des 6 derniers rounds en sens inverse (reverse_quad_round)
    for i in range(6, 12):
        message = reverse_quad_round(message, kr[i], km[i])
    return message


def decrypt_block(cipher, key):
    """
    Cette fonction effectue le déchiffrement d'un bloc de 128bits en exécutant les rounds successifs du cast-256
    :param cipher: le bloc à déchiffrer (128bits)
    :param key: la clé de chiffrement (256bits)
    :return: le message (128bits)
    """
    # Génération des sous-clés de chiffrement
    kr, km = key_generator(key)

    # Exécution des 6 premiers rounds en sens inverse (forward_quad_round)
    for i in range(11, 5, -1):
        cipher = forward_quad_round(cipher, kr[i], km[i])

    # Exécution des 6 derniers rounds (reverse_quad_round)
    for i in range(5, -1, -1):
        cipher = reverse_quad_round(cipher, kr[i], km[i])
    return cipher

