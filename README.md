# chiffrement-cast-256
Le chiffrement CAST-256, également connu sous le nom de CAST6, appartient à la famille des algorithmes de chiffrement de blocs.

Cast-256 fonctionne avec des blocs de 128 bits et des clés de 128, 160, 192, 224, ou 256 bits, offrant ainsi une flexibilité en termes de longueur de clé.

CAST-256 utilise une structure en réseau de Feistel, qui divise la clé en sous-clés pour chaque tour d'opération. Il effectue un certain nombre de tours (rounds) pour mélanger les données de manière sécurisée 

# Explication de fichier

1. Cast256.py : Le fichier cast256.py contient des fonctions de chiffrement et dechiffrement 
   - encrypt_block(message, key) : Cette fonction effectue le chiffrement d'un bloc de 128 bits en exécutant les rounds successifs de l'algorithme CAST-256.
     Les sous-clés de chiffrement sont générées à l'aide de la fonction key_generator du module key_generator.
     Les 12 rounds de chiffrement sont exécutés en alternant entre les fonctions forward_quad_round et reverse_quad_round
     - decrypt_block(cipher, key) : Cette fonction effectue le déchiffrement d'un bloc de 128 bits en exécutant les rounds successifs de l'algorithme CAST-256 dans l'ordre inverse.
       Les sous-clés de chiffrement sont générées de la même manière qu'avec la fonction de chiffrement.
       Les 12 rounds de déchiffrement sont exécutés en alternant entre les fonctions forward_quad_round et reverse_quad_round.
       
2. function_cast256.py : Le fichier function_cast256.py contient des opérations spécifiques à chaque round (forward et reverse) de l'algorithme CAST-256
   - table_substitution(bloc) : Cette fonction effectue une opération de substitution sur un bloc de données, introduisant ainsi de la confusion
   - function1(d, kri, kmi) : Cette fonction correspond à la fonction 1 du CAST-256. Elle effectue des opérations de somme modulo, décalage à gauche, substitution (S-BOX), et XOR dans un ordre spécifique.
   - function2(d, kri, kmi) : Cette fonction correspond à la fonction 2 du CAST-256. Elle effectue des opérations similaires à function1, mais dans un ordre différent.
   - function3(d, kri, kmi) : Cette fonction correspond à la fonction 3 du CAST-256. Elle effectue des opérations similaires à function1 et function2, mais dans un ordre différent.
   - forward_quad_round(abcd, kr, km) : Cette fonction correspond à la phase de chiffrement (forward_quad_round) du CAST-256. Elle décompose un bloc de 128 bits en quatre blocs de 32 bits, puis applique les fonctions spécifiques à chaque round dans un ordre particulier. Les résultats intermédiaires sont recombinés pour former le bloc de sortie.
   - reverse_quad_round(abcd, kr, km) : Cette fonction correspond à la phase de déchiffrement (reverse_quad_round) du CAST-256. Elle décompose un bloc de 128 bits de la même manière que la fonction forward_quad_round, mais applique les fonctions dans l'ordre inverse.
3. key_generator.py : Le fichier key_generator.py contient des  opérations spécifiques à chaque octave de l'algorithme CAST-256
   - forward_octave(abcdefgh, tr, tm) : Cette fonction correspond à la phase d'octave du chiffrement CAST-256. Elle décompose un bloc de 256 bits en huit blocs de 32 bits, puis applique les fonctions spécifiques à chaque round dans un ordre particulier. Les résultats intermédiaires sont recombinés pour former le bloc de sortie.
   - initialization() : Cette fonction initialise les clés de rotation tr et de masque tm nécessaires à la génération des clés du CAST-256. Elle crée deux tableaux à deux dimensions (8x24) contenant respectivement les clés de rotation et de masque.
   - key_generator(key) : Cette fonction génère les clés de rotation kr et de masque km pour le chiffrement CAST-256 à partir de la clé de chiffrement (256 bits). Elle utilise les clés de rotation et de masque générées par la fonction initialization et applique des opérations spécifiques pour obtenir les clés de rotation et de masque nécessaires.
     
4. mode_operation.py :  Le fichier mode_operation.py contient des fonction des modes d'opération ECB (Electronic Codebook) et CBC (Cipher Block Chaining) pour le chiffrement et le déchiffrement avec l'algorithme CAST-256.
   - rdm_iv_generator() : Génère un vecteur d'initialisation (IV) aléatoire de 128 bits
   - encrypt_ecb(blocks, key) : Chiffre une liste de blocs en utilisant le mode d'opération Electronic Codebook (ECB) avec l'algorithme CAST-256.
   - decrypt_ecb(blocks, key) : Déchiffre une liste de blocs chiffrés en utilisant le mode d'opération Electronic Codebook (ECB) avec l'algorithme CAST-256.
   - encrypt_cbc(blocks, key) : Chiffre une liste de blocs en utilisant le mode d'opération Cipher Block Chaining (CBC) avec l'algorithme CAST-256.
   - decrypt_cbc(blocks, key) : Déchiffre une liste de blocs chiffrés en utilisant le mode d'opération Cipher Block Chaining (CBC) avec l'algorithme CAST-256.
   - decrypt(blocks, key, operation_mode="ECB") : Déchiffre une liste de blocs selon le mode d'opération spécifié ("ECB" ou "CBC").
   - encrypt(blocks, key, operation_mode="ECB") : Chiffre une liste de blocs selon le mode d'opération spécifié ("ECB" ou "CBC").

5. utils.py : Le fichier utils.py contient des fonctions qui permettront d'effectuer des opérations arithmétiques et binaires de base.

   - sum_mod_232(a, b) : Cette fonction effectue la somme de deux nombre a et b dans l'espace module 2^32
   -  diff_mod_232(a, b) : Cette fonction effectue la différence entre deux nombres aa et bb dans un espace modulo 2^32.
   - build_128_bit_bloc_from_32_bit_blocs(a, b, c, d) : Cette fonction assemble quatre blocs de 32 bits (a,b,c,d) en un seul bloc de 128 bits
   - extract_32bit_bloc_from_128(abcd) : Cette fonction décompose un bloc de 128 bits (abcd) en blocs de 32 bits (a,b,c,d)
   - extract_32bit_bloc_from_256(abcdefgh) : Cette fonction décompose un bloc de 256 bits (abcdefghabcdefgh) en huit blocs de 32 bits (a,b,c,d,e,f,g,h)
   - build_256_bit_bloc_from_32_bit_blocs(a, b, c, d, e, f, g, h) : Cette fonction assemble huit blocs de 32 bits (a, b, c, d, e, f, g, h) en un seul bloc de 256 bits
   - extract_8bit_blocs_from_32(abcd) : Cette fonction décompose un bloc de 32 bits (abcd) en quatre blocs de 8 bits
   - shift_left(data, input_size, n_bit) : Cette fonction effectue un décalage circulaire vers la gauche de n_bitn_bit positions sur un entier de taille input_sizeinput_size bits.
   
   
