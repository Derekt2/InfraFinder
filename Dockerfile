FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /opt

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

COPY ./infrafinder.py ./
COPY ./secrets.py ./

ENTRYPOINT ["uv", "run", "python", "-u", "infrafinder.py"]
