pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Getting source code from GitHub'
                checkout scm
                sh 'ls -la'
            }
        }

        stage('Automated Tests') {
            steps {
                echo 'Running website tests'
                sh 'python3 -m unittest discover -s tests -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building website Docker image'
                sh 'docker build -t swathi-devops-website:latest .'
            }
        }

        stage('Publish to Docker Hub') {
            steps {
                echo 'Publishing image to Docker Hub'

                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKERHUB_USERNAME',
                        passwordVariable: 'DOCKERHUB_TOKEN'
                    )
                ]) {
                    sh '''
                        set +x
                        echo "$DOCKERHUB_TOKEN" | docker login \
                            -u "$DOCKERHUB_USERNAME" --password-stdin

                        docker tag swathi-devops-website:latest \
                            "$DOCKERHUB_USERNAME/swathi-devops-website:latest"

                        docker push \
                            "$DOCKERHUB_USERNAME/swathi-devops-website:latest"

                        docker logout
                    '''
                }
            }
        }
    }
}
