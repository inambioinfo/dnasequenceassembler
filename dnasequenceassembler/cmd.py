import click
from fastaparser import FASTAparser
from assembler import Assembler

@click.command()
@click.argument('f', type=click.Path(exists=True))
def touch(f):
    click.echo(click.format_filename(f))
    fasta_parser = FASTAparser(f)
    parsed_sequences = fasta_parser.parse()
    assembler = Assembler(parsed_sequences)
    result = assembler.assemble()
    with open("result_assembled_sequence.txt", "w") as text_file:
        text_file.write(result)
