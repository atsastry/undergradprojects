from ordered_list import *
from huffman_bit_writer import *
from huffman_bit_reader import *

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char  # stored as an integer - the ASCII character code value
        self.freq = freq  # the frequency associated with the node
        self.left = None  # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

    def __eq__(self, other):
        '''Needed in order to be inserted into OrderedList'''
        return self is not None and other is not None and self.char == other.char and self.freq == other.freq

    def __lt__(self, other):
        '''Needed in order to be inserted into OrderedList'''
        # returns true if self should come before other when added to an OrderedList
        return isinstance(other, HuffmanNode) and self.freq < other.freq or (self.freq == other.freq and self.char < other.char)


def read_file(file_name):
    with open(file_name, 'r', newline='') as f:
        output = f.read()
        f.close()
    return output


def write_file(file_name, content):
    with open(file_name, 'w', newline='')as f:
        f.write(content)
        f.close()

def cnt_freq(filename):
    '''Opens a text file with a given file name (passed as a string) and counts the
    frequency of occurrences of all the characters within that file'''
    f = open(filename, 'r')
    newL = [0] * 256
    for line in f:
        for char in line:
            newL[ord(char)] += 1
    f.close()
    return newL


def create_huff_tree(char_freq):
    '''Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree'''
    huff_tree = OrderedList()
    for i in range(len(char_freq)):
        if char_freq[i] > 0:
            huff_tree.add(HuffmanNode(i, char_freq[i]))
    if huff_tree.is_empty():
        return huff_tree.add(HuffmanNode(48, 256))
    while huff_tree.size() > 1:
        child = huff_tree.pop(0)
        child_2 = huff_tree.pop(0)
        huff_parent_freq = child.freq + child_2.freq
        if child.char < child_2.char:
            char = child.char
        else:
            char = child_2.char
        huff_parent_node = HuffmanNode(char, huff_parent_freq)
        huff_tree.add(huff_parent_node)
        huff_parent_node.left = child
        huff_parent_node.right = child_2
    return huff_tree.pop(0)


def create_code(node):
    '''Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation
    as the index into the arrary, with the resulting Huffman code for that character stored at that location'''
    # do this recursively ??
    newL = [""] * 256
    if node is None:
        return None
    return create_code_helper(node, newL, "")


def create_code_helper(node, huff_codes_lst, huff_str):
    # base case: no children
    if node.right is None and node.left is None:
        huff_codes_lst[node.char] = huff_str
    if node.left is not None:
        create_code_helper(node.left, huff_codes_lst, huff_str + "0")
    if node.right is not None:
        create_code_helper(node.right, huff_codes_lst, huff_str + "1")
    return huff_codes_lst


def create_header(freqs):
    '''Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” '''
    newL = []
    for i in range(len(freqs)):
        if freqs[i] > 0:
            newL.append(str(i))
            newL.append(str(freqs[i]))
    string = " ".join(newL)
    return string


def huffman_encode(in_file, out_file):
    '''Takes input file name and output file name as parameters - both files will have .txt extensions
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Also creates a second output file which adds _compressed before the .txt extension to the name of the file.
    This second file is actually compressed by writing individual 0 and 1 bits to the file using the utility methods
    provided in the huffman_bits_io module to write both the header and bits.
    Take not of special cases - empty file and file with only one unique character'''
    try:
        in_file_text = open(in_file, 'r')
    except FileNotFoundError:
        raise FileNotFoundError
    out_file_text = open(out_file, 'w')
    out_file_compressed = HuffmanBitWriter(out_file.replace('.txt', '_compressed.txt'))
    in_file_freq = cnt_freq(in_file)
    header = create_header(in_file_freq)
    # do this for compressed
    huff_trees = create_huff_tree(in_file_freq)
    if huff_trees == None:
        out_file = in_file
        in_file_text.close()
        out_file_text.close()
        out_file_compressed.close()
        return
    #if huff_trees.right is not None or huff_trees.left is not None:
    out_file_compressed.write_str(header + '\n')
    out_file_text.write(header + '\n')
    huff_code = create_code(huff_trees)
    for i in in_file_text:
        for j in i:
            out_file_text.write(huff_code[ord(j)])
            out_file_compressed.write_code(huff_code[ord(j)])
    out_file_text.close()
    out_file_compressed.close()
    in_file_text.close()


def parse_header(header_string: str):
    list_of_freqs = [0] * 256
    header_lst = header_string.split()
    for i in range(len(header_lst) // 2):
        list_of_freqs[int(header_lst[i * 2])] = int(header_lst[(i * 2) + 1])
    return list_of_freqs


def huffman_decode(encoded_file, decode_file):
    try:
        hbr = HuffmanBitReader(encoded_file)
    except FileNotFoundError:
        raise FileNotFoundError
    header = hbr.read_str()
    list_of_freqs = parse_header(header)
    huff_tree = create_huff_tree(list_of_freqs)
    node = huff_tree
    total = sum(list_of_freqs)
    newL = []
    counter = 0
    while counter < total:
        if node.left is None and node.right is None:
            newL.append(chr(node.char))
            node = huff_tree
            counter += 1
        elif hbr.read_bit() == False:
            node = node.left
        else:
            node = node.right
    write_file(decode_file, "".join(newL))
    hbr.close()
