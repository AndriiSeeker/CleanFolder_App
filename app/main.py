from app_design import start_app
from logger import get_logger

logger = get_logger(__name__)

if __name__ == '__main__':
    try:
        logger.info("The program started correctly")
        start_app()
    except Exception as err:
        logger.error(f'ERROR {err}')
    finally:
        logger.info("the program ended")

