pipeline {
    agent any

    environment {
        gpg_secret = credentials("gpg-secret")
        gpg_trust = credentials("gpg-ownertrust")
    }

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

        stage("Add credentials") {

            steps {
                sh '''
                    gpg --batch --import $gpg_secret
                    gpg --import-ownertrust $gpg_trust
                '''
            }
        }

        stage("build app") {

            steps {
                sh '''
                    git secret reveal -v
                    docker compose build
                    docker compose up -d
                '''
            }
        }
    }
}