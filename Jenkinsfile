pipeline {
    agent any

    parameters {
        booleanParam(name: 'buildImage', defaultValue: false, description: 'Build docker image?')
        booleanParam(name: 'destroy', defaultValue: false, description: 'Destroy Terraform build?')
    }

    environment {
        dockerhub=credentials('dockerhub')
        AWS_ACCESS_KEY_ID=credentials('aws_access_key_id')
        AWS_SECRET_ACCESS_KEY=credentials('aws_secret_access_key')
    }

    stages {

        stage("verify tooling") {
            
            steps {
                sh '''
                    docker version
                    docker info
                    terraform -help
                    ansible --version
                '''
            }
        }

        stage("build docker image") {

            when {
                equals expected: true, actual: params.buildImage
            }

            steps {
                sh '''
                    docker build -t jpmontoya19/cisco_demo:flask-app .
                '''
            }
        }

        stage("push image to docker-hub") {

            when {
                equals expected: true, actual: params.buildImage
            }

            steps {
                sh '''
                    echo $dockerhub_PSW | docker login -u $dockerhub_USR --password-stdin
                    docker push jpmontoya19/cisco_demo:flask-app
                '''
            }
        }

        stage("initialize terraform") {
            
            steps {
                dir('terraform') {
                    sh "terraform init"
                }
            }
        }

        stage("plan infrastructure") {

            when {
                not {
                    equals expected: true, actual: params.destroy
                }
            }

            steps {
                dir('terraform') {
                    sh '''
                        terraform plan
                    '''
                }
            }
        }

        stage("build infrastructure") {

            when {
                not {
                    equals expected: true, actual: params.destroy
                }
            }

            steps {
                dir('terraform') {
                    sh "terraform apply --auto-approve"
                }
            }
        }

        stage("Use ansible") {
            when {
                not {
                    equals expected: true, actual: params.destroy
                }
            }

            steps {
                dir('ansible') {
                    withCredentials([[
                        $class: 'AmazonWebServicesCredentialsBinding', 
                        credentialsId:'aws_credentials', 
                        accessKeyVariable: 'AWS_ACCESS_KEY', 
                        secretKeyVariable: 'AWS_SECRET_KEY'
                    ]]) {

                        ansiblePlaybook(
                            credentialsId: 'aws_ec2_key',
                            disableHostKeyChecking: true, 
                            installation: 'ansible', 
                            inventory: 'aws_ec2.yml',
                            playbook: 'playbook.yml',
                            extraVars: [
                                aws_access_key: [value: '${AWS_ACCESS_KEY_ID}', hidden: true],
                                aws_secret_key: [value: '${AWS_SECRET_ACCESS_KEY}', hidden: true]
                            ]
                        )
                    }
                }
            }
        }

        stage("destroy infrastructure") {
            when {
                equals expected: true, actual: params.destroy
            }

            steps {
                dir('terraform') {
                    sh "terraform destroy --auto-approve"
                }
            }
        }
    }
}