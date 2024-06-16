# Meta Package
Name:           ros-iron-nav2-simple-commander
Version:        1.2.9
Release:        1%{?dist}
License:        Apache-2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-nav2_simple_commander and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-nav2_simple_commander
Requires:       ros2-iron-nav2_simple_commander-devel

Obsoletes: ros-iron-nav2-simple-commander < 1.2.9-1

%description
An importable library for writing mobile robot applications in python3

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Jun 05 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.2.9-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.2.8-1
- Update to latest release
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.2.7-1
- Update to latest release
