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

    # test - is an error raised for invalid nucleotide
    try:
        transcribe("AZFC")
        
        assert False, "Invalid nucleotide sequence should raise an error"

    except ValueError as e:
        assert str(e) == "Invalid nucleotide in sequence. \nOnly allowed sequence values are: ['A', 'C', 'T', 'G']."


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    
    seq = "ATACGC"

   # test normal sequence
    assert reverse_transcribe("UAUGCG") == "GCGTAT"

    # test normal lower case sequence
    assert reverse_transcribe("uaugcg") == "GCGTAT"

    # test - is an error raised  for invalid nucleotide
    try:
        reverse_transcribe("AZFC")

        assert False, "Invalid nucleotide sequence should raise an error"

    except ValueError as e:
        assert str(e) == "Invalid nucleotide in sequence. \nOnly allowed sequence values are: ['A', 'C', 'T', 'G']."
