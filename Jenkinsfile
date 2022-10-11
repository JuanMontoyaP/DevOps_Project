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