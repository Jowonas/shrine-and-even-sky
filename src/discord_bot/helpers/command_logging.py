import logging


def command_log(fn):
    def __command_log_wrapper(*args, **kwargs):
        logger = logging.getLogger("Discord_Command_Logger")
        func_name: str = fn.__name__
        try:
            logger.info(f"Executing Function: {func_name}, args: {args} and kwargs {kwargs}")
            return fn(*args, *kwargs)
        except Exception as E:
            logger.warning(f"Error whilst Executing Function: {func_name}, args: {args}, kwargs: {kwargs}, Error: {E}")

    return __command_log_wrapper

