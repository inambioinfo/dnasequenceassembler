# dnasequenceassembler

## OVERVIEW

This python library assembles a unique DNA sequence given fragments of that sequence.
This library works best with at most 50 fragments no longer than 1000 base pairs.

## TECHNICAL APPROACH

Two fragments are considered to overlap if they match exactly by more than half of their length. The approach is to find all the pairs of overlapping fragments that meet the latter rule. Then the pattern of overlapping pairs is used to figure out the order of fragments. Once the order in which the fragments overlap is found, the indices of overlap are used to assemble the sequence.

## HOW TO USE

```shell
$ cd dnasequenceassembler
$ virtualenv venv
$ . venv/bin/activate
$ pip install .
$ assemble [YOUR_FILE_WITH_SEQUENCES_IN_FASTA_FORMAT]
```

your assembled sequence will be put in:
```shell
result_assembled_sequence.txt
```

###Example input:
my_fasta_sequences.txt
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

###Example output:
result_assembled_sequence.txt
```python
ATTAGACCTGCCGGAATAC
```

## RUN TESTS

```shell
$ cd dnasequenceassembler
$ virtualenv venv
$ . venv/bin/activate
$ pip install .
$ py.test dnasequenceassembler/test.py
```

## FASTA PARSER
[FASTA format](https://en.wikipedia.org/wiki/FASTA_format)

1. no more than 80 characters per license
2. first line of the FASTA file starts with ">"


## LIMITS

1. at most 50 DNA sequences in FASTA format
2. character set is limited to T/C/G/A
3. Each sequence does not exceed 1000 characters
