from pytoolbox.cache.lru_cache import LRUCache


def test_create_instance_without_cache_len():
    # Arrange
    cache = LRUCache()

    # Act & Assert
    assert isinstance(cache, LRUCache)


def test_create_instance_with_cache_len():
    # Arrange
    cache = LRUCache(cache_len=10)

    # Act & Assert
    assert isinstance(cache, LRUCache)


def test_add_element_to_cache():
    # Arrange
    cache = LRUCache()

    # Act
    cache["key"] = "value"

    # Assert
    assert "key" in cache


def test_add_element_to_cache_multiples_keys():
    # Arrange
    cache = LRUCache()

    # Act
    cache[("key", "key_2", "key_3")] = "value"

    # Assert
    assert ("key", "key_2", "key_3") in cache


def test_add_element_with_empty_key():
    # Arrange
    cache = LRUCache()

    # Act
    cache[""] = "value"

    # Assert
    assert "" in cache


def test_retrieve_element():
    # Arrange
    cache = LRUCache()

    # Act
    cache["key"] = "value"

    # Assert
    assert cache["key"] == "value"


def test_retrieve_element_with_multiples_keys():
    # Arrange
    cache = LRUCache()

    # Act
    cache[("key_1", "key_2", "key_3")] = "value"

    # Assert
    assert cache[("key_1", "key_2", "key_3")] == "value"


def test_retrieve_element_with_empty_key():
    # Arrange
    cache = LRUCache()

    # Act
    cache[""] = "value"

    # Assert
    assert cache[""] == "value"


def test_removed_old_elements():
    # Arrange
    cache = LRUCache(cache_len=2)

    # Act
    cache["key_1"] = "value_1"
    cache["key_2"] = "value_2"
    cache["key_3"] = "value_3"
    cache["key_4"] = "value_4"

    # Assert
    assert "key_1" not in cache
    assert "key_2" not in cache
    assert "key_3" in cache
    assert "key_4" in cache

    assert len(cache) == 2


def test_removed_old_elements_with_multiples_keys():
    # Arrange
    cache = LRUCache(cache_len=2)

    # Act
    cache[("key_1", "key_11", "key_111")] = "value_111"
    cache[("key_1", "key_12", "key_121")] = "value_121"
    cache[("key_2", "key_21", "key_211")] = "value_211"
    cache[("key_2", "key_22", "key_221")] = "value_221"

    cache[("key_1", "key_11", "key_112")] = "value_112"
    cache[("key_1", "key_12", "key_122")] = "value_122"
    cache[("key_2", "key_21", "key_212")] = "value_212"
    cache[("key_2", "key_22", "key_222")] = "value_222"

    # Assert
    assert ("key_1", "key_11", "key_111") not in cache
    assert ("key_1", "key_11", "key_112") not in cache
    assert ("key_1", "key_12", "key_121") not in cache
    assert ("key_1", "key_12", "key_122") not in cache
    assert ("key_2", "key_21", "key_211") not in cache
    assert ("key_2", "key_21", "key_221") not in cache
    assert cache[("key_2", "key_21", "key_212")] == "value_212"
    assert cache[("key_2", "key_22", "key_222")] == "value_222"

    assert len(cache) == 2
