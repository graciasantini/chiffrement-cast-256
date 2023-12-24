# chiffrement-cast-256
Le chiffrement CAST-256, également connu sous le nom de CAST6, appartient à la famille des algorithmes de chiffrement de blocs.

Cast-256 fonctionne avec des blocs de 128 bits et des clés de 128, 160, 192, 224, ou 256 bits, offrant ainsi une flexibilité en termes de longueur de clé.

CAST-256 utilise une structure en réseau de Feistel, qui divise la clé en sous-clés pour chaque tour d'opération. Il effectue un certain nombre de tours (rounds) pour mélanger les données de manière sécurisée 

# Explication de fichier

1. Cast256.py
   
2. function_cast256.py
   
3. key_generator.py
   
4. mode_operation.py
   
5. utils.py
   Le fichier utils.py contient des fonctions qui permettront d'effectuer des opérations arithmétiques et binaires de base.
   
   A. sum_mod_232(a, b) : Cette fonction effectue la somme de deux nombre a et b dans l'espace module 2^32
   
   B. diff_mod_232(a, b) : Cette fonction effectue la différence entre deux nombres aa et bb dans un espace modulo 2^32.
   
   C. build_128_bit_bloc_from_32_bit_blocs(a, b, c, d) : Cette fonction assemble quatre blocs de 32 bits (a,b,c,d) en un seul bloc de 128 bits
   
   D. extract_32bit_bloc_from_128(abcd) : Cette fonction décompose un bloc de 128 bits (abcd) en blocs de 32 bits (a,b,c,d)
   
   E. extract_32bit_bloc_from_256(abcdefgh) : Cette fonction décompose un bloc de 256 bits (abcdefghabcdefgh) en huit blocs de 32 bits (a,b,c,d,e,f,g,h)
   
   F. build_256_bit_bloc_from_32_bit_blocs(a, b, c, d, e, f, g, h) : Cette fonction assemble huit blocs de 32 bits (a, b, c, d, e, f, g, h) en un seul bloc de 256 bits
   
   G. extract_8bit_blocs_from_32(abcd) : Cette fonction décompose un bloc de 32 bits (abcd) en quatre blocs de 8 bits
   
   H. shift_left(data, input_size, n_bit) : Cette fonction effectue un décalage circulaire vers la gauche de n_bitn_bit positions sur un entier de taille input_sizeinput_size bits.
   
   
