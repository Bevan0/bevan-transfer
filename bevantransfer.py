import click
import socket
import sys

PORT = 4545

@click.group()
def cli():
    click.echo("Bevan Transfer\n(C) Copyright 2022 Bevan Ellis and contributors\nReleased under the MIT License\n")


@click.command("send")
@click.argument("file", type=click.File("rb"))
@click.argument("ip", type=click.STRING)
def do_send(file, ip):
    click.echo("Connecting to {}...".format(ip))
    sock = None
    try:
        sock = socket.socket()
        sock.connect((ip, PORT))
    except Exception as e:
        click.echo("Error occured when attempting to connect to IP.")
        click.echo(e.with_traceback())
        return

    sock.sendfile(file)
    sock.close()
    click.echo("File sent. Thank you for transferring.")
    file.close()
    return


@click.command("recv")
@click.argument("file", type=click.File("wb"))
def do_recv(file):
    click.echo("Please wait...")
    sock = socket.socket()
    sock.bind(("0.0.0.0", PORT))
    click.echo("Ready to accept files.")
    sock.listen(1)
    sock2, address = sock.accept()
    click.echo("Connection received from {}".format(address))
    try:
        while True:
            a = sock2.recv(1)
            if len(a) == 0:
                click.echo("File transferred.")
                sock2.close()
                sock.close()
                file.close()
                break
            file.write(bytes(a))
    except Exception as e:
        click.echo("An error occured while receiving:")
        click.echo(e.with_traceback())


cli.add_command(do_send)
cli.add_command(do_recv)

if __name__ == "__main__":
    cli()
