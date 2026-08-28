"""
Package: service
Package for the Counter Service
"""
import sys
from flask import Flask

# Create Flask application
app = Flask(__name__)

# Import the routes after the Flask app is created
from service import routes, models  # noqa: E402, E501
from service.common import error_handlers, log_handlers  # noqa: E402

# Set up logging for production
log_handlers.init_logging(app, "gunicorn.error")

app.logger.info(70 * "*")
app.logger.info(
    "  C O U N T E R   S E R V I C E   R U N N I N G  ".center(70, "*")
)
app.logger.info(70 * "*")

app.logger.info("Service initialized!")
