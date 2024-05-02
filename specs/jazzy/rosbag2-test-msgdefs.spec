# Meta Package
Name:           ros-jazzy-rosbag2-test-msgdefs
Version:        0.26.2
Release:        1%{?dist}
License:        Apache-2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rosbag2_test_msgdefs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rosbag2_test_msgdefs
Requires:       ros2-jazzy-rosbag2_test_msgdefs-devel

Obsoletes: ros-jazzy-rosbag2-test-msgdefs < 0.26.2-1

%description
message definition test fixtures for rosbag2 schema recording

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.26.2-1
- Update to latest release
