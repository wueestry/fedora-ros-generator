# Meta Package
Name:           ros-jazzy-composition-interfaces
Version:        2.0.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-composition_interfaces and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-composition_interfaces
Requires:       ros2-jazzy-composition_interfaces-devel

Obsoletes: ros-jazzy-composition-interfaces < 2.0.2-1

%description
A package containing message and service definitions for managing
composable nodes in a container process.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.0.2-1
- Update to latest release
