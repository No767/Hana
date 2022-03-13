import click

@click.command()
@click.option('--greeting', '-g')
def main(greeting):
    click.echo(f"please help me... {greeting}")
    
if __name__ == "__main__":
    main()