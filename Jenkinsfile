pipeline{
    agent any 
    environment {
        SONAR_PROJECT_KEY = 'ai-agent-llmops'
        SONAR_SCANNER_HOME = tool 'sonar-qube-scanner'
        // AWS_SESSION = "us-east-1"
        // ECR_REPO = "ai-agent-repo"
        // IMAGE_TAG = "latest"
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
}
}