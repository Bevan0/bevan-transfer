# Bevan Transfer

**SECURITY WARNING: THIS PROGRAM SENDS FILES UNENCRYPTED THROUGH THE INTERNET! DO NOT SEND SENSITIVE FILES THROUGH IT.**

Bevan Transfer is a simple CLI file transfer system written in Python for single files.

## Usage

On the receiving computer, run `main.py` and enter `RECV`. Enter the (relative) file name & path for the received file to be written to. When you see "Please wait...", it is ready to receive files.

On the sending computer, run `main.py` and enter `SEND`. Enter the (relative) file name & path of the file to be sent. Next, enter the IP address of the receiving computer. Finally, it will confirm the file name and IP address. Enter `Y` to confirm and it will connect and send the file.

Once the file transfer is complete, the sending computer will exit the program. The receiving computer will continue to run but it will not accept additional connections; you can exit with `CTRL+C` / equivalent in your system's CLI.

## License

The project is licensed under the MIT License.
