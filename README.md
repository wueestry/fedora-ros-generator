# fedora_ros_generator
This repository creates a generator for ROS packages

The generated ROS packages are hosted on [ROS COPR](https://copr.fedorainfracloud.org/coprs/wueestry/ros/).

This project is heavily based on the work done by morxa [rosfed](https://github.com/morxa/rosfed), but tries to make the packages more closely related to the original ubuntu packages (eg. naming, etc) and tries to be compatible with ros 2.

## The Generator

The `ros_generator.py` script works as follows:

1. It fetches package information about the upstream ROS package with the
   `rosinstall_generator`. This includes dependencies, license, sources, and
   the version.

   **Note:** It is important to have an updated rosdep database. You can update it
   by executing `rosdep update` after rosdep is installed.
2. With this information, it generates a SPEC file using the template in
   `./templates/`. The generic template in `./templates/pkg.spec.j2` works for
   most packages. For some packages, the template needs to be modified, in
   which case you can find the per-package template in
   `./templates/$pkgname.spec.j2`. Note that all package-specific templates
   extend the generic base template in `./templates/pkg.spec.j2`.
3. Additional modifications can be done by adding a config file to
   `cfg/$pkgname.yaml`. This allows to add missing build and runtime
   dependencies, filter out some dependencies, add build flags, and make a
   package noarch.
4. Optionally, the package is built in a COPR. The module `copr_build` supports
   building dependency chains.

The `ros_generator.py` script uses a default ROS distro, which usually is the latest
one but it may be falling behind in some cases. To know the default ROS distro
the `./ros_generator.py --help` command can be used.

A `--distro` or `-D` option allows to choose a different ROS distro than the default.

### How to add a new package

In the simplest case, run `./ros_generator.py $pkgname`, or
`./ros_generator.py -r $pkgname` if you want to generate SPEC files
for all dependencies of the given package.

You may need to do the following modifications to the config in
`./cfg/$pkgname.yaml`
