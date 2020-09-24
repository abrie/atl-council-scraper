FROM python:3.8-alpine as base

FROM base as builder

RUN mkdir /install
WORKDIR /install

COPY requirements.txt /requirements.txt

RUN pip install --no-warn-script-location --prefix=/install -r /requirements.txt

# See https://stackoverflow.com/a/55757473/12429735
ENV USER=appuser
ENV UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    "${USER}"

FROM base

COPY --from=builder /install /usr/local
COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /etc/group /etc/group
COPY app /app

# Use unprivileged, non-root user.
USER appuser:appuser

WORKDIR /
ENTRYPOINT ["python", "-m", "app"]
