pipeline {
    agent any
    tools {
        maven 'maven-3.9'
    }
    stages {
        stage("build jar") {
            steps {
                script {
                    buildJar()
                }
            }
        }
        stage("build and oush image") {
            steps {
                script {
                    buildIamge 'nanatwn/demo-app:jma-3.0'
                    dockerLogin()
                    dockerPush 'nanatwn/demo-app:jma-3.0'
                    }
                }
            }
        }
        stage("deploy") {
            steps {
                script {
                    echo "deploying the application..."
                }
            }
        }
    }
}
