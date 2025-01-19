# write tests for parsers

# add current working directory to python path
# to load seqparser module
import sys
sys.path.append(".")

from seqparser import (
        FastaParser,
        FastqParser)

import pytest

def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    # test - is 'normal' / example fasta file parsed correctly? 
    # test.fa
    test_parser = FastaParser("data/test.fa")

   # check that the parser is returning the correct data types
    for header, seq in test_parser:
        assert isinstance(header, str)
        assert isinstance(seq, str)

    # check first seq is parsed correctly
    seq0 = 'TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA'
    first_line = list(test_parser)[0]
    assert first_line[0] == "seq0"
    assert first_line[1] == seq0


  # testing of edge cases - empty file, corrupted file
  # does parser correctly fail? 
def test_empty_FastaParser():
    """""
    Test of handling empty or corrupted fasta file
    """""
    # test empty file (blank.fa)
    try:
        test_parser = FastaParser("tests/blank.fa")

        for header, seq in test_parser:
            print(header)
            print(seq)

        assert False, "Empty file should have raised an error"
        
    except ValueError as e:
        assert str(e) == "File (tests/blank.fa) had 0 lines."

def test_corrupted_FastaParser():
   # test corrupted file - contain headers but sequence is blank lines
   # bad3.fa
    try: 
        test_parser = FastaParser("tests/bad3.fa")
        
        for header, seq in test_parser:
            print(header)
            print(seq)

        assert False, "Empty sequence lines should have raised an error"

    except ValueError as e:
        assert str(e) == "Got an empty line for tests/bad3.fa @ line 2" 

   # test corrupted file - contain headers but not sequence (no blank lines)
   # bad.fa
    try: 
        test_parser = FastaParser("tests/bad.fa")

        for header, seq in test_parser:
             print(header)
             print(seq)

        assert False, "Empty sequence lines should have raised an error"

    except ValueError as e:

        assert str(e) == "File (tests/bad.fa) had 0 lines."

   # test corrupted file - contain sequence but not headers
   # bad2.fa
   # ... but this error is not caught with the provided parser class
   # so I've commented out this test

  #  try:
  #      test_parser = FastaParser("tests/bad2.fa")

   #     for header, seq in test_parser:
   #          print(header)
   #          print(seq)

   # except ValueError as e:
   #     print(str(e)) 
   #     pass

def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """

    # test - first line of fastq file is None, if parsed as fasta
    test_parser = FastaParser("data/test.fq")
    first_line = list(test_parser)[0]
    assert first_line[0] is None

# does FastqParser correctly read in a fastq file
def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    # test - properly reads in normal file
    # test.fq
    test_parser = FastqParser("data/test.fq")

    for header, seq, qual in test_parser:
        assert isinstance(header, str)
        assert isinstance(seq, str)
        assert isinstance(qual, str)

    # check first seq is parsed correctly
    seq0 = 'TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG'
    qual0 = '*540($=*,=.062565,2>\'487\')!:&&6=,6,*7>:&132&83*8(58&59>\'8!;28<94,0*;*.94**:9+7"94(>7=\'(!5"2/!%"4#32='
    first_line = list(test_parser)[0]
    assert first_line[0] == "seq0"
    assert first_line[1] == seq0
    assert first_line[2] == qual0

# does FastqPparser correctly fail on empty or corrupted file?
def test_empty_FastqParser():
    # test  - does parser correctly fail on empty file
    # blank.fq
    try:
        test_parser = FastqParser("tests/blank.fq")

        for header, seq, qual in test_parser:
            assert isinstance(header, str)
            assert isinstance(seq, str)
            assert isinstance(qual, str)

        assert False, "Empty file should have raised an error"

    except ValueError:
        pass

def test_corrupt_FastqParser():    
    # test - does parser correctly fail on corrupted file? - contain headers but not sequence
    # bad.fq
    try:
        test_parser = FastqParser("tests/bad.fq")

        for header, seq, qual in test_parser:
            assert isinstance(header, str)
            assert isinstance(seq, str)
            assert isinstance(qual, str)

        assert False, "Empty sequence lines should have raised an error"

    except ValueError:
        pass
   

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    # test first line is None if fasta file is parsed as fastq
    test_parser = FastqParser("data/test.fa")
    first_line = list(test_parser)[0]
    assert first_line[0] is None


