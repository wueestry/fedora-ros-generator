# Meta Package
Name:           ros-jazzy-ros2launch
Version:        0.26.7
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ros2launch and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ros2launch
Requires:       ros2-jazzy-ros2launch-devel

Obsoletes: ros-jazzy-ros2launch < 0.26.7-1

%description
The launch command for ROS 2 command line tools.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 05 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.26.7-1
- Update to latest release
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.26.6-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.26.5-1
- Update to latest release
