# Meta Package
Name:           ros-jazzy-rsl
Version:        1.1.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rsl and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rsl
Requires:       ros2-jazzy-rsl-devel

Obsoletes: ros-jazzy-rsl < 1.1.0-1

%description
ROS Support Library

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.1.0-1
- Update to latest release
