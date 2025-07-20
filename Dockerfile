FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

WORKDIR /app
ENV UV_LINK_MODE=copy
ENV PYTHONUNBUFFERED=1

ADD . /app

# Install deps (from lock file)
RUN uv sync --locked --no-install-project --no-dev
RUN uv sync --locked --no-dev

# Include .env
COPY .env /app/.env

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8080
ENTRYPOINT ["uv", "run", "adk", "web", "--host", "0.0.0.0", "--port", "8080"]
