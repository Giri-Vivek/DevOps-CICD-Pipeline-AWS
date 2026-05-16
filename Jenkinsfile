pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "girivivek686/flask-cicd-app"
        DOCKER_TAG = "v1"
        EC2_HOST = "54.91.228.247"
        EC2_USER = "ubuntu"
        SSH_KEY = "/var/jenkins_home/myserverkey.pem"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Giri-Vivek/DevOps-CICD-Pipeline-AWS.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .
                """
            }
        }

        stage('Login to DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub',
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS'
                )]) {
                    sh """
                    echo \$PASS | docker login -u \$USER --password-stdin
                    """
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh """
                docker push ${DOCKER_IMAGE}:${DOCKER_TAG}
                """
            }
        }

        stage('Deploy to EC2') {
            steps {
                sh """
                chmod 400 ${SSH_KEY}

                ssh -o StrictHostKeyChecking=no -i ${SSH_KEY} ${EC2_USER}@${EC2_HOST} '
                    docker pull ${DOCKER_IMAGE}:${DOCKER_TAG} &&
                    docker stop flask-app || true &&
                    docker rm flask-app || true &&
                    docker run -d -p 5000:5000 --name flask-app ${DOCKER_IMAGE}:${DOCKER_TAG}
                '
                """
            }
        }
    }

    post {
        success {
            echo " Deployment Successful! App is running."
        }
        failure {
            echo " Pipeline Failed. Check logs."
        }
    }
}
