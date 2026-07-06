import app

def test_cloud_app():
    try:
        app.run_app()
        assert True
    except Exception as e:
        assert False, f"Crashed: {e}"
# trigger pipeline update