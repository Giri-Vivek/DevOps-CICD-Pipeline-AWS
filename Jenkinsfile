stage('Deploy to EC2') {
    steps {
        sh '''
        ssh -i /var/jenkins_home/myserverkey.pem -o StrictHostKeyChecking=no ubuntu@54.91.228.247 "
        docker pull girivivek686/flask-cicd-app:v1 &&
        docker stop flask-app || true &&
        docker rm flask-app || true &&
        docker run -d -p 5000:5000 --name flask-app girivivek686/flask-cicd-app:v1
        "
        '''
    }
}
