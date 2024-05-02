# Meta Package
Name:           ros-iron-rosbag2-test-msgdefs
Version:        0.22.6
Release:        1%{?dist}
License:        Apache-2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rosbag2_test_msgdefs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rosbag2_test_msgdefs
Requires:       ros2-iron-rosbag2_test_msgdefs-devel

Obsoletes: ros-iron-rosbag2-test-msgdefs < 0.22.6-1

%description
message definition test fixtures for rosbag2 schema recording

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.22.6-1
- Update to latest release
