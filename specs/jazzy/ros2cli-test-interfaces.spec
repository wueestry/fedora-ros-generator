# Meta Package
Name:           ros-jazzy-ros2cli-test-interfaces
Version:        0.32.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ros2cli_test_interfaces and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ros2cli_test_interfaces
Requires:       ros2-jazzy-ros2cli_test_interfaces-devel

Obsoletes: ros-jazzy-ros2cli-test-interfaces < 0.32.0-1

%description
A package containing interface definitions for testing ros2cli.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.32.0-1
- Update to latest release
