import click
from fastaparser import FASTAparser
from aligner import Aligner

@click.command()
@click.argument('f', type=click.Path(exists=True))
def touch(f):
    click.echo(click.format_filename(f))
    fasta_parser = FASTAparser(f)
    parsed_sequences = fasta_parser.parse()
    aligner = Aligner(parsed_sequences)
    aligner.align()
