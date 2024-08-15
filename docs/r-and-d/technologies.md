# Technologies

## Server Application and API Application

- possible choices (most popular and having experience)
  - Node.js
  - GoLang
  - Django

### Node.js

- Advantages
  - scalability
  - good and enomerous libraries and tools
  - fast for web tasks
- Disadvantages
  - performance
  - **time implementation overhead in many usecases**
  - **strange coding tricks required**

### GoLang

- Advantages
  - scalability
  - performance
  - simplicity
  - flexibility
  - concurrency
- Disadvantages
  - lack of libraries (because of being new language)
  - **time implementation overhead in many usecases**

### Django

- Advantages
  - **very easy and rapid development**
  - **ready to use apps and panels**
  - high-level abstractions
- Disadvantages
  - average performance
  - average scalability

## Log Management

- possible choices
  - Datadog
  - ELK (Elasticsearch) stack
  - Sentry

## Task Scheduling

- possible choices
  - Cronjob
  - Celery

### Cronjob

- Advantages
  - Simplicity: Cron jobs are straightforward to set up and manage, especially for simple, repetitive tasks.
  - Widely Supported: Almost every Unix-like operating system comes with cron support out of the box.
  - Flexibility: Offers a wide range of scheduling options, including minute-level granularity.

- Disadvantages
  - Limited to Server Environments: Primarily designed for server environments, making them less portable for client-side or mobile application scheduling.
  - Lack of Advanced Features: Does not support complex task dependencies or distributed processing.
  - Manual Configuration Required: Setting up cron jobs requires manual configuration, which can be error-prone if not done carefully.

### Celery

- Advantages
  - Asynchronous Processing: Tasks are executed asynchronously, allowing for faster response times and better utilization of resources.
  - Scalability: Can distribute tasks across multiple workers, scaling horizontally to handle increased load.
  - Integration: Easily integrates with Python frameworks like Django, Flask, and Pyramid, simplifying task management within these ecosystems.
- Disadvantages
  - Complexity: Setting up and configuring Celery can be complex, especially for beginners or small projects.
  - Resource Intensive: Each worker process consumes system resources, potentially leading to higher costs or slower performance on limited hardware.
  - Dependency on Message Brokers: Requires a message broker (RabbitMQ, Redis, etc.) to function, adding another component to manage.

## Real-Time Communication

- possible choices
  - WebRTC
  - MQTT
  - Websocket

### WebRTC

- Advantages
  - Peer-to-Peer Connectivity: Enables direct connection between peers without the need for intermediaries, reducing latency and improving efficiency.
  - Cross-Browser Compatibility: Works across major web browsers, facilitating broad adoption.
  - Rich Media Support: Supports audio, video, and data channels, enabling rich media experiences.
- Disadvantages
  - Complexity in Implementation: Implementing secure and efficient WebRTC connections can be challenging due to NAT traversal issues and security considerations.
  - Browser Limitations: While most modern browsers support WebRTC, older versions may not, limiting compatibility.
  - Requires Signaling Servers: Although WebRTC enables peer-to-peer communication, signaling servers are still needed to coordinate communication sessions, which adds complexity.

### MQTT

- Advantages
  - Low Bandwidth Usage: Designed for efficiency, MQTT uses very little bandwidth, making it ideal for remote locations or devices with limited connectivity.
  - Quality of Service (QoS): Offers three levels of QoS, ensuring reliable delivery of messages even over unreliable networks.
  - Broker-Based Architecture: Centralized message brokers simplify device management and message routing.

- Disadvantages
  - Limited to Text Messages: While MQTT supports binary payloads, it primarily handles text-based messages, which might limit its use for certain types of data transmission.
  - Dependent on Broker Availability: The entire system's reliability depends on the availability and performance of the MQTT broker.
  - Complexity in Scaling: As the number of clients increases, managing and distributing messages efficiently becomes more challenging.

### Websocket

- TODO
