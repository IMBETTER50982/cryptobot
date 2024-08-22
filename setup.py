from setuptools import setup


# Requirements used for submodules
plot = ["plotly>=4.0"]
hyperopt = [
    "scipy",
    "scikit-learn",
    "ft-scikit-optimize>=0.9.2",
    "filelock",
]

freqai = [
    "scikit-learn",
    "joblib",
    'catboost; platform_machine != "aarch64"',
    "lightgbm",
    "xgboost",
    "tensorboard",
    "datasieve>=0.1.5",
]

freqai_rl = [
    "torch",
    "gymnasium",
    "stable-baselines3",
    "sb3-contrib",
    "tqdm",
]

hdf5 = [
    "tables",
    "blosc",
]

develop = [
    "coveralls",
    "isort",
    "mypy",
    "pre-commit",
    "pytest-asyncio",
    "pytest-cov",
    "pytest-mock",
    "pytest-random-order",
    "pytest",
    "ruff",
    "time-machine",
    "types-cachetools",
    "types-filelock",
    "types-python-dateutil" "types-requests",
    "types-tabulate",
]

jupyter = [
    "jupyter",
    "nbstripout",
    "ipykernel",
    "nbconvert",
]

all_extra = plot + develop + jupyter + hyperopt + hdf5 + freqai + freqai_rl

setup(
    tests_require=[
        "pytest",
        "pytest-asyncio",
        "pytest-cov",
        "pytest-mock",
    ],
    install_requires=[
        # from requirements.txt
        "ccxt>=4.3.24",
        "SQLAlchemy>=2.0.6",
        "python-telegram-bot>=20.1",
        "humanize>=4.0.0",
        "cachetools",
        "requests",
        "httpx>=0.24.1",
        "urllib3",
        "jsonschema",
        "numpy<2.0",
        "pandas>=2.2.0,<3.0",
        "TA-Lib",
        "pandas-ta",
        "technical",
        "tabulate",
        "pycoingecko",
        "py_find_1st",
        "python-rapidjson",
        "orjson",
        "jinja2",
        "questionary",
        "prompt-toolkit",
        "joblib>=1.2.0",
        "rich",
        'pyarrow; platform_machine != "armv7l"',
        "fastapi",
        "pydantic>=2.2.0",
        "pyjwt",
        "websockets",
        "uvicorn",
        "psutil",
        "schedule",
        "janus",
        "ast-comments",
        "aiofiles",
        "aiohttp",
        "cryptography",
        "sdnotify",
        "python-dateutil",
        "pytz",
        "packaging",
        "freqtrade-client",
    ],
    extras_require={
        "dev": all_extra,
        "plot": plot,
        "jupyter": jupyter,
        "hyperopt": hyperopt,
        "hdf5": hdf5,
        "freqai": freqai,
        "freqai_rl": freqai_rl,
        "all": all_extra,
    },
    url="https://github.com/freqtrade/freqtrade",
)
