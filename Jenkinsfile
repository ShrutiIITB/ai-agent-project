pipeline{
    agent any 
    environment {
        SONAR_PROJECT_KEY = 'ai-agent-llmops'
        SONAR_SCANNER_HOME = tool 'sonar-qube-scanner'
        DOCKER_IMAGE = 'technologia111/my-ai-agent:latest'
        }


    stages{
        stage('Cloning Github Repo to Jenkins'){
            steps{
                script{
                    echo "Cloning the repository..."
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/ShrutiIITB/ai-agent-project.git']])
                }
            }
        }

        stage('SonarQube Analysis'){
            steps{
                withCredentials([string(credentialsId: 'sonar-qube-token', variable: 'SONAR_TOKEN')]){
                    
                    // name of the scanner in system 
                
                    sh """
                    ${SONAR_SCANNER_HOME}/bin/sonar-scanner \
                    -Dsonar.projectKey=${SONAR_PROJECT_KEY} \
                    -Dsonar.sources=. \
                    -Dsonar.host.url=http://sonarqube-dind:9000 \
                    -Dsonar.login=${SONAR_TOKEN}
                    """
                    
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    docker.withRegistry(
                        'https://index.docker.io/v1/', 
                        'docker-hub-registry'
                    ){
                        def image = docker.build(DOCKER_IMAGE)
                        image.push()
                    }
                    
                }
            }
    
        }
    }
        
    
}
        
