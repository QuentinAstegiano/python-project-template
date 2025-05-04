# Use a Python image with uv pre-installed
FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim as build

# Install the project into `/app`
WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy

# Install the project's dependencies using the lockfile and settings
ADD pyproject.toml .
ADD uv.lock .
RUN uv sync --frozen --no-install-project --no-dev

# Then, add the rest of the project source code and install it
# Installing separately from its dependencies allows optimal layer caching
ADD src/main /app
RUN uv sync --frozen --no-dev

###############################################################################
FROM python:3.13-slim-bookworm

RUN groupadd -r app
RUN useradd -r -d /app -g app -N app

COPY --from=build --chown=app:app /app /app

USER app
WORKDIR /app

# Run the FastAPI application by default
CMD ["fastapi", "run", "--host", "0.0.0.0", "app.py"]
