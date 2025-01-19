# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    A function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence

    Args:
    seq (str): The DNA sequence to transcribe (e.g. ATACGC).
    reverse (bool): If True, reverse-transcribe RNA to DNA.
    """

    seq = seq.upper()
        
    if reverse:
        return reverse_transcribe(seq)
    
    else:

        # check that all characters in the input sequence are valid
        if all(nuc in ALLOWED_NUC for nuc in seq):
            # if nucleotides are valid, then transcrip
            return ''.join(TRANSCRIPTION_MAPPING[nuc] for nuc in seq)
        
        else:
            raise ValueError("Invalid nucleotide in sequence. \n" 
                                       + "Only allowed sequence values are: " 
                                       + str(list(ALLOWED_NUC))
                                       + "."
                                       )


def reverse_transcribe(seq: str) -> str:
    """
    A function that will transcribe an input sequence and reverse
    the sequence

        Args:
    seq (str): The DNA sequence to transcribe (e.g. ATACGC).
    """
    seq = seq.upper()
    
    # check that all characters in the input sequence are valid
    if all(nuc in ALLOWED_NUC for nuc in seq):
        transcribed_seq =  ''.join(TRANSCRIPTION_MAPPING[nuc] for nuc in seq)[::-1]
        return transcribed_seq
    
    else: 
        raise ValueError("Invalid nucleotide in sequence. \n" 
                                  + "Only allowed sequence values are: " 
                                  + str(list(ALLOWED_NUC))
                                  + "."
                                  )
