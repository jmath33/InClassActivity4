import pytest
import palindrome

def test_pal():
	assert (pal("deed")) == (True)

#test designed to fail
def test_pal_1():
	assert (pal("sis sis") == (False)

def test_pal_2():
	assert (pal("chipmunk") == (False)

