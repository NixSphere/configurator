{ pkgs ? import <nixpkgs> {} }:

pkgs.python3Packages.buildPythonApplication rec {
    pname = "configurator";
    version = "0.1.0";
    format = "other";

    propagatedBuildInputs = [
        # List of dependencies
        pkgs.python3Packages.flask
    ];

    # Add further lines to `installPhase` to install any extra data files if needed.
    dontUnpack = true;
    installPhase = ''
        install -Dm755 ${./server.py} $out/bin/${pname}
    '';
}