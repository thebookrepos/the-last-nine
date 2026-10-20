# Contributing

Thank you for helping improve *The Last Nine*. This guide keeps reviews quick.

## Before you start

- For a mistake in the book, open an **Erratum** issue first. A pull request is not needed.
- For a large change, open an issue to discuss it before you write the code.

## Pull requests

1. Fork the repository and create a branch from `main`.
2. Keep one change per pull request.
3. Put new material in the folder of the chapter it belongs to. Name files `NN-short-description.ext`, continuing the numbering in that folder.
4. Add a row for the new file to that folder's README.
5. Say which tool versions you tested against.
6. Check that the file parses. Run `python3 -m py_compile` for Python and a YAML linter for YAML.
7. Remove anything private: hostnames, account IDs, customer data and internal URLs.

## Style

- Keep listings short and runnable. A listing teaches one idea.
- Comments explain why, not what.
- Use the checkout example from the book where it fits, so readers can follow along.

## Code of conduct

Be respectful and assume good intent. Critique the work, not the person. The maintainer may close issues or pull requests that do not follow this.

By contributing, you agree that your contribution is released under the MIT License.
