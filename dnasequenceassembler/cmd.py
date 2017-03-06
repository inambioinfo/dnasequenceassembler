import click
from fastaparser import FastaParser
from assembler import Assembler

@click.command()
@click.argument('fasta_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path(writable=True))
@click.option('--show/--no-show', default=False,
                help='prints resulting order of fragments identifiers')
def touch(fasta_file, output_file, show):
    click.echo(click.format_filename(fasta_file))
    fasta_parser = FastaParser(fasta_file)
    fragments, fragment_ids  = fasta_parser.parse()
    assembler = Assembler(fragments, fragment_ids, print_fragment_id_order=show)
    assembled = assembler.assemble()
    with open(output_file, "w") as text_file:
        text_file.write(assembled)
