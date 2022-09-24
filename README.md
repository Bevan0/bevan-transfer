# Bevan Transfer

**SECURITY WARNING: THIS PROGRAM SENDS FILES UNENCRYPTED THROUGH THE INTERNET! DO NOT SEND SENSITIVE FILES THROUGH IT.**

Bevan Transfer is a simple CLI file transfer system written in Python for single files. It has no dependencies, other than Python 3 (latest version recommended).

## Installation

Run `python setup.py install` to install the program; there are no dependencies. The command `bevan-transfer` should become available in your CLI.

## Usage

On the receiving computer, run `bevan-transfer` and enter `RECV`. Enter the (relative) file name & path for the received file to be written to. When you see "Please wait...", it is ready to receive files.

On the sending computer, run `bevan-transfer` and enter `SEND`. Enter the (relative) file name & path of the file to be sent. Next, enter the IP address of the receiving computer. Finally, it will confirm the file name and IP address. Enter `Y` to confirm and it will connect and send the file.

Once the file transfer is complete, both the receiving and the sending programs will exit.

## License

The project is licensed under the MIT License.
