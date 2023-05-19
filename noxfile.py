from nox import Session
from nox_poetry import session


@session(venv_backend="none")
def fmt(s: Session) -> None:
    s.run("ruff", "check", ".", "--fix")
    s.run("black", ".")


@session(venv_backend="none")
def generate_requirements_txt(s: Session) -> None:
    s.run("poetry", "export", "-f", "requirements.txt", "--output", "requirements.txt")


@session(venv_backend="none")
def test(s: Session) -> None:
    s.run("python", "-m", "pytest", "test", *s.posargs)


@session(venv_backend="none")
def type_check(s: Session) -> None:
    s.run("python", "-m", "mypy", "src", "test")
