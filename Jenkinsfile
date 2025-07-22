pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }
    stages{
        stage("Cloning from Github....."){
            steps{
                script{
                    echo 'Cloning from Github.....'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/saksham011023/Anime-Recommendor_System.git']])
                }
            }
        }
        stage("Making a virtual environment..."){
            steps{
                script{
                    echo 'Making a virtual environment...'
                    sh '''
                    rm -rf ${VENV_DIR}
                        
                        # Try using venv first, fallback to virtualenv if needed
                    if python -m venv ${VENV_DIR} 2>/dev/null; then
                        echo "Using python venv"
                    else
                        echo "venv failed, trying virtualenv"
                        python -m pip install --user virtualenv
                        python -m virtualenv ${VENV_DIR}
                    fi
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    pip install dvc
                    '''
            }
        }
    }
        stage('DVC Pull'){
            steps{
                withCredentials([file(credentialsId:'gcp-key',variable: 'GOOGLE_APPLICATION_CREDENTIALS')]){
                   script{
                    echo 'DVC Pull...'
                    sh '''
                    . ${VENV_DIR}/bin/activate
                    dvc pull
                    '''
                   } 
                }
            }
        }
    }
}