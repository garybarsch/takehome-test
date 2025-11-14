# takehome

## Goals

- Pass all pytests.
- Achieve 100% test coverage.

## Instructions

1. Extract takehome-project.zip
2. Enter the `takehome-project/` directory and initialize a new git repository
   within the directory.
3. Add/import all extracted files to git and create an initial commit.
4. Examine the code in `src/` and `tests/`
5. Update the `src/` files until all tests pass and coverage is 100%.
6. **Make sure to commit frequently (after every fix).**

## Testing

To run all of the tests:

```bash
uv run pytest
uv run pytest --cov=takehome
```

To run specific tests and coverage at the same time:

```bash
uv run pytest --cov=takehome.inventory tests/test_inventory.py
```

## Results

Once the goal or time limit has been reached, bundle up the repository and send a
copy to the provided email:

```bash
git bundle create takehome.bundle --all
```

## References

- [uv](https://docs.astral.sh/uv/)
