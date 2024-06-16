# Meta Package
Name:           ros-jazzy-rosbag2-test-common
Version:        0.26.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rosbag2_test_common and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rosbag2_test_common
Requires:       ros2-jazzy-rosbag2_test_common-devel

Obsoletes: ros-jazzy-rosbag2-test-common < 0.26.3-1

%description
Commonly used test helper classes and fixtures for rosbag2

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.26.3-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.26.2-1
- Update to latest release
