# Event-Driven Architecture Demo: Food Supermarket

This repository contains a demo of an event-driven architecture for a food supermarket. The architecture includes two microservices: `orders-microservice` and `inventory-microservice`. These services communicate via a locally running Kafka cluster, which is managed by Docker Compose.

## Microservices Overview

- **orders-microservice**: Handles customer orders, publishes events to Kafka.
- **inventory-microservice**: Subscribes to order events, updates inventory based on orders.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Running the Demo

1. Clone this repository:
   ```bash
   git clone https://github.com/Princeigwe/kafka-EDA-demo.git
   cd kafka-EDA-demo
