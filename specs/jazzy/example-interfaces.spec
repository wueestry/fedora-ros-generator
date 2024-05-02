# Meta Package
Name:           ros-jazzy-example-interfaces
Version:        0.12.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-example_interfaces and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-example_interfaces
Requires:       ros2-jazzy-example_interfaces-devel

Obsoletes: ros-jazzy-example-interfaces < 0.12.0-1

%description
Contains message and service definitions used by the examples.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.12.0-1
- Update to latest release
