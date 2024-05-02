# Meta Package
Name:           ros-jazzy-rosbag2
Version:        0.26.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rosbag2 and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rosbag2
Requires:       ros2-jazzy-rosbag2-devel

Obsoletes: ros-jazzy-rosbag2 < 0.26.2-1

%description
Meta package for rosbag2 related packages

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.26.2-1
- Update to latest release
