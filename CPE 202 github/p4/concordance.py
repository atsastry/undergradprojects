from hash_quad import *
import string


class Concordance:

    def __init__(self):
        self.stop_table = None  # hash table for stop words
        self.concordance_table = None  # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            f = open(filename, 'r')
        except:
            raise (FileNotFoundError)
        self.stop_table = HashTable(191)
        for line in f:
            self.stop_table.insert(line.strip())
        f.close()

    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table,
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        (The stop words hash table could possibly be None.)
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            f = open(filename, 'r')
        except:
            raise (FileNotFoundError)
        self.concordance_table = HashTable(191)
        str_conversion = f.read()
        lines = str_conversion.splitlines()
        for i in range(len(lines)):
            lines[i] = lines[i].replace("'", "")
            for ch in string.punctuation:
                lines[i] = lines[i].replace(ch, " ")
        newL = []
        for content in lines:
            newL.append(content.lower().split())
        for i in range(len(newL)):
            for word in newL[i]:
                if word.isalpha() and not self.stop_table.in_table(word):
                    # if it's not in the table already, insert it
                    if not self.concordance_table.in_table(word):
                        self.concordance_table.insert(word, [i + 1])
                    else:
                        # check for duplicates here
                        store_index = self.concordance_table.get_index(word)
                        if isinstance(store_index, int) and (i + 1) != self.concordance_table.hash[store_index][1][-1]:
                            self.concordance_table.hash[store_index][1].append(i + 1)
        f.close()

    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        f = open(filename, 'w')
        tot_keys = self.concordance_table.get_all_keys()
        tot_keys.sort()
        for key in tot_keys:
            lst_ints = self.concordance_table.get_value(key)
            lst_strs = [str(val) for val in lst_ints]
            line = key + ": " + " ".join(lst_strs)
            f.write(line)
            f.write('\n')
        f.close()