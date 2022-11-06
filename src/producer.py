import os
import sys
import logging

logging.basicConfig(level=logging.DEBUG)

def configure():

    return os.environ["GROUP_ID"],\
           os.environ["TOPIC"],\
           os.environ["CLIENT_ID"],\
           os.environ["CLIENT_SECRET"],\
           os.environ["BOOTSTRAP_SERVERS"]


if __name__ == '__main__':
    groupId, topic, clientId, clientSecret, bootstrapServers = configure()
    try:
        logging.debug(groupId)
        logging.debug(topic)
        logging.debug(clientId)
        logging.debug(clientSecret)
        logging.debug(bootstrapServers)
    except KeyError:
        logging.debug("Environment variable not found")
        sys.exit(1)

