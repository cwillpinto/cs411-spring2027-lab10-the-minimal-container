# TODO: replace this single-stage/root image with a named builder stage and a
# minimal runtime stage. Copy only the compiled binary and set a non-root USER.
FROM golang:1.25-alpine
WORKDIR /app
COPY . .
RUN go build -o /app/server .
EXPOSE 8080
ENTRYPOINT ["/app/server"]
