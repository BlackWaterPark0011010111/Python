import logging

from utils import do_something
from common import configure_logging

logger = logging.getLogger(__name__)


def main ():
    configure_logging(level=logging.INFO)    

    logger.warning("hello")

    do_something()
    logger.warning("bye")




if __name__=="__main__":

    main()