class ADN:
    # opening and reading the sequence file to make it an attribute of the class
    def __init__(self, sequence_file):
        with open(sequence_file, "r", encoding='utf-8-sig') as f:
            self.sequence = f.read()

        # conversion table as an attribute of the class
        self.conversion_table = {'ATA': 'I',
                            'ATC': 'I',
                            'ATT': 'I',
                            'ATG': 'M',
                            'ACA': 'T',
                            'ACC': 'T',
                            'ACG': 'T',
                            'ACT': 'T',
                            'AAC': 'N',
                            'AAT': 'N',
                            'AAA': 'K',
                            'AAG': 'K',
                            'AGC': 'S',
                            'AGT': 'S',
                            'AGA': 'R',
                            'AGG': 'R',
                            'CTA': 'L',
                            'CTC': 'L',
                            'CTG': 'L',
                            'CTT': 'L',
                            'CCA': 'P',
                            'CCC': 'P',
                            'CCG': 'P',
                            'CCT': 'P',
                            'CAC': 'H',
                            'CAT': 'H',
                            'CAA': 'Q',
                            'CAG': 'Q',
                            'CGA': 'R',
                            'CGC': 'R',
                            'CGG': 'R',
                            'CGT': 'R',
                            'GTA': 'V',
                            'GTC': 'V',
                            'GTG': 'V',
                            'GTT': 'V',
                            'GCA': 'A',
                            'GCC': 'A',
                            'GCG': 'A',
                            'GCT': 'A',
                            'GAC': 'D',
                            'GAT': 'D',
                            'GAA': 'E',
                            'GAG': 'E',
                            'GGA': 'G',
                            'GGC': 'G',
                            'GGG': 'G',
                            'GGT': 'G',
                            'TCA': 'S',
                            'TCC': 'S',
                            'TCG': 'S',
                            'TCT': 'S',
                            'TTC': 'F',
                            'TTT': 'F',
                            'TTA': 'L',
                            'TTG': 'L',
                            'TAC': 'Y',
                            'TAT': 'Y',
                            'TAA': '_',
                            'TAG': '_',
                            'TGC': 'C',
                            'TGT': 'C',
                            'TGA': '_',
                            'TGG': 'W', }

    # method that returns the sequence
    def get_sequence(self):
        return self.sequence

    # method that returns the conversion table
    def get_conversion_table(self):
        return self.conversion_table

    # method to get an arrays of strings from one big string, regrouped by a certain nb of elements
    def split_sequence_in_array(self, split_nb) -> list:
        sequence = self.sequence
        return [sequence[i:i + split_nb] for i in range(0, len(sequence), split_nb)]


    # method to translate an array of characters using the conversion table
    def convert_codon_sequence_to_proteines(self, codon_list):
        proteine_sequence = ""
        for codon in codon_list:
            if codon in self.conversion_table:
                proteine_sequence += self.conversion_table[codon]
        return proteine_sequence

