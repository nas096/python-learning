def to_rna(dna_strand):
    rnaTranscription = {
        "G": "C",
        "A": "U",
        "T": "A",
        "C": "G"
    }

    return "".join([rnaTranscription[nucleotide] for nucleotide in dna_strand])
