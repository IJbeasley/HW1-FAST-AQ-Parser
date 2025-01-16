# write tests for parsers

# add current working directory to python path
# to load seqparser module
import sys
sys.path.append(".")

from seqparser import (
        FastaParser,
        FastqParser)

#import pytest

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
    print("yayo")
    #print(FastaParser("tests/test.fa"))

    # test empty file
    try:
        test_parser = FastaParser("tests/blank.fa")

        for header, seq in test_parser:
            print(header)
            print(seq)
        
    except ValueError as e:
        assert str(e) == "File (tests/blank.fa) had 0 lines."


    try: 
        test_parser = FastaParser("tests/bad3.fa")
        
        for header, seq in test_parser:
            print(header)
            print(seq)
 
    except ValueError as e:
        assert str(e) == "Got an empty line for tests/bad3.fa @ line 2" 

    # test corrupted file - contain headers but not sequence
    try: 
        test_parser = FastaParser("tests/bad.fa")

        for header, seq in test_parser:
             print(header)
             print(seq)

    except ValueError as e:

        assert str(e) == "File (tests/bad.fa) had 0 lines."

    # test corrupted file - contain sequence but not headers
    # error is not caught with provided parser function 
  #  try:
  #      test_parser = FastaParser("tests/bad2.fa")

   #     for header, seq in test_parser:
   #          print(header)
   #          print(seq)

   # except ValueError as e:
   #     print(str(e)) 
   #     pass

    # test normal file
    test_parser = FastaParser("data/test.fa")

    for header, seq in test_parser:
        assert isinstance(header, str)
        assert isinstance(seq, str)



#print(FastaParser("tests/bad3.fa"))
print(test_FastaParser())


#for header, sequence in test_parser:
#    print(f"Header: {header}")
#    print(f"Sequence: {sequence}")


#print(FastaParser("tests/bad.fa"))

#FastaParser("tests/test.fa")._get_record()
#test_FastaParser()


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    pass

FastqParser("tests/test.fq")

def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """

    # test empty file
    try:
        test_parser = FastqParser("tests/empty.fq")
    except ValueError:
        pass
    
    # test corrupted file - contain headers but not sequence
    try:
        FastqParser("tests/bad.fq")
    except ValueError:
        pass
   
   # test corrupted file - contain sequence but not headers
    try:
        FastqParser("tests/bad2.fq")
    except ValueError:
        pass
    


def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    pass