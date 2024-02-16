# Replacing the letters in DNA with their inverse, e.g. A to T
def DNA_strand(dna):
    letter_map = {"A": "T", "T": "A", "C": "G", "G": "C"}
    inverse = ""
    for char in dna:
        inverse += letter_map[char]
    return inverse
print(DNA_strand("GATTACA"))