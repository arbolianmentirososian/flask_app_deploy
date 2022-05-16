pipeline {
    agent any
    environment {
        GIT_EMAIL = sh(script: "git show -s --format='%ae' HEAD | tr -d '\n'", returnStdout: true)
        DOCKERFILE_EXISTS = fileExists 'Dockerfile'
    }
    options {
	    buildDiscarder(logRotator(artifactNumToKeepStr: '7'))
	}
    stages {
        stage('Build') {
            steps {
                script {
                    COMMIT_HASH = sh(script: "git rev-parse HEAD", returnStdout: true, ).trim()
                    VERSION = sh(script: "python3 -c 'import version; print(version.__version__)'", returnStdout: true).trim()
                    if (fileExists('ci-build.sh')) {
                        sh 'bash ./ci-build.sh PREPROD'
                    } else {
                        echo 'ci-build.sh not found - skipping this stage'
                    }
                }
            }
        }
        stage('Unit Tests') {
            steps {
                lock('lock_test') {
                    script {
                    sh """#!/bin/bash
                        python3 -m venv venv
                        source ./venv/bin/activate
                        pip install -r requirements.txt
                        pip install pytest pytest-cov
                        pytest --cov=src/ --cov-report=xml:test/coverage.xml --junitxml=test/results.xml
                    """
                    }
                }
                junit(testResults: 'test/results.xml', allowEmptyResults: true)
            }
        }
        stage('Generating docs') {
            steps {
                script {
                    sh """#!/bin/bash
                        pip install pdoc3
                        pip install -r requirements.txt
                        mkdir -p docs/
                        find docs -maxdepth 1 -type f -delete
                        if [[ -f "generate_docs.sh" ]]; then
                            ./generate_docs.sh
                        else
                            pdoc --pdf --force --output-dir docs/ src/app > docs/result.md
                        fi
                        pandoc -f markdown -t html5 --metadata title="Flask_App_Deploy" --template=docs/templates/template.html5 --toc docs/result.md -o docs/index.html
                    """
                }
                publishHTML target: [
					allowMissing: true,
					alwaysLinkToLastBuild: false,
					keepAll: true,
					reportDir: 'docs/',
					reportFiles: 'index.html',
					reportName: 'apidoc'
			    ]
            }
        }
        stage('Static analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh """
                        ${tool("SonarQubeScanner")}/bin/sonar-scanner \
                            -D sonar.projectKey="Flask_App_Deploy" \
                            -D sonar.projectName="Flask_App_Deploy" \
                            -D sonar.projectVersion=${VERSION} \
                            -D sonar.sources=src/ \
                            -D sonar.tests=test/ \
                            -D sonar.python.coverage.reportPaths=test/coverage.xml \
                            -D sonar.python.xunit.reportPath=test/result.xml
                    """
                }
                timeout(time: 1, unit: 'HOURS') {
                    waitForQualityGate abortPipeline: false
                }
            }
        }
    }
}