# import sys, random, py, pytest, os
# from app import app
# from xprocess import ProcessStarter

# @pytest.fixture
# def test_web_address(xprocess):
#     python_executable = sys.executable
#     app_file = py.path.local(__file__).dirpath("../app.py")
#     port = str(random.randint(4000, 4999))
#     class Starter(ProcessStarter):
#         env = {"PORT": port, "APP_ENV": "test", **os.environ}
#         pattern = "Running on http://"
#         args = [python_executable, app_file]

#     xprocess.ensure("flask_test_server", Starter)

#     yield f"localhost:{port}"

#     xprocess.getinfo("flask_test_server").terminate()
