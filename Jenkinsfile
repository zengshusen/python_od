#!/user/bin/env groovy
@Library('jenkins-shared-library') _


pipeline {
    agent any
    tools {
        maven 'maven-3.9'
    }
    stages{
        stage("init"){
            steps{
                script{
                    gv=load "script.groovy"
                    
                }
            }
        }
    }
    stages {
        stage("build jar") {
            steps {
                script {
                   buildJar()
                }
            }
        }
        stage("build image") {
            steps {
                script {
                    buildImage()
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
