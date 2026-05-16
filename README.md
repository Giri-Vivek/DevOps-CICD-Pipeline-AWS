This project demonstrates a fully automated CI/CD pipeline using Jenkins, Docker, GitHub, and AWS EC2. 
The pipeline automates code integration, builds a Docker image, pushes it to DockerHub, and deploys the application on an EC2 instance.

Project Structure
DevOps-CICD-Pipeline-AWS/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
└── README.md

CI/CD Pipeline Flow
GitHub → Jenkins → Docker Build → DockerHub → AWS EC2 → Flask App Running.

"Tech Stack"
Python (Flask)
Docker
Jenkins (CI/CD Automation)
Git & GitHub
AWS EC2 (Ubuntu)
DockerHub

Checkout Code
Jenkins pulls latest code from GitHub.

Build Docker Image
docker build -t flask-cicd-app:v1 .

Push to DockerHub
docker push girivivek686/flask-cicd-app:v1

Deploy to EC2
"""docker pull girivivek686/flask-cicd-app:v1
docker stop flask-app || true
docker rm flask-app || true
docker run -d -p 5000:5000 --name flask-app girivivek686/flask-cicd-app:v1"""

Application Access
"""
    http://<EC2-PUBLIC-IP>:5000
    http://54.91.228.247:5000
  
"""

Key Configurations
Jenkins Plugins
  Git Plugin
  Pipeline Plugin
  Docker Pipeline
  SSH Agent Plugin
  
Required Credentials
  DockerHub login
  EC2 SSH Key
  
AWS Security Groups
  22 → SSH
  8080 → Jenkins
  5000 → Flask App


Key Features

✔ End-to-end CI/CD automation
✔ Docker containerization
✔ Jenkins pipeline as code
✔ AWS EC2 deployment
✔ GitHub integration
✔ DockerHub image registry

Author
    Vivek Giri
    GitHub: https://github.com/Giri-Vivek
    DockerHub: https://hub.docker.com/u/girivivek686
