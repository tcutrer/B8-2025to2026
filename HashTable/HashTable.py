"""
A implementation of a hash table in Python.
"""

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [OpenAddressingBucket.EMPTY_SINCE_START] * self.size
        self.cOne = 73  # Constant for quadratic probing
        self.cTwo = 37  # Constant for quadratic probing
        self.initalHashValue = 5381  # Initial hash value
        self.hashMultiplier = 33  # Multiplier for hash function
        self.loadFactorThreshold = 0.7  # Threshold to trigger resizing
        self.COLLISIONS = 0  # Counter for collisions
        self.bucketCount = 0  # Track used buckets to avoid O(n) counting
        self.BUCKET_CHECK_COUNT = 0

    def _hash(self, key):
        hash_value = self.initalHashValue
        for char in str(key):
            hash_value = (hash_value * self.hashMultiplier) + ord(char)
        return hash_value % self.size

    def insert(self, key, value):
        hashKey = self._hash(key)
        inserted = False
        multiple = 1
        is_new = False
        collided = False
        while not inserted:
            self.BUCKET_CHECK_COUNT += 1
            if self.table[hashKey].isEmpty():
                self.table[hashKey] = OpenAddressingBucket(key, value)
                inserted = True
                is_new = True
                self.bucketCount += 1
                if collided:
                    self.COLLISIONS += 1
                break
            elif self.table[hashKey].key == key:
                self.table[hashKey].value = value
                inserted = True
                break
            else:
                hashKey = (hashKey + 1) % self.size  # Linear probing
                multiple += 1
                if not collided:
                    collided = True

        # Only check resize if we added a new entry (not an update)
        if is_new and self.bucketCount / self.size > self.loadFactorThreshold:
            self._resize()

        return multiple
    
    def insert_or_update(self, key, value=1):
        """Optimized insert that handles word counting in one operation."""
        hashKey = self._hash(key)
        multiple = 1
        is_new = False
        collided = False
        while True:
            self.BUCKET_CHECK_COUNT += 1
            if self.table[hashKey].isEmpty():
                self.table[hashKey] = OpenAddressingBucket(key, value)
                is_new = True
                self.bucketCount += 1
                if collided:
                    self.COLLISIONS += 1
                break
            elif self.table[hashKey].key == key:
                # Update existing key
                self.table[hashKey].value += value
                break
            else:
                hashKey = (hashKey + 1) % self.size  # Linear probing
                multiple += 1
                if not collided:
                    collided = True
        
        # Only check resize if we added a new entry
        if is_new and self.bucketCount / self.size > self.loadFactorThreshold:
            self._resize()
        
        return multiple

    def search(self, key):
        hashKey = self._hash(key)
        empty_marker = OpenAddressingBucket.EMPTY_SINCE_START
        while self.table[hashKey] is not empty_marker:
            if self.table[hashKey].key == key:
                return self.table[hashKey].value
            else:
                hashKey = (hashKey + 1) % self.size  # Linear probing
        return None

    def delete(self, key):
        hashKey = self._hash(key)
        multiple = 1
        empty_marker = OpenAddressingBucket.EMPTY_SINCE_START
        while self.table[hashKey] is not empty_marker:
            if self.table[hashKey].key == key:
                self.table[hashKey] = OpenAddressingBucket.EMPTY_AFTER_REMOVAL
                self.bucketCount -= 1
                return True
            else:
                hashKey = (hashKey + 1) % self.size  # Linear probing
                multiple += 1
        return False
    
    def _resize(self):
        old_table = self.table
        self.size *= 2
        self.table = [OpenAddressingBucket.EMPTY_SINCE_START] * self.size
        self.bucketCount = 0  # Reset count

        for bucket in old_table:
            if not bucket.isEmpty():
                # Use direct insertion without resize checks to avoid recursive resizing
                self._insert_no_resize(bucket.key, bucket.value)
    
    def _insert_no_resize(self, key, value):
        """Insert without triggering resize checks (used during _resize)."""
        hashKey = self._hash(key)
        collided = False
        while True:
            self.BUCKET_CHECK_COUNT += 1
            if self.table[hashKey].isEmpty():
                self.table[hashKey] = OpenAddressingBucket(key, value)
                self.bucketCount += 1
                if collided:
                    self.COLLISIONS += 1
                break
            elif self.table[hashKey].key == key:
                self.table[hashKey].value = value
                break
            else:
                hashKey = (hashKey + 1) % self.size
                if not collided:
                    collided = True

class OpenAddressingBucket:
    def __init__(self, bucket_key = None, bucket_value = None):
        self.key = bucket_key
        self.value = bucket_value
    
    def isEmpty(self):
        if self is OpenAddressingBucket.EMPTY_SINCE_START:
            return True
        return self is OpenAddressingBucket.EMPTY_AFTER_REMOVAL

# Initialize two special bucket types: empty-since-start and empty-after-removal
OpenAddressingBucket.EMPTY_SINCE_START = OpenAddressingBucket()
OpenAddressingBucket.EMPTY_AFTER_REMOVAL = OpenAddressingBucket()