.ONESHELL:

run-app:
	@ UNIX_SOCKET=/var/run/docker.sock uvicorn gauntry:app --host 0.0.0.0 --port 20001 --loop uvloop