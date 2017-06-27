from invoke import task
from src.provider import app


@task
def test_consumer(ctx):
    """Runs the consumer pact tests"""
    ctx.run('pytest src')


@task
def test_provider(ctx):
    """Validate pact files against server"""
    import threading

    def run_provider():
        app.run('0.0.0.0', port=1234)

    provider = threading.Thread(target=run_provider, daemon=True)
    provider.start()
    ctx.run(
        'pact-verifier '
        '--provider-base-url=http://localhost:1234 '
        '--pact-urls=consumer-provider.json'
    )
