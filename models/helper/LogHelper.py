import logging
import models.mqtt as helper
# from models.mqtt import helper as helper
import paho.mqtt.client as paho
#
# user = ""
# password = ""
# broker = "173.230.128.181"
# transport = "websockets"  # "websockets" or "tcp"
# user = "mqtt_user"
#
# if transport == "websockets":
#     port = 9001
# elif transport == "tcp":
#     port = 1883
# else:
#     port = 1883
# broker_address = broker
# password = "ChestyPuller1775!"
#
# def on_publish(client,userdata,result):             #create function for callback
#     pass
# def on_disconnect():
#     client1.loop_stop()
#
# def recconnect():
# 	print("reconnectin...")
#
# def send_mqtt():
#     client1 = paho.Client(client_id="", clean_session=True,userdata=None, transport=transport)                           #create client object
#     client1.connect(broker, port)
#     client1.on_publish = on_publish  # assign function to callback
#     return client1
#
# def on_connect(client, userdata, flags, rc):
#     print("Connected with result code "+str(rc))
#
#
# client1 = helper.send_mqtt()
# client1.loop_start()


class Logger:
    logger = None

    def __init__(self):
        pass

    @classmethod
    def get_level(cls, level):
        if level == "CRITICAL":
            return logging.CRITICAL
        elif level == "ERROR":
            return logging.ERROR
        elif level == "WARNING":
            return logging.WARNING
        elif level == "INFO":
            return logging.INFO
        elif level == "DEBUG":
            return logging.DEBUG
        else:
            return logging.NOTSET

    @classmethod
    def configure(
        cls,
        filelog=1,
        logfile="pycryptobot.log",
        fileloglevel="DEBUG",
        consolelog=1,
        consoleloglevel="INFO",
    ):
        # reduce informational logging
        logging.getLogger("requests").setLevel(logging.WARNING)
        logging.getLogger("urllib3").setLevel(logging.WARNING)

        # initialize class logger
        cls.logger = logging.getLogger("pycryptobot")
        cls.logger.setLevel(logging.DEBUG)

        if not consolelog and not filelog:
            cls.logger.disabled = True

        if consolelog:
            # set a format which is simpler for console use
            consoleHandlerFormatter = logging.Formatter("%(message)s")
            # define a Handler which writes sys.stdout
            consoleHandler = logging.StreamHandler()
            # Set log level
            consoleHandler.setLevel(cls.get_level(consoleloglevel))

            # tell the handler to use this format
            consoleHandler.setFormatter(consoleHandlerFormatter)
            # add the handler to the root logger
            cls.logger.addHandler(consoleHandler)

        if filelog:
            # set up logging to file
            fileHandlerFormatter = logging.Formatter(
                fmt="%(asctime)s %(levelname)-8s %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )
            fileHandler = logging.FileHandler(logfile)
            fileHandler.setLevel(cls.get_level(fileloglevel))
            fileHandler.setFormatter(fileHandlerFormatter)
            cls.logger.addHandler(fileHandler)

    @classmethod
    def debug(cls, str):
        cls.logger.debug(str)

    @classmethod
    def info(cls, str):
        cls.logger.info(str)

    def mqtt(topic, str):
        client1 = helper.send_mqtt()
        client1.loop_start()
        ret = client1.publish("PyCryptoBot_test/"+topic, str)


    @classmethod
    def warning(cls, str):
        cls.logger.warning(str)

    @classmethod
    def error(cls, str):
        cls.logger.error(str)

    @classmethod
    def critical(cls, str):
        cls.logger.critical(str)
