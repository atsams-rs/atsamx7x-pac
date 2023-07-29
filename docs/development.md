# Developer's Guide

## Prerequisites
```sh
cargo install atpacks-svd-harvester
```

## Update SVDs
Use this step to automatically download most recent SVDs:
```sh
atpacks-svd-harvester -r https://packs.download.microchip.com/ -f same70,sams70,samv70,samv71 -d svd -m svdmap.json
```

## Update PACs
This step regenerates PAC crates based on `pac/templates` content. The `svdmap.json` is used to propagate info about versions of ATPACKs SVDs were obtained from as Atmel/Microchip do not version them.
```sh
tools/pacs.py
```

## Test
<!-- TODO: Describe how to test it with board examples -->

## Publication / Release
```sh
for p in `ls -d pac/at*` ; do cargo publish -p ${p##*/} ; done
```
