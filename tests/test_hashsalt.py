from hash.hashsalt import HashSalt
import random
import string

def test_hashsalt() -> None:
    test_str = ''.join((random.choice(string.ascii_letters + string.digits) for i in range(8)))
    hash = HashSalt(test_str)
    hashed_data = hash.generate_salted_hash()

    assert hashed_data == hash.generate_salted_hash()
    
    hash1 = HashSalt(test_str)
    assert hashed_data != hash1.generate_salted_hash()
    
    test_str = ''.join((random.choice(string.ascii_letters) for i in range(8)))
    hash2 = HashSalt(test_str)
    hashed = hash2.generate_salted_hash()
    assert hashed == hash2.generate_salted_hash()
    
    hash3 = HashSalt(test_str)
    assert hashed != hash3.generate_salted_hash()