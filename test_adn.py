from adn import ADN

class TestADN:

    def setUp(self):
        # with open("adn.txt", "r", encoding='utf-8-sig') as f:
        #     string_sequence = f.read()
        adn = ADN("sequence.txt")
        return adn

    def test_sequence_getter_returns_a_string(self):
        adn = self.setUp()
        assert type(adn.get_sequence()) == str

    def test_conversion_table_getter_returns_a_dictionnary(self):
        adn = self.setUp()
        assert type(adn.get_conversion_table()) == dict

    def test_get_codons_returns_a_list(self):
        adn = self.setUp()
        assert type(adn.split_sequence_in_array(3)) == list

    def test_get_codons_returns_a_list_split_by_3_characters(self):
        adn = self.setUp()
        assert len(adn.split_sequence_in_array(3)[0]) == 3
        assert len(adn.split_sequence_in_array(3)[2]) == 3
        assert len(adn.split_sequence_in_array(3)[5]) == 3

    def test_get_codons_returns_correct_characters(self):
        adn = self.setUp()
        assert adn.split_sequence_in_array(3)[0] == "CTC"
        assert adn.split_sequence_in_array(3)[1] == "TTG"
        assert adn.split_sequence_in_array(3)[2] == "AAC"


    def test_convert_codon_to_proteine_returns_correct_key(self):
        adn = self.setUp()
        assert adn.convert_codon_to_proteine("GTT") == "V"

    def test_convert_codon_sequence_to_proteines_returns_correct_list(self):
        adn = self.setUp()
        assert adn.convert_codon_sequence_to_proteines(["GTT", "CGT", "TGA"]) == "VR_"





