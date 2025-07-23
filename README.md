# web

# https://testomat.io/blog/popular-python-libraries-to-make-python-testing-more-efficient/

pack build my-app --builder paketobuildpacks/builder:base \
--buildpack paketobuildpacks/python:latest \
--buildpack paketobuildpacks/poetry:latest \
--pull-policy never