let
  pkgs = import <nixpkgs> { };
in
pkgs.mkShellNoCC {
  packages = with pkgs; [
    (python3.withPackages (packages: [
      packages.jinja2
      packages.pyyaml
      packages.markdown
      packages.libsass
      packages.ansible
    ]))
    fswatch
    http-server
  ];
}
