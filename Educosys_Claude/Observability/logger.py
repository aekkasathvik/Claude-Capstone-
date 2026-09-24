import logging


# Set root logger to WARNING — suppresses noisy third-party library logs (OpenAI, httpcore etc.)
logging.basicConfig(
   level=logging.WARNING,
   format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

def get_logger(name: str) -> logging.Logger:
   # Our own loggers run at DEBUG — only third-party libraries are suppressed and making it easy to understand what's happening in our codebase.and what file is this log part of 
   logger = logging.getLogger(name)
   logger.setLevel(logging.DEBUG)
   return logger