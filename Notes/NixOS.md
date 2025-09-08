
# NixOS

[[🏷️Linux distribution]]

NixOS is a Linux distribution built around the Nix package manager, known for its declarative configuration, reproducibility, and atomic upgrades. Unlike traditional Linux distributions, NixOS uses a unique approach to package and system management, making it highly reliable and easy to roll back changes.

![[Image 2.93.png|150]]

- **Declarative configuration**: System settings and installed packages are defined in a single configuration file (`/etc/nixos/configuration.nix`), ensuring consistency across deployments.
- **Atomic upgrades and rollbacks**: System updates do not modify existing files directly. Instead, changes are applied atomically, allowing users to switch between configurations safely.
- **Isolated package management**: Nix’s functional package manager ensures that dependencies do not conflict, allowing multiple versions of a package to coexist.
- **Immutable system structure**: Unlike traditional Linux distributions, where package installations modify global system files, NixOS stores packages in `/nix/store`, keeping the base system untouched.
- **Reproducibility**: Because the entire system is configured declaratively, users can recreate identical environments across different machines effortlessly.
- **Flexibility**: NixOS supports multiple desktop environments, servers, and containerized workloads, making it suitable for a wide range of use cases.

NixOS is ideal for developers, system administrators, and users who value stability, reproducibility, and advanced package management capabilities.

---

See also:
