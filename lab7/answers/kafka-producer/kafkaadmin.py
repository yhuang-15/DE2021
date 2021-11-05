from kafka.admin import KafkaAdminClient, NewTopic


def delete_topics(admin, topics):
    admin.delete_topics(topics)


def create_topics(admin, topic_list):
    admin.create_topics(new_topics=topic_list, validate_only=False)


if __name__ == '__main__':
    admin_client = KafkaAdminClient(bootstrap_servers="34.134.194.165:9092",
                                    client_id='Lab8')  # use your VM's external IP Here!
    topic_list = [NewTopic(name="game", num_partitions=1, replication_factor=1),
                  NewTopic(name="avg_score", num_partitions=1, replication_factor=1)]
    # delete_topics(admin_client, topics=['avg_score', 'game'])
    create_topics(admin_client, topic_list)
