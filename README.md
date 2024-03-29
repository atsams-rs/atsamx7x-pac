# ATSAMx7x Rust PACs

This repository holds the PACs (Peripheral Access Crates) that supports and enable working with Microchip SAM S70/E70/V70/V71-based devices using Rust. Originally hosted in [atsamx7x-rust](https://github.com/atsams-rs/atsamx7x-rust) has been moved here to ease maintain and versioning in one Cargo Workspace.

The PACs are generated from SVD files provided by Microchip, publicly available at at the [Microchip Packs Repository](https://packs.download.microchip.com/).

## Development

This repository employs a [trunk-based development](https://trunkbaseddevelopment.com/): development occurs on `development` with short-lived branches that merges into it.
When a release is met, for example a `v0.3.2` release, a `release/v0.3.x` branch is spun of `development` and the release tagged. If this branch already exists, relevant commits are back-ported instead.

Development is done towards `development` branch.

### Commit Messages

This repository follows [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification, but with
first letter **capitalized**, for example:
```markdown
Fix: Add missing files

Building the create demonstrated some files were uncommitted, this rectifies the problem.

Resolves #999 
```
or
```markdown
Chore(Release): Prepare for 99.999.999

Closes #998
```

## Building

Install the ARMv7-EM target:
```sh
$ rustup target add thumbv7em-none-eabihf
```
and build the examples:
```sh
# <TBD>
```

## Flashing the device
Refer to the [SAM V71 Xplained Ultra README](/atsams-rs/atsamx7x-rust/boards/atsamv71_xult/README.md).

## Extra Documentation
* [Development Guide](docs/development.md)

# License

All source code in this repository is licensed under either of

* Apache License, Version 2.0 ([LICENSE-APACHE](./LICENCE-APACHE) or https://www.apache.org/licenses/LICENSE-2.0)
* MIT license ([LICENSE-MIT](./LICENSE-MIT) or https://opensource.org/licenses/MIT) \
at your option.

## Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted for inclusion in the work by you, as defined in the Apache-2.0 license, shall be licensed as above, without any additional terms or conditions.

