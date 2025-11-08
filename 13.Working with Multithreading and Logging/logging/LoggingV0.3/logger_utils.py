import logging


class CustomFilter(logging.Filter):
    def filter(self, record):
        return "ALARM" not in record.getMessage()
    

class MyLoggerAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        user_data = kwargs.get("user", "unknown")
        return f"{msg} {{user={user_data}}}", kwargs
    
    