# write tests for transcribe functions

# add current working directory to python path
# to load seqparser module
import sys
sys.path.append(".")

seq = "ATACGC"

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

    assert transcribe(seq, reverse=False) == "UAUGCG", "Normal sequence not transcribed correctly (by transcribe function)"	
    assert transcribe(seq, reverse=True) == "GCGUAU", "Reverse sequence not transcribed correctly (by transcribe function)"	

def test_transcribe_lower():
    """
    Test - does the transcribe function behave correctly for lower case sequences?
    """
    assert transcribe(seq.lower(), reverse=False) == "UAUGCG", "Normal lower case sequence not transcribed correctly (by transcribe function)"
    assert transcribe(seq.lower(), reverse=True) == "GCGUAU", "Reverse lower case sequence not transcribed correctly (by transcribe function)"

def test_transcribe_invalid():
    """
    Test - is an error raised for invalid nucleotides for the transcribe function?
    """	

    try:
        transcribe("AZFC")
        
        assert False, "Invalid nucleotide sequence should raise an error"

    except ValueError as e:
        assert str(e) == "Invalid nucleotide in sequence. \nOnly allowed sequence values are: ['A', 'C', 'T', 'G'].", "Invalid nucleotide sequence should raise an different ValueError"

def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """

   # test - does the reverse_transcribe behave correctly for a normal sequence (seq)
    assert reverse_transcribe(seq) == "GCGUAU", "Normal sequence not reverse transcribed correctly (by reverse_transcribe function)"

def test_reverse_transcribe_lower():
    """
    Test: does the reverse_transcribe function behave correctly for a lower case sequence? 
    """
    # test normal lower case sequence
    assert reverse_transcribe(seq.lower()) == "GCGUAU", "Normal lower case sequence not reverse transcribed correctly (by reverse_transcribe function)"	


def test_reverse_transcribe_invalid():
    """
    Test: is an error raised  for invalid nucleotide sequences for the reverse_transcribe function?
    """	

    try:
        reverse_transcribe("AZFC")

        assert False, "Invalid nucleotide sequence should raise an error"

    except ValueError as e:
        assert str(e) == "Invalid nucleotide in sequence. \nOnly allowed sequence values are: ['A', 'C', 'T', 'G'].", "Invalid nucleotide sequence should raise an different ValueError"	



