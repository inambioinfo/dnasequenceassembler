# dnasequenceassembler

## OVERVIEW

This python library assembles a unique DNA sequence given fragments of that sequence.
This library works best with at most 50 fragments no longer than 1000 base pairs.

## TECHNICAL APPROACH

Two fragments are considered to overlap if they match exactly by more than half of their length. The approach is to find all the pairs of overlapping fragments that meet the latter rule. Then the pattern of overlapping pairs is used to figure out the order of fragments. Once the order in which the fragments overlap is found, the indices of overlap are used to assemble the sequence.

## HOW TO USE

### Requirements

```
Python 2.7
```

### Install

```shell
$ git clone https://github.com/paolacastro/dnasequenceassembler.git
$ cd dnasequenceassembler
$ virtualenv venv
$ . venv/bin/activate
$ pip install .
```

### Usage

```shell
Usage: assemble [OPTIONS] FASTA_FILE OUTPUT_FILE

Options:
  --show / --no-show  prints resulting order of fragments identifiers
```

#### Example usage

```shell
$ assemble --show dnasequenceassembler/data/sample_input.txt result.txt
```

#### Example output in the commandline via --show
```shell
>Frag_56
>Frag_58
>Frag_57
>Frag_59
```

#### Example FASTA_FILE
sample_input.txt
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

#### Example OUTPUT_FILE
result.txt
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

## FASTA PARSER AND FASTA SEQUENCE LIMITS
[FASTA format](https://en.wikipedia.org/wiki/FASTA_format)

### Fasta sequence convention
1. no more than 80 characters per line
2. first line of the FASTA file starts with ">"

### sequence limitations

1. at most 50 DNA sequences in FASTA format
2. character set is limited to T/C/G/A
3. Each sequence does not exceed 1000 characters
