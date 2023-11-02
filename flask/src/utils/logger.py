import json
import logging


class FormatterMmRfc(logging.Formatter):
    def formatMessage(self, record):
        try:
            record.args = json.dumps(record.args) if record.args else {}
        except TypeError:
            ...

        return self._style.format(record)


def load() -> None:
    formatter = FormatterMmRfc(
        """
            {
              "global_event_timestamp": "%(asctime)s",
              "level": "%(levelname)s",
              "message": "%(message)s",
              "context": "%(args)s",
              "path_name": "%(pathname)s",
              "func_name": "%(funcName)s",
              "service_name": "Example Lambda Api"
            }
        """
    )

    logger = logging.getLogger()
    logger.setLevel("WARNING")
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
