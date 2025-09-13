# deb-pkg-init

`deb-pkg-init` is a Python wrapper for the `dh_make` tool, used to generate the template files necessary for creating Debian packages. The script prompts the user to input essential environment variables (`DEBEMAIL` and `DEBFULLNAME`), as well as the package version, and automatically runs `dh_make` with the current directory's name and version.

## Features

- Prompts the user to enter `DEBEMAIL`, `DEBFULLNAME`, and package version.
- Automatically retrieves the current directory's basename to form the package name.
- Executes `dh_make` with the `-p` option to generate Debian package templates.
- Checks if `dh_make` is installed, and exits with an error if not.

## Prerequisites

- Python 3.x
- `dh_make` installed on the system

To install `dh_make`, run:

```bash
$ sudo apt install dh-make
```

## Usage

1. Run the script:

```bash
$ deb-pkg-init.py
```

2. You will be prompted to enter your `DEBEMAIL`, `DEBFULLNAME`, and the package version (e.g., `1.0`).

3. The script will automatically execute `dh_make` using the basename of the current directory and the specified version to create the necessary Debian packaging template.

### Example:

```bash
$ deb-pkg-init.py
Enter DEBEMAIL: your.email@example.com
Enter DEBFULLNAME: Your Full Name
Enter package version (e.g., 1.0): 1.0
Type of package: (single, indep, library, python)
[s/i/l/p]? s
Maintainer Name     : Your Full Name
Email-Address       : your.email@example.com
Date                : Wed, 25 Sep 2024 09:50:15 +0900
Package Name        : my-package
Version             : 1.0
License             : blank
Package Type        : single
Are the details correct? [Y/n/q] Y
Currently there is not top level Makefile. This may require additional tuning
Done. Please edit the files in the debian/ subdirectory now.

```

In this example, the script runs the `dh_make` command and generates a Debian package template for a package named `my-package` with version `1.0`.

## License

This project is licensed under the [MIT License](./LICENSE).
