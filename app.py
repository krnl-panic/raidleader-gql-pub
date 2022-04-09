from raidleader_gql import app
from waitress import serve
import logging


logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)

if __name__ == "__main__":
    serve(app, listen="*:42069")
