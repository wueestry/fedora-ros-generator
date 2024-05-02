# Meta Package
Name:           ros-jazzy-launch
Version:        3.4.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-launch and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-launch
Requires:       ros2-jazzy-launch-devel

Obsoletes: ros-jazzy-launch < 3.4.2-1

%description
The ROS launch tool.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.4.2-1
- Update to latest upstream
