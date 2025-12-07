
import os
import asyncio
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.sdk.trace.export.in_memory_span_exporter import InMemorySpanExporter

# Setup OTel to capture spans in memory
exporter = InMemorySpanExporter()
provider = TracerProvider()
processor = SimpleSpanProcessor(exporter)
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

# Mock env vars - Enable standard tracing to see if it works + errors
os.environ["LANGSMITH_OTEL_ENABLED"] = "true"
os.environ["LANGSMITH_TRACING"] = "true"
# os.environ["LANGCHAIN_TRACING_V2"] = "false"
# os.environ["LANGCHAIN_API_KEY"] = "dummy" # Unset to simulate user state

# Import LangChain after env vars
from langchain_core.runnables import RunnableLambda

def test_func(x):
    return x + 1

chain = RunnableLambda(test_func)
chain.invoke(1)

# Check spans
spans = exporter.get_finished_spans()
print(f"Spans captured: {len(spans)}")
if len(spans) > 0:
    for span in spans:
        print(f"Span: {span.name}")
