# Install dependencies

Preferably using a [virtual environment](https://docs.python.org/3/tutorial/venv.html), install the packages you need to run this simulation:

```shell
pip install -r requirements.txt
```

# Set environment variables

Export the following environment variables to configure your OTLP exporter:

```shell
export OTEL_EXPORTER_OTLP_ENDPOINT=https://otlp.nr-data.net:4317
export OTEL_EXPORTER_OTLP_HEADERS="api-key=<YOUR-LICENSE-KEY>"
```

> Note: This endpoint is for accounts based in the US. If you have an EU account, use https://otlp.eu01.nr-data.net:4317 instead. Also, don't forget to replace `<YOUR-LICENSE-KEY>` with your real [license key](https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/#ingest-license-key).

# Simulate your requests

Now that you've configured your environment, run the simulation:

```shell
python sim.py
```
