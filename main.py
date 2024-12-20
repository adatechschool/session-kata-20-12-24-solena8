from adn import ADN

adn = ADN("sequence.txt")
codons = adn.split_sequence_in_array(3)
print(codons)
proteines = adn.convert_codon_sequence_to_proteines(codons)
print(proteines)
get_25_nucleotides = adn.split_sequence_in_array(25)
print(get_25_nucleotides)
