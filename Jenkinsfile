pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Getting website source code'
                sh 'ls -la'
            }
        }

        stage('Test') {
            steps {
                echo 'Running website tests'
                sh 'python3 -m unittest discover -s tests -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image'

                sh '''
                    docker build -t swathi-devops-website:latest .
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying website'

                sh '''
                    docker rm -f swathi-website || true

                    docker run -d \
                    --name swathi-website \
                    -p 8081:80 \
                    swathi-devops-website:latest
                '''
            }
        }

        stage('Verify') {
            steps {
                echo 'Checking website deployment'

                sh '''
                    python3 -c "import urllib.request; print(urllib.request.urlopen('http://docker:8081').status)"
                '''
            }
        }
    }
}