pipeline {
    agent any

    stages {

        stage("verify tooling") {
            
            steps {
                sh '''
                    docker version
                    docker info
                    docker compose version
                '''
            }
        }

        stage("build app") {

            steps {
                sh '''
                    docker-compose build
                    docker-compose up -d
                '''
            }
        }
    }
}