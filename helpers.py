from datetime import datetime, timedelta


class FormatLocator:

    @staticmethod
    def format_locator(locator_tuple, text_to_format):
        method, locator = locator_tuple
        locator = locator.format(text_to_format)
        return method, locator


class FutureDate:

    @staticmethod
    def future_date():
        return str(datetime.now().date() + timedelta(days=3))
