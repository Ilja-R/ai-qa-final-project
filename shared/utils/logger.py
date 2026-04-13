import logging
import sys
import os

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

def setup_logger(name: str) -> logging.Logger:
    """
    Configures a logger with both console and file handlers.
    """
    logger = logging.getLogger(name)
    
    # If logger already has handlers, don't add more (prevents duplicate logs)
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    # Standard professional format
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Console Handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File Handler
    file_handler = logging.FileHandler("logs/app.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

# Pre-configured loggers for major components
app_logger = setup_logger("app")
service_logger = setup_logger("service")
ai_logger = setup_logger("ai")
