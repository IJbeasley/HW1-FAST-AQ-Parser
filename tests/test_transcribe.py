# write tests for transcribe functions

# add current working directory to python path
# to load seqparser module
import sys
sys.path.append(".")

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True

def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """

    seq = "ATACGC"

    assert transcribe(seq, reverse=False) == "UAUGCG"
    assert transcribe(seq, reverse=True) == "GCGTAT"

    # separate test for lower case - make into function later
    assert transcribe(seq.lower(), reverse=False) == "UAUGCG"
    assert transcribe(seq.lower(), reverse=True) == "GCGTAT"

    # test for invalid nucleotide
    try:
        transcribe("AZFC")
    except ValueError as e:
        assert str(e) == "Invalid nucleotide in sequence. \nOnly allowed sequence values are: ['A', 'C', 'T', 'G']."


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """

    assert reverse_transcribe("UAUGCG") == "GCGTAT"

    # lower case test
    assert reverse_transcribe("uaugcg") == "GCGTAT"

    # test for invalid nucleotide
    try:
        reverse_transcribe("AZFC")
    except ValueError as e:
        assert str(e) == "Invalid nucleotide in sequence. \nOnly allowed sequence values are: ['A', 'C', 'T', 'G']."

    pass