# IBM DB2 CDC Comparison

This project aims to compare and contrast IBM DB2 CDC options with Snowflake. It includes steps to build the project using both Debezium and Kafka, as well as Airbyte.

## Build with Debezium and Kafka
First DB2 needs to be installed on Docker. I followed [Installing DB2 on Your Coffee Break](https://ajstorm.medium.com/installing-db2-on-your-coffee-break-5be1d811b052) and modified it to use docker-compose. This is found in the root folder of the project. [^1]

To use the Db2 Command Line Processor (CLP) once the install has completed, run the following command:

`docker exec -it db2 bash -c "su - db2inst1"`


### Steps modified to use Snowflake as the target for Debezium:

1. In the "The solution at a very high level" section, skip the instructions for configuring Debezium with PostgreSQL and logical decoding plugins, as this is not necessary when using Snowflake as the target.
2. In the "Set up and run the project" section, modify the `KAFKA_CONNECT_CONFIG_STORAGE_TOPIC_REPLICATION_FACTOR` and `KAFKA_CONNECT_CONFIG_PROVIDERS` environment variables in the `kafka-connect` service to include the Snowflake connector configuration. You will also need to set the `KAFKA_CONNECT_CONFIG_PROVIDERS` variable to include the Debezium connector configuration.
3. Add a new service in the `docker-compose.yml` file for the Snowflake connector. Set the appropriate environment variables for the Snowflake connector, such as the Snowflake account, username, password, warehouse, database, and schema.
4. In the "Verify the changes" section, use the Snowflake web UI or a Snowflake client to verify that the change events captured by Debezium are being written to the target Snowflake database.

## Build replication with Airbyte

TODO: Add instructions for building replication with Airbyte.

## Project Repository

The project can be found at the following repository:

git clone https://github.com/ben-evolv/docker-compose-db2.git

[^1]: Storm, A. J. (n.d.). Installing DB2 on Your Coffee Break. Retrieved from https://ajstorm.medium.com/installing-db2-on-your-coffee-break-5be1d811b052


