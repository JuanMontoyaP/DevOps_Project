pipeline {
    agent none

    environment {
        gpg_secret = credentials("gpg-secret")
        gpg_trust = credentials("gpg-ownertrust")
    }

    stages {

        stage("verify tooling") {

            agent any
            
            steps {
                sh '''
                    docker version
                    docker info
                '''
            }
        }

        stage("Add credentials") {

            agent any

            steps {
                sh '''
                    gpg --batch --import $gpg_secret
                    gpg --import-ownertrust $gpg_trust
                '''
            }
        }

        stage("reveal app secrets") {

            agent any

            steps {
                sh '''
                    git secret reveal -f
                '''
            }
        }

        stage("build docker image") {

            agent {
                
                dockerfile {
                    filename "Dockerfile"
                    additionalBuildArgs "-t jpmontoya19/cisco_demo"
                }

            }

            steps {
                sh '''
                    python --version
                '''
            }
        }
    }
}