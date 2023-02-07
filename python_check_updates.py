#!/usr/bin/env python3
import pprint
from typing import Dict, List, Literal

import click
import requests
from packaging.requirements import Requirement
from packaging.version import Version

FormatTypeType = Literal["setup.py", "requirements.txt", "pypackage.toml", "dict"]


def get_package_names_from_requirements(requirements: List[str]) -> List[str]:
    return [Requirement(requirement).name for requirement in requirements]


def get_latest_versions(package_names: List[str]) -> Dict[str, Version]:
    versions = {}
    for package_name in package_names:
        versions[package_name] = latest_version(get_versions(package_name))
    return versions


def get_versions(package_name: str) -> List[Version]:
    resp = requests.get(f"https://pypi.org/pypi/{package_name}/json", timeout=10)
    releases_info = resp.json()["releases"]
    versions = [Version(v) for v in releases_info.keys()]
    versions.sort()
    return versions


def latest_version(versions: List[Version]) -> Version:
    return list(sorted(versions))[-1]


def format_dependencies(
    dependencies: Dict[str, Version], format_type: FormatTypeType
) -> str:
    if format_type == "requirements.txt":
        return (
            "[\n"
            + "\n".join(
                f'    "{name}=={str(version)}",'
                for name, version in dependencies.items()
            )
            + "\n]"
        )
    if format_type == "setup.py":
        raise NotImplementedError("not yet ready")
    if format_type == "pypackage.toml":
        raise NotImplementedError("not yet ready")
    # TODO json output?
    return pprint.pformat(
        {name: str(version) for name, version in dependencies.items()}
    )


@click.command()
@click.argument("dependency_file")
@click.option(
    "--format-type",
    type=click.Choice(["setup.py", "requirements.txt", "pypackage.toml", "dict"]),
    default="requirements.txt",
)
def print_latest_versions_of_deps(
    dependency_file: str, format_type: FormatTypeType
) -> None:
    from distutils.core import run_setup

    distribution = run_setup(dependency_file, stop_after="init")

    new_versions = get_latest_versions(
        get_package_names_from_requirements(distribution.install_requires)
    )

    click.echo(format_dependencies(new_versions, format_type))


if __name__ == "__main__":
    print_latest_versions_of_deps()
