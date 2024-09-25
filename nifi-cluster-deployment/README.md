# Docker Compose Setup for Nginx, NiFi, and Zookeeper

This directory provides a Docker Compose configuration to set up an environment with Nginx, NiFi, and Zookeeper. The configuration ensures that Nginx serves as a reverse proxy to NiFi and that Zookeeper is used as a coordination service.

## Services

### 1. Nginx

- **Image**: `nginx`
- **Exposed Ports**: 8080, 9092
- **Dependencies**: NiFi
- **Configuration**:
  - The proxy configuration is defined in `./conf/proxy.conf` which is mounted to the container at `/etc/nginx/conf.d/proxy.conf`.

### 2. Zookeeper

- **Image**: `bitnami/zookeeper:latest`
- **Exposed Ports**: 2181
- **Environment**: 
  - `ALLOW_ANONYMOUS_LOGIN=yes`

### 3. NiFi

- **Image**: `apache/nifi:latest`
- **Dependencies**: Zookeeper
- **Replicas**: 1
- **Exposed Ports**: 8080, 8083
- **Environment**:
  - `NIFI_WEB_HTTP_PORT=8080`
  - `NIFI_CLUSTER_IS_NODE=true`
  - `NIFI_CLUSTER_NODE_PROTOCOL_PORT=8082`
  - `NIFI_ZK_CONNECT_STRING=zookeeper:2181`
  - `NIFI_ELECTION_MAX_WAIT=1 min`
  - `NIFI_SENSITIVE_PROPS_KEY=3e38a10eb5fb`

## Getting Started

### Prerequisites

Ensure that you have Docker and Docker Compose installed on your machine.

### Configuration

1. **Nginx Proxy Configuration**:
   - Nginx proxy conf is in a directory named `conf` in the nifi-training/nifi-cluster-deployment directory

### Deploying the Stack

To deploy the stack using Docker Compose, navigate to the root directory of your project and run:


`docker-compose up -d`