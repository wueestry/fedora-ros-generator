# Meta Package
Name:           ros-iron-rosbag2-test-common
Version:        0.22.6
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rosbag2_test_common and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rosbag2_test_common
Requires:       ros2-iron-rosbag2_test_common-devel

Obsoletes: ros-iron-rosbag2-test-common < 0.22.6-1

%description
Commonly used test helper classes and fixtures for rosbag2

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.22.6-1
- Update to latest release
