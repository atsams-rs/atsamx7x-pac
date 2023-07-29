#!/usr/bin/env python3
import argparse, glob, json, os, pathlib, shutil, string, sys

def process_template(source: pathlib.Path, destination: pathlib.Path, substitutions: dict[str, str]):
    if source.suffix != ".template":
        sys.exit("The source file is not a template.")
    template = ""
    with open(source) as templatefile:
        template = templatefile.read()
    filename = destination.joinpath(source.stem)
    print("* Substituting {} into {}".format(source, filename))
    os.makedirs(destination, exist_ok=True)
    with open(filename, "w") as cargotomlfile:
        cargotomlcontent = string.Template(template).substitute(substitutions)
        cargotomlfile.write(cargotomlcontent)

def link_svd_file(svdfile: pathlib.Path, pacdir: pathlib.Path):
    os.makedirs(pacdir.joinpath("svd"))
    os.symlink(svdfile, pacdir.joinpath("svd/chip.svd"))

def generate_crate(templatedir: pathlib.Path, pacdir: pathlib.Path, data: dict):
    all_templates = glob.iglob("**/*.template", root_dir=templatedir, recursive=True)
    for template in all_templates:
        innerdir = pathlib.Path(template).parent
        template = templatedir.joinpath(template)
        process_template(template, pacdir.joinpath(innerdir), data)

def read_svd_version_map(location: pathlib.Path) -> dict[str,str]:
    with open(location, "r") as file:
        data = json.load(file)
        if "mapping" not in data:
            sys.exit("Incorrect SVD version map format.")
        return data["mapping"]

def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("svddir", type=pathlib.Path, help="directory with SVD collection")
    parser.add_argument("-m", "--mapping", type=pathlib.Path,
                        required=False, metavar="mapfile.json", default=pathlib.Path("./svdmap.json"),
                        help="json file with version mappings (from `harvester`)")
    return parser.parse_args()

def main(argv: list[str]):
    args = arguments()
    svd_version_map = read_svd_version_map(args.mapping)  # TODO: change as option / make sure harvester updates, not overwrites
    all_svd_files = glob.iglob("ATSAM[E,S,V]7[0,1]*.svd", root_dir=args.svddir)
    for svd_file in all_svd_files:
        pac_name = pathlib.Path(svd_file).stem.lower()
        pac_path = pathlib.Path("pac/%s" % pac_name)  # TODO: pac out dir as arg?
        print("Converting {} to {}".format(svd_file, pac_path))
        shutil.rmtree(pac_path, ignore_errors=True)
        os.makedirs(pac_path)
        data = {
            'crate': str(pac_name),
            'chip': str(pac_name).upper(),
            'svd2rust_version': "0.28.0",  # TODO: keep in synced
            'atpack_version': svd_version_map.get(str(pac_name).upper(), "(unknown)"),  # TODO: process `svdmap.json`
        }
        link_svd_file(pathlib.Path(os.getcwd(), args.svddir, svd_file), pathlib.Path(os.getcwd(), pac_path))
        generate_crate(pathlib.Path("pac/templates"), pac_path, data)

if __name__ == '__main__':
    main(sys.argv)
