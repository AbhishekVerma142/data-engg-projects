build_docker_image:
	docker build -t fast .

run_docker_image:
	docker run -e PORT=8000 fast

push_docker_image:
	docker push $_

deploy_docker_image:
	gcloud run deploy fast-app --image europe-west1-docker.pkg.dev/wagon-bootcamp-424410/docker-hub/fast:0.2 --region=europe-west1 --allow-unauthenticated

lint_dockerfile:
	docker run --rm -i hadolint/hadolint < Dockerfile

commit_message:
	git commit -m"Updates"

github_push:
	git push origin master
