# Meta Package
Name:           ros-jazzy-simulation
Version:        0.11.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-simulation and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-simulation
Requires:       ros2-jazzy-simulation-devel

Obsoletes: ros-jazzy-simulation < 0.11.0-1

%description
A package which extends 'ros_base' and includes simulation packages.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Aug 03 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.11.0-1
- Update to latest release
