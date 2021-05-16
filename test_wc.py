import pytest
import wc

def test_count():
	assert count("How many words are in this?") == 6

def test_count():
	assert count("One") == 1

def test_count():
	assert count("; : ! @") == 4
