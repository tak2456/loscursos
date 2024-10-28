# from os import environ

# port = int(environ.get('PORT', 8888))
# host = environ.get('HOST', 'localhost')


from os import environ
from pathlib import Path

here = Path(__file__).absolute().parent.parent

host = environ.get('HOST', 'localhost')
port = int(environ.get('PORT', 8888))

cert_file = environ.get('CERT_FILE', here / 'cert.pem')
key_file = environ.get('KEY_FILE', here / 'key.pem')
