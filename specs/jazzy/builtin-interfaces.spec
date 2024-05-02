# Meta Package
Name:           ros-jazzy-builtin-interfaces
Version:        2.0.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-builtin_interfaces and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-builtin_interfaces
Requires:       ros2-jazzy-builtin_interfaces-devel

Obsoletes: ros-jazzy-builtin-interfaces < 2.0.2-1

%description
A package containing message and service definitions for types defined
in the OMG IDL Platform Specific Model.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.0.2-1
- Update to latest release
