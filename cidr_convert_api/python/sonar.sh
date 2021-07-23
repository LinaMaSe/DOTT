sonar-scanner \
  -Dsonar.projectKey=codeAnalysis \
  -Dsonar.sources=. \
  -Dsonar.host.url=http:18.117.184.134:9000 \
  -Dsonar.login=f73e0ac4d8aaf4fdd588047144df5ce03f04b06c
  -Dorg.jenkinsci.plugins.durabletask.BourneShellScript.HEARTBEAT_CHECK_INTERVAL=86400
