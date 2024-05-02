# Meta Package
Name:           ros-iron-geometric-shapes
Version:        2.1.3
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-geometric_shapes and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-geometric_shapes
Requires:       ros2-iron-geometric_shapes-devel

Obsoletes: ros-iron-geometric-shapes < 2.1.3-1

%description
This package contains generic definitions of geometric shapes and
bodies.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.1.3-1
- Update to latest release
