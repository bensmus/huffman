from huffman import *


def is_prefix(prefix, string):
    prefix_len = len(prefix)
    return string[:prefix_len] == prefix


def prefix_free(codes):
    for i, icode in enumerate(codes):
        for j, jcode in enumerate(codes):
            if i != j and is_prefix(icode, jcode):
                return False
    return True


class TestPrefix:
    def test_is_prefix(self):
        assert is_prefix('prefix', 'prefixes are cool')
        assert is_prefix('s', 'snakes are cool')
        assert is_prefix('snak', 'snakes are cool')
        assert not is_prefix('snk', 'snakes are cool')

    def test_prefix_free(self):
        codes = ['10', '11', '01', '00']
        assert prefix_free(codes)


class TestHuffman:
    def test_get_char_counts(self):
        assert get_char_counts('') == {}
        assert get_char_counts('abc') == {'a': 1, 'b': 1, 'c': 1}
        assert get_char_counts('aaabc') == {'a': 3, 'b': 1, 'c': 1}
  
    def test_NodeQueue(self):
        nq = NodeQueue({'a': 1, 'b': 4})
        print(nq.l)
        assert nq.length() == 2
        assert nq.pop() == Node('a', 1)
        assert nq.pop() == Node('b', 4)

    def test_codes_from_tree(self):
        leafA = Node('a', 2)
        leafB = Node('b', 2)
        root = Node('ab', 4, leafA, leafB)
        assert codes_from_tree(root) == {'a': '0', 'b': '1'}
    
    def test_get_huff_codes(self):
        assert (
            get_huff_codes('aab') == {'a': '0', 'b': '1'} or
            get_huff_codes('aab') == {'a': '1', 'b': '0'}
        )
        
        plaintext = 'aabc'
        mapping = get_huff_codes(plaintext) # mapping characters to codes
        assert len(mapping['a']) == 1 # 'a' more often: shorter code
        assert len(mapping['b']) == 2
        assert len(mapping['c']) == 2
    
    def test_prefix_free(self):
        plaintext = 'qwervhaaaskdfaaaskfj'
        mapping = get_huff_codes(plaintext)
        codes = mapping.values()
        assert prefix_free(codes)
