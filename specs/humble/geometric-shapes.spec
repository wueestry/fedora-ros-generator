# Meta Package
Name:           ros-humble-geometric-shapes
Version:        2.1.3
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-geometric_shapes and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-geometric_shapes
Requires:       ros2-humble-geometric_shapes-devel

Obsoletes: ros-humble-geometric-shapes < 2.1.3-1

%description
This package contains generic definitions of geometric shapes and
bodies.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Sep 27 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.1.3-1
- update to latest release
* Thu Mar 09 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.1.3-1
- Initial humble build
