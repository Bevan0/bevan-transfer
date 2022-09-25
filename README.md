# Bevan Transfer

**SECURITY WARNING: THIS PROGRAM SENDS FILES UNENCRYPTED THROUGH THE INTERNET! DO NOT SEND SENSITIVE FILES THROUGH IT.**

Bevan Transfer is a simple CLI file transfer system written in Python 3 for single files. It only requires the library Click to function.

## Installation

Run `python setup.py install` to install the program; setuptools will automatically install Click if it is not installed. The command `bevan-transfer` should become available in your CLI.

## Usage

On the receiving computer, run `bevan-transfer recv [file name]`, with [file name] being substituted with where you want to save your file. When you see `Ready to accept files.`, you can now send the file.

On the sending computer, run `bevan-transfer send [file name] [ip of receiver]`, with [file name] being substituted with the file you want to send and [ip of receiver] being substituted with the IP of the receiving computer.

Once the file transfer is complete, both the receiving and the sending programs will exit.

## License

The project is licensed under the MIT License.
