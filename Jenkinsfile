pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building application'
                sh 'python3 --version'
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated tests'
                sh 'pytest -v'
            }
        }

        stage('Package') {
            steps {
                echo 'Creating build artifact'
                sh 'echo "Application packaged successfully" > build-info.txt'
                archiveArtifacts artifacts: 'build-info.txt', fingerprint: true
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment stage completed'
            }
        }
    }
}
