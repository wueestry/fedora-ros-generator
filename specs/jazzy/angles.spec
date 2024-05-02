# Meta Package
Name:           ros-jazzy-angles
Version:        1.16.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-angles and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-angles
Requires:       ros2-jazzy-angles-devel

Obsoletes: ros-jazzy-angles < 1.16.0-1

%description
This package provides a set of simple math utilities to work with
angles. The utilities cover simple things like normalizing an angle
and conversion between degrees and radians. But even if you're trying
to calculate things like the shortest angular distance between two
joint space positions of your robot, but the joint motion is
constrained by joint limits, this package is what you need. The code
in this package is stable and well tested. There are no plans for
major changes in the near future.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.16.0-1
- Update to latest release
