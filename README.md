# dnasequencealigner

##OVERVIEW

This python package figures out a unique DNA sequence given a maximum of 50 subsequences

Example input:

```python
>Frag_56
ATTAGACCTG
>Frag_57
CCTGCCGGAA
>Frag_58
AGACCTGCCG
>Frag_59
GCCGGAATAC
```

Example output:

```python
ATTAGACCTGCCGGAATAC
```

## FASTA PARSER

1. no more than 80 characters per license
2. first line of the FASTA file starts with ">"


## LIMITS

1. at most 50 DNA sequences in FASTA format
2. character set is limited to T/C/G/A
3. Each sequence does not exceed 1000 characters

## TECHNICAL

Two sequences are considered to overlap if they match exactly by more than half of their length.
