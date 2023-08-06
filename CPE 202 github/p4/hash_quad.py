from math import sqrt
import math

class HashTable:

    def __init__(self, table_size): # add appropriate attributes, NO default size
        ''' Initializes an empty hash table with a size that is the smallest
            prime number that is >= table_size (i.e. if 10 is passed, 11 will
            be used, if 11 is passed, 11 will be used.)'''
        self.num_items = 0
        if self.is_prime(table_size):
            self.table_size = table_size
        else:
            self.table_size = self.next_prime(table_size)
        self.hash = [None] * self.table_size

        # table size not working when size 1 is passed
        # when 1 is passed, it prints [None] but i believe the table size should be changed to 2 (next largest prime number)
         # so it should be printing [None, None] ?

    def insert(self, key, value=None):
        ''' Inserts an entry into the hash table (using Horner hash function to determine index,
                and quadratic probing to resolve collisions).
                The key is a string (a word) to be entered, and value is any object (e.g. Python List).
                If the key is not already in the table, the key is inserted along with the associated value
                If the key is in the table, the new value replaces the existing value.
                If load factor is greater than 0.5 after an insertion, hash table size should be increased
                to the next prime greater than 2*table_size.'''
        index = self.horner_hash(key) % self.table_size
        constant = index
        if self.hash[index] is None:
            self.num_items += 1
            self.hash[index] = (key, value)
        elif self.hash[index][0] == key and self.hash[index][1] != value:
            self.hash[index] = (key, value)
        else:
            j = 0
            self.num_items += 1
            while self.hash[index] is not None:
                store = (constant + j**2) % self.table_size
                if self.hash[store] is None:
                    self.hash[store] = (key, value)
                    break
                elif self.hash[store][0] == key:
                    self.hash[store] = (key, value)
                    break
                else:
                    index = store
                    j += 1
        if self.get_load_factor() > 0.5:
            self.rehash()

    def rehash(self):
        self.num_items = 0
        og_hash = self.hash
        self.table_size = self.next_prime(2 * self.table_size)
        self.hash = [None] * self.table_size
        for tups in og_hash:
            if tups is not None:
                self.insert(tups[0], tups[1])


    def horner_hash(self, key: str):
        ''' Compute the hash value by using Horner’s rule, as described in project specification.
            This method should not mod with the table size'''
        n = min(len(key), 8)
        horner_sum = 0
        for i in range(n):
            horner_sum += ord(key[i]) * 31**(n - 1 - i)
        return horner_sum

    def next_prime(self, n):
        if n <= 1:
            return 2
        prime = n
        found = False
        while not found:
            prime = prime + 1
            if self.is_prime(prime) == True:
                found = True
        return prime

    def is_prime(self, n):
        if (n <= 1):
            return False
        if (n <= 3):
            return True
        if (n % 2 == 0 or n % 3 == 0):
            return False
        for i in range(5, int(math.sqrt(n) + 1), 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True


    def in_table(self, key):
        ''' Returns True if key is in an entry of the hash table, False otherwise.'''
        if self.get_index(key) is None:
            return False
        return True

    def get_index(self, key):
        ''' Returns the index of the hash table entry containing the provided key.
        If there is not an entry with the provided key, returns None.'''
        # if self.in_table(key) == False:
        #     return None
        cnt = 0
        index = self.horner_hash(key) % self.table_size
        store = index
        change = self.hash[index]
        if change is None:
            return None
        while change[0] != key:
            cnt += 1
            store = (index + cnt*cnt) % self.table_size
            change = self.hash[store]
            if change is None:
                return None
        return store


    def get_all_keys(self):
        ''' Returns a Python list of all keys in the hash table.'''
        newL = []
        for item in self.hash:
            if item is not None:
                newL.append(item[0])
        return newL

    def get_value(self, key):
        ''' Returns the value associated with the key.
        If key is not in hash table, returns None.'''
        if not self.in_table(key):
            return None
        store = self.get_index(key)
        value = self.hash[store][1]
        return value


    def get_num_items(self):
        ''' Returns the number of entries in the table.'''
        return self.num_items

    def get_table_size(self):
        ''' Returns the size of the hash table.'''
        return self.table_size

    def get_load_factor(self):
        ''' Returns the load factor of the hash table (entries / table_size).'''
        return self.num_items/self.table_size