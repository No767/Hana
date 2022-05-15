import typer

def main(hello: str = False):
    typer.echo(f"{hello}")
    
if __name__ == "__main__":
    typer.run(main)