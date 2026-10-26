# CS411 Spring 2027 · Lab 10: The Minimal Container

Starter template: https://github.com/cwillpinto/cs411-spring2027-lab10-the-minimal-container

Read the included handout. The Go service is complete; your task is to replace the deliberately single-stage, root-running `Dockerfile` and incomplete `.dockerignore` with a minimal multi-stage image.

```sh
go test ./...
python verify_image.py
docker build -t cs411-lab10 .
docker run --rm -d --name cs411-lab10-check -p 18080:8080 cs411-lab10
```

Then request `http://localhost:18080/health`, inspect `docker image history cs411-lab10`, `docker image inspect cs411-lab10`, and `docker top cs411-lab10`. Stop the container with `docker stop cs411-lab10-check`. The unchanged starter passes Go tests but fails the public static image checks. Docker engine access is needed for build/runtime evidence.

## Work in your own GitHub repository

The instructor starter is an upstream source. Keep your completed work in a repository under your own GitHub account, then submit the repository URL and the evidence listed in the assignment handout through Blackboard.

If Blackboard links a template repository, choose **Use this template**, create the new repository under your account, and clone that new repository. Check `git remote -v` before pushing; `origin` must be your repository.

For a direct clone, first create an empty repository under your account. Replace the placeholders below with the starter link supplied in Blackboard and your own empty repository URL:

```sh
git clone https://github.com/cwillpinto/cs411-spring2027-lab10-the-minimal-container
cd <cloned-directory>
git remote rename origin upstream
git remote add origin <your-empty-repository-url>
git remote -v
git push -u origin HEAD
```

Commit and push your completed work to your own `origin`. Do not push to the instructor's upstream repository. Use the exact submission files and verification commands in the assignment handout.
