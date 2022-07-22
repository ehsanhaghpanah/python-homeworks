import logging

def config_logging() -> None:
	# FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
	FORMAT = '%(asctime)s %(message)s'
	# logging.basicConfig(format = FORMAT)
	logging.basicConfig(level = logging.DEBUG, format = FORMAT)
	# logging.basicConfig(format = FORMAT, level = logging.DEBUG)

def foo():
	logging.debug("debug")
	# logging.warning("WARN")
	# logging.error("error")
	# logging.info("info")
	# logging.critical("critical")
	return None

config_logging()
foo()
