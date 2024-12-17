"""
Модуль agent_logger.py

Этот модуль предоставляет класс AgentLogger, предназначенный для ведения логов
в рамках системы интерактивного анализа. Класс AgentLogger позволяет записывать
сообщения различных уровней важности (debug, info, warning, error, critical),
используя объект логирования из стандартной библиотеки Python.

Основные возможности:
- Ведение логов на разных уровнях важности.
- Поддержка форматированных строк и дополнительных аргументов.
- Возможность записи исключений с трассировкой стека.

Примеры использования:
>>> from agent_logger import AgentLogger
>>> logger = AgentLogger(logging.getLogger())
>>> logger.info("Это информационное сообщение.")
>>> logger.error("Произошла ошибка!")
"""

import logging


class AgentLogger(object):
    """
    Класс логгера агента интерактивного анализа.

    Этот класс используется для регистрации сообщений различного уровня важности,
    таких как отладочные сообщения, информационные, предупреждения, ошибки и критические ошибки.
    """

    def __init__(self, log):
        """
        Конструктор класса.

        :param log: Объект логирования, который будет использоваться для записи сообщений.
        :type log: logging.Logger
        """
        self._log = log

    def debug(self, msg, *args, **kwargs):
        """
        Запись отладочного сообщения.

        :param msg: Сообщение, которое нужно записать.
        :type msg: str
        :param args: Дополнительные аргументы для форматирования строки.
        :param kwargs: Ключевые слова для форматирования строки.
        """
        return self._log.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        """
        Запись информационного сообщения.

        :param msg: Сообщение, которое нужно записать.
        :type msg: str
        :param args: Дополнительные аргументы для форматирования строки.
        :param kwargs: Ключевые слова для форматирования строки.
        """
        return self._log.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        """
        Запись предупреждающего сообщения.

        :param msg: Сообщение, которое нужно записать.
        :type msg: str
        :param args: Дополнительные аргументы для форматирования строки.
        :param kwargs: Ключевые слова для форматирования строки.
        """
        return self._log.warning(msg, *args, **kwargs)

    def warn(self, msg, *args, **kwargs):
        """
        Запись предупреждающего сообщения (синоним метода warning).

        :param msg: Сообщение, которое нужно записать.
        :type msg: str
        :param args: Дополнительные аргументы для форматирования строки.
        :param kwargs: Ключевые слова для форматирования строки.
        """
        return self._log.warn(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        """
        Запись сообщения об ошибке.

        :param msg: Сообщение, которое нужно записать.
        :type msg: str
        :param args: Дополнительные аргументы для форматирования строки.
        :param kwargs: Ключевые слова для форматирования строки.
        """
        return self._log.error(msg, *args, **kwargs)

    def exception(self, msg, *args, exc_info=True, **kwargs):
        """
        Запись исключения с трассировкой стека.

        :param msg: Сообщение, которое нужно записать.
        :type msg: str
        :param args: Дополнительные аргументы для форматирования строки.
        :param exc_info: Флаг, определяющий необходимость включения информации о текущем исключении.
        :type exc_info: bool
        :param kwargs: Ключевые слова для форматирования строки.
        """
        return self._log.exception(msg, *args, exc_info=exc_info, **kwargs)

    def critical(self, msg, *args, **kwargs):
        """
        Запись критического сообщения.

        :param msg: Сообщение, которое нужно записать.
        :type msg: str
        :param args: Дополнительные аргументы для форматирования строки.
        :param kwargs: Ключевые слова для форматирования строки.
        """
        return self._log.critical(msg, *args, **kwargs)

    def log(self, level, msg, *args, **kwargs):
        """
        Запись сообщения с указанным уровнем важности.

        :param level: Уровень важности сообщения.
        :type level: int
        :param msg: Сообщение, которое нужно записать.
        :type msg: str
        :param args: Дополнительные аргументы для форматирования строки.
        :param kwargs: Ключевые слова для форматирования строки.
        """
        return self._log.log(level, msg, *args, **kwargs)


loggers = {}

LOG_FORMAT = "[%(asctime)s] %(levelname)s [%(name)s] %(message)s"


def logger_config(logging_name):
    """
    Получение логгера по названию
    :param logging_name: Название логгера
    :return: Объект логгера
    """

    global loggers

    if loggers.get(logging_name):
        return loggers.get(logging_name)

    logger = logging.getLogger(logging_name)
    logger.handlers.clear()

    level = logging.INFO

    logger.setLevel(level)

    console = logging.StreamHandler()
    console.setLevel(level)
    console.setFormatter(logging.Formatter(LOG_FORMAT))
    logger.addHandler(console)

    loggers[logging_name] = logger
    return AgentLogger(logger)
