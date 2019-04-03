from setuptools import setup

setup(
    name="sphinx-codio-theme",
    description="Sphinx Codio Theme.",
    author="LaunchCode",
    author_email="education@launchcode.org",
    install_requires=[
        "setuptools",
    ],
    entry_points={
        'sphinx.html_themes': [
            'codio = sphinx_codio_theme',
        ]
    }
)
