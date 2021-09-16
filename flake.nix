{
  description = "System Information displayed through Discord Rich Presence";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs";

    utils.url = "github:numtide/flake-utils";
    poetry2nix.url = "github:nix-community/poetry2nix";
  };

  outputs = { self, nixpkgs, utils, poetry2nix }:
    utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
          overlays = [ poetry2nix.overlay ];
        };
      in rec {
        defaultPackage = pkgs.poetry2nix.mkPoetryApplication {
          projectDir = ./.;
        };

        defaultApp = defaultPackage;
      }
    );  
}
