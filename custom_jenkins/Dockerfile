FROM jenkins/jenkins:lts
USER root

# Install Docker CLI only (simpler & supported)
RUN apt-get update -y && \
    apt-get install -y docker.io && \
    groupadd -f docker && \
    usermod -aG docker jenkins && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

USER jenkins    