import os


def configure():

    return os.environ["GROUP_ID"],\
           os.environ["TOPIC"],\
           os.environ["CLIENT_ID"],\
           os.environ["CLIENT_SECRET"],\
           os.environ["BOOTSTRAP_SERVERS"]


if __name__ == '__main__':
    groupId, topic, clientId, clientSecret, bootstrapServers = configure()
    print(groupId)
    print(topic)
    print(clientId)
    print(clientSecret)
    print(bootstrapServers)

