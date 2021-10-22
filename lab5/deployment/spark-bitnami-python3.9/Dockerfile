FROM bitnami/python:3.9.0 as build

FROM bitnami/spark:3.1.1

COPY --from=build /opt/bitnami/python/ /opt/bitnami/python/