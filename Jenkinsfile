pipeline {
    agent any

    environment {
        dockerhub=credentials('dockerhub')
    }

    stages {

        stage("verify tooling") {
            
            steps {
                sh '''
                    docker version
                    docker info
                '''
            }
        }

        stage("build docker image") {

            steps {
                sh '''
                    docker build -t jpmontoya19/cisco_demo:flask-app .
                '''
            }
        }

        stage("push docker image to docker-hub") {

            steps {
                sh '''
                    echo $dockerhub_PSW | docker login -u $dockerhub_USR --password-stdin
                    docker push jpmontoya19/devopslab_ci:flask-app
                '''
            }
        }
    }
}