# Meta Package
Name:           ros-jazzy-geometric-shapes
Version:        2.3.2
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-geometric_shapes and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-geometric_shapes
Requires:       ros2-jazzy-geometric_shapes-devel

Obsoletes: ros-jazzy-geometric-shapes < 2.3.2-1

%description
This package contains generic definitions of geometric shapes and
bodies.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.3.2-1
- Update to latest release
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.3.1-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.2.1-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.1.3-1
- Update to latest release
