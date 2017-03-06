import click
from fastaparser import FastaParser
from assembler import Assembler

@click.command()
@click.argument('f', type=click.Path(exists=True))
@click.argument('result', type=click.Path(writable=True))
def touch(f,result):
    click.echo(click.format_filename(f))
    fasta_parser = FastaParser(f)
    parsed_sequences = fasta_parser.parse()
    assembler = Assembler(parsed_sequences)
    assembled = assembler.assemble()
    with open(result, "w") as text_file:
        text_file.write(assembled)
