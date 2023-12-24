import secrets

from cast256 import encrypt_block, decrypt_block


def rdm_iv_generator():
    """
    Cette fonction doit pouvoir générer un nombre aléatoire de 128bits
    :return: un entier représenté sur 128 bits généré de manière aléatoire.
    """
    return secrets.randbits(128)


def encrypt_ecb(blocks, key):
    """
    Cette fonction applique le chiffrement CAST256 à une liste de blocs de 128 bits suivant le mode d'opération ECB.
    :param blocks: Liste de blocs (128bits) à chiffrer.
    :param key: clé de chiffrement 256 bits
    :return: la liste de blocs chiffrés.
    """
    encrypted_blocks = []

    for block in blocks:
        encrypted_block = encrypt_block(block, key)
        encrypted_blocks.append(encrypted_block)
    return encrypted_blocks


def decrypt_ecb(blocks, key):
    """
    Cette fonction dé-chiffre une liste de blocs de 128 bits qui a été préalablement chiffrée
    avec la méthode CAST256 suivant le mode d'opération ECB.
    :param blocks: Liste de blocs à déchiffrer.
    :param key: clé de chiffrement 256 bits
    Identique à celle utilisée pour le chiffrement.
    :return: la liste de blocs déchiffrés.
    """
    decrypted = []
    for block in blocks:
        decrypte = decrypt_block(block, key)
        decrypted.append(decrypte)
    return decrypted


def encrypt_cbc(blocks, key):
    """
    Cette fonction applique le chiffrement CAST256 à une liste de blocs de 128 bits suivant le mode d'opération CBC.
    :param blocks: Liste de blocs à chiffrer.
    :param key: clé de chiffrement 256 bits
    :return: la liste de blocs chiffrés avec le vecteur initial utilisé en première position.
    """
    # Génération d'un vecteur d'initialisation aléatoire de 128 bits
    iv = rdm_iv_generator()

    # Liste pour stocker les blocs chiffrés
    encrypted_blocks = [iv]

    # Chiffrement de chaque bloc en utilisant le bloc précédent
    previous_block = iv
    for block in blocks:
        # XOR avec le bloc précédent (ou le vecteur d'initialisation pour le premier bloc)
        block_to_encrypt = block ^ previous_block
        # Chiffrement du bloc
        encrypted_block = encrypt_block(block_to_encrypt, key)

        # Stockage du bloc chiffré pour l'utilisation ultérieure
        encrypted_blocks.append(encrypted_block)

        # Mise à jour du bloc précédent pour le prochain tour de boucle
        previous_block = encrypted_block

    return encrypted_blocks


def decrypt_cbc(blocks, key):
    """
    Cette fonction dé-chiffre une liste de blocs de 128 bits qui a été préalablement chiffrée
    avec la méthode CAST256 suivant le mode d'opération CBC.
    :param blocks: Liste de blocs à déchiffrer.
    :param key: clé de chiffrement 256 bits
    Identique à celle utilisée pour le chiffrement.
    :return: la liste de blocs déchiffrés.
    """
    # Initialisation du vecteur d'initialisation
    iv = blocks[0]

    # Liste pour stocker les blocs déchiffrés
    decrypted_blocks = []

    # Déchiffrement de chaque bloc en utilisant le mode CBC
    for block in blocks[1:]:
        # Déchiffrement du bloc
        decrypted_block = decrypt_block(block, key)

        # XOR du bloc déchiffré avec le bloc précédent chiffré (ou le vecteur d'initialisation pour le premier bloc)
        xor_result = decrypted_block ^ iv

        # Ajout du bloc résultant à la liste
        decrypted_blocks.append(xor_result)

        # Met à jour le vecteur d'initialisation pour le prochain bloc
        iv = block
    return decrypted_blocks


def decrypt(blocks, key, operation_mode="ECB"):
    """
    Cette fonction dé-chiffre une liste de blocs de 128 bits qui a été préalablement chiffrée
    avec la méthode CAST256 suivant le mode d'opération CBC ou ECB.
    :param blocks: Liste de blocs à déchiffrer.
    :param key: la clé de chiffrement 256 bit
    :param operation_mode: string spécifiant le mode d'opération ("ECB" ou "CBC")
    :return: la liste de blocs déchiffrés.
    """
    if operation_mode.upper() == "ECB".upper():
        return decrypt_ecb(blocks, key)
    elif operation_mode.upper() == "CBC".upper():
        return decrypt_cbc(blocks, key)
    else:
        raise ValueError("Mode d'opération non pris en charge. Utilisez 'ECB' ou 'CBC'.")


def encrypt(blocks, key, operation_mode="ECB"):
    """
    Cette fonction applique le chiffrement CAST256 à une liste de blocs de 128 bits.
    :param blocks: Liste de blocs à chiffrer.
    :param key: la clé de chiffrement 256 bit
    :param operation_mode: string spécifiant le mode d'opération ("ECB" ou "CBC")
    :return: la liste de blocs chiffrés avec le vecteur initial utilisé en première position.
    """
    if operation_mode.upper() == "ECB".upper():
        return encrypt_ecb(blocks, key)
    elif operation_mode.upper() == "CBC".upper():
        return encrypt_cbc(blocks, key)
    else:
        raise ValueError("Mode d'opération non pris en charge. Utilisez 'ECB' ou 'CBC'.")
