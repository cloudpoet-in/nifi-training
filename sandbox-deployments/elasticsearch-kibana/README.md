# Elasticsearch and Kibana Docker Setup

This repository contains a Docker Compose setup for running Elasticsearch and Kibana. This allows you to easily deploy a local instance of Elasticsearch and Kibana for development and testing purposes.

## Prerequisites

Ensure you have Docker and Docker Compose installed on your machine:

- [Docker](https://docs.docker.com/engine/install/)

## Services

### Elasticsearch

- **Image**: `docker.elastic.co/elasticsearch/elasticsearch:7.17.24`
- **Container Name**: `es01-test`
- **Ports**: 
  - `9200:9200` (HTTP)
  - `9300:9300` (Transport)
- **Environment Variables**:
  - `discovery.type=single-node`

### Kibana

- **Image**: `docker.elastic.co/kibana/kibana:7.17.24`
- **Container Name**: `kib01-test`
- **Ports**: 
  - `5601:5601` (HTTP)
- **Environment Variables**:
  - `ELASTICSEARCH_HOSTS=http://es01-test:9200`
- **Depends On**: `elasticsearch`

## Network

- **Name**: `elastic`
- **Driver**: `bridge`

## Getting Started

1. **Clone the Repository**
   ```sh
   git clone https://github.com/cloudpoet-in/nifi-training.git
   cd nifi-training/elasticsearch-kibana
   docker-compose up -d
2. **Verify the Setup**

- Open a web browser and navigate to http://localhost:9200 to access the Elasticsearch HTTP endpoint.
- Open a web browser and navigate to http://localhost:5601 to access the Kibana web interface.

3. **Stopping the Services**
To stop the services, run:

docker-compose down