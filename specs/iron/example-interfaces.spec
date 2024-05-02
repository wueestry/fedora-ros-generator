# Meta Package
Name:           ros-iron-example-interfaces
Version:        0.10.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-example_interfaces and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-example_interfaces
Requires:       ros2-iron-example_interfaces-devel

Obsoletes: ros-iron-example-interfaces < 0.10.2-1

%description
Contains message and service definitions used by the examples.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.10.2-1
- Update to latest release
