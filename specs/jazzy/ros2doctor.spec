# Meta Package
Name:           ros-jazzy-ros2doctor
Version:        0.32.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ros2doctor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ros2doctor
Requires:       ros2-jazzy-ros2doctor-devel

Obsoletes: ros-jazzy-ros2doctor < 0.32.3-1

%description
A command line tool to check potential issues in a ROS 2 system

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 05 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.32.3-1
- Update to latest release
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.32.2-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.32.1-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.32.0-1
- Update to latest release
