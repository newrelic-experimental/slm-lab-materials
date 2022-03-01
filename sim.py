from datetime import datetime, timezone, timedelta
from grpc import Compression
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
import random

# OpenTelemetry setup
provider = TracerProvider(
    resource=Resource.create({"service.name": "demo-service"})
)

processor = BatchSpanProcessor(
    OTLPSpanExporter(compression=Compression.Gzip)
)

provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

# Constants for controlling simulator
DAYS_BACK = 7
HOURS_BETWEEN_TRACES = int((DAYS_BACK * 24) / 20)

# Ticker for simulating past events
ticker = datetime.now(timezone.utc) - timedelta(days=7)

def timestamp():
    """Get a timestamp in the past"""
    global ticker

    millis = ticker.timestamp()
    ticker = ticker + timedelta(hours=HOURS_BETWEEN_TRACES)
    return millis

def now_yet():
    """Determine if the ticker has reached the current time"""
    return ticker.timestamp() >= datetime.now().timestamp()

def simulate():
    duration = int(random.randint(1, 10) * 1e9)
    start_time = int(timestamp() * 1e9)
    end_time = start_time + duration

    return start_time, end_time

def do_work():
    start_time, end_time = simulate()
    print(datetime.fromtimestamp(start_time / 1e9))
    print(datetime.fromtimestamp(end_time / 1e9))
    span = tracer.start_span("work", start_time=start_time)
    span.end(end_time=end_time)

while not now_yet():
    do_work()
