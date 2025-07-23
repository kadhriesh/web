pipeline {
    agent any
    environment {
        IMAGE_NAME = "web-app"
        GIT_URL = "https://github.com/kadhriesh/web.git"
    }
    stages {
        stage('Clone Repo') {
            steps {
                git url: "${GIT_URL}"
            }
        }
        stage('Build Image with Buildpacks') {
            steps {
                sh 'pack build ${IMAGE_NAME} --path .'
            }
        }
        stage('Run Image') {
            steps {
                sh 'docker run -d --name web-app-container ${IMAGE_NAME}'
            }
        }
    }
}