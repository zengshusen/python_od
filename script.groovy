#!/user/bin/env groovy
library identifier: 'jenkins-shared-library@master',retriever:modeSCM(
    [$class:'GitSCMSource',
     remote:'https://github.com/zengshusen/jenkins-shared-library.git'
     credentialsId:'github-credentials'])
@library('jenkins-shared-library@2.0')
def buildApp() {
    echo 'building the application...'
}

def testApp() {
    echo 'testing the application...'
}

def deployApp() {
    echo 'deploying the application...'
    echo "deploying version ${params.VERSION}"
}

return this
