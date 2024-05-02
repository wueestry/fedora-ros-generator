# Meta Package
Name:           ros-iron-builtin-interfaces
Version:        1.6.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-builtin_interfaces and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-builtin_interfaces
Requires:       ros2-iron-builtin_interfaces-devel

Obsoletes: ros-iron-builtin-interfaces < 1.6.0-1

%description
A package containing message and service definitions for types defined
in the OMG IDL Platform Specific Model.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.6.0-1
- Update to latest release
