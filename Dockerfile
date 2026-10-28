# Intuition -- multi-stage build: install in a builder, ship only the
# installed package on a clean slim runtime. Pure stdlib, no build deps.
FROM python:3.12-slim AS builder
WORKDIR /build
COPY pyproject.toml README.md ./
COPY src ./src
RUN pip install --no-cache-dir --prefix=/install .

FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
WORKDIR /app
COPY --from=builder /install /usr/local
RUN useradd --create-home intuition
USER intuition
HEALTHCHECK --interval=30s --timeout=5s \
    CMD python -c "import intuition" || exit 1
ENTRYPOINT ["intuition"]
CMD ["list"]
