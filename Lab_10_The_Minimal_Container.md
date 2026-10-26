# Lab 10: The Minimal Container

**CS 411: Computing Paradigms - Spring 2027**  
**Week 13: April 5-11, 2027**  
**Due:** April 11, 2027  
**Value:** 100 points

## Purpose

Package the supplied service with a multi-stage Docker build. Keep compilers, caches, credentials, and source history out of the runtime image, then run the service as a non-root user.

## Learning objectives

- Distinguish images from containers
- Use reusable image layers
- Reduce runtime contents and privileges

## Before you begin

1. Review the Week 13 slide deck and assigned VoiceThread or reading.
2. Create your own repository from the Spring 2027 template linked in Blackboard. The Go `/health` service is complete; the single-stage, root-running `Dockerfile` and incomplete `.dockerignore` are intentional TODOs.
3. Run `go test ./...` and `python verify_image.py` before editing. Save the static-check failures in `Lab10_Terminal.txt`. You need a running Docker engine for the later build and runtime evidence.

## Part A Image design (25 points)

Explain the boundary before building.

- In `Lab10_Analysis.md` or PDF, identify Go source, compiler, module cache, repository history, local outputs, and possible credential files as builder-only or excluded artifacts.
- Describe the runtime process, `/health` endpoint, and container port 8080. Distinguish the immutable image from a running container instance.
- Draw the intended build stages and predict which changes invalidate the module-download layer versus only the source-compile layer.

## Part B Multi-stage build (45 points)

Create a reproducible image.

- Replace the starter `Dockerfile` with a named `builder` stage that caches module dependencies before copying source, then builds a Linux binary with `CGO_ENABLED=0`.
- Use a minimal runtime stage containing only that compiled binary. Copy it with `COPY --from=builder`; do not copy source, compilers, caches, or credentials into the runtime image.
- Set an explicit non-root `USER`, `EXPOSE 8080`, and an explicit `ENTRYPOINT`. Complete `.dockerignore` to exclude `.git`, credential files such as `.env`, local outputs, and unneeded handouts. Run `python verify_image.py` again.

## Part C Inspect and verify (30 points)

Collect evidence from the built image.

- Build with `docker build -t cs411-lab10 .`. Save `docker image history cs411-lab10` and the image size from `docker image inspect cs411-lab10` in `Lab10_Image_History.txt`.
- Start a disposable container with `docker run --rm -d --name cs411-lab10-check -p 18080:8080 cs411-lab10`. Request `http://localhost:18080/health` and record HTTP 200 and body `ok`.
- Record `docker image inspect -f '{{.Config.User}}' cs411-lab10` and `docker top cs411-lab10-check`, then stop it with `docker stop cs411-lab10-check`. Capture all commands/output in `Lab10_Terminal.txt`.

## Verification

- `go test ./...` and `python verify_image.py` pass.
- `docker build -t cs411-lab10 .` succeeds and the runtime image contains only the binary and minimal base contents.
- The health endpoint returns HTTP 200, and image inspection reports a non-root user.

## What to submit

Submit your own repository URL and:

1. Your own repository URL (created from the Spring 2027 template).
2. `Dockerfile` and `.dockerignore` in that repository.
3. `Lab10_Analysis.pdf` or `Lab10_Analysis.md`.
4. `Lab10_Image_History.txt` and `Lab10_Terminal.txt`.

## Rubric

| Criterion | Points |
| --- | ---: |
| Image design explanation | 20 |
| Correct multi-stage build | 35 |
| Minimal runtime and non-root execution | 20 |
| Health and inspection evidence | 15 |
| Layer-cache analysis | 10 |
| **Total** | **100** |

## AI usage and academic integrity

Add an **AI Usage** section to the required analysis file. Name each tool and list the prompts or interactions that affected the work. If you did not use AI, write `AI Usage: None.` You must be able to explain and defend every submitted design and line of code.

## Late work

Late work may be accepted for up to three calendar days with a 25 percent deduction per day, following the course syllabus.
