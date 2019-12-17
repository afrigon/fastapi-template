# Fast API Template

This is a template project to build api using the [FastAPI](https://github.com/tiangolo/fastapi) library.

## Start the application

The run script will start the app with the `DEBUG` flag turned on.

```sh
make run
```

### Dockerfile

The project can be started in production mode using docker-compose

```sh
docker-compose up --build
```

## Documentation

FastAPI project are self documenting, visit`/docs`.

## Code Quality

### Tests

`pytest` is used for testing.

```sh
make test
```

### Lint

`flake8` is used for linting.

```sh
make lint
```

### Coverage

The coverage script will create an html file in `./htmlcov` and output a minimal report.

```sh
make coverage
```

## License

FastAPI-template is MIT licensed.

