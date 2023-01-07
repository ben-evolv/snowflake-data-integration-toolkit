# Data Integration Toolkit

This project provides a modular approach to data integration, allowing you to create multiple scenarios using different combinations of data sources, replication methods, transformation, and target data warehouse.

## Project Structure

The project is structured as follows:

- `src`: This directory contains the source code for the various data sources, replication methods, transformation, and target data warehouse modules.
  - `data_sources`: This directory contains the code and configuration files for the different data sources available, such as DB2, Postgres, and MySQL.
  - `replication_methods`: This directory contains the code and configuration files for the different replication methods available, such as Debezium and Kafka, Airbyte, Matillion, and Fivetran.
  - `transformation`: This directory contains the code and configuration files for the different transformation tools available, such as dbt.
- `scenarios`: This directory contains the configuration files for each individual data integration scenario.

data_integration_toolkit<br>
├── src<br>
│ ├── data_sources<br>
│ │ ├── db2<br>
│ │ │ ├── code<br>
│ │ │ ├── config<br>
│ ├── replication_methods<br>
│ │ ├── airbyte<br>
│ │ │ ├── code<br>
│ │ │ ├── config<br>
├── scenarios<br>
│ ├── db2_to_snowflake_with_airbyte<br>
│ │ ├── docker-compose.yml<br>
│ │ ├── data_source_config.yml<br>
│ │ ├── replication_config.yml<br>
│ │ ├── target_config.yml<br>

## Setting Up a Scenario

To set up a new data integration scenario, follow these steps:

1. Choose the data source, replication method, transformation, and target data warehouse modules that you want to use for your scenario.
2. In the `src` directory, navigate to the code and configuration directories for each of the modules that you selected.
3. Follow the instructions in the `README.md` files for each module to set up the code and configuration files.
4. In the `scenarios` directory, create a new directory for your scenario and add the necessary configuration files.
5. Run the data integration scenario using the appropriate command line tools or scripts.

## Additional Resources

- [Data Sources](src/data_sources/README.MD): Information and instructions for each of the data sources available.
- [Replication Methods](src/replication_methods/README.MD): Information and instructions for each of the replication methods available.
- [Transformation](src/transformation/README.MD): Information and instructions for the transformation tools available.
