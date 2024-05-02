# Meta Package
Name:           ros-iron-rosbag2-compression
Version:        0.22.6
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rosbag2_compression and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rosbag2_compression
Requires:       ros2-iron-rosbag2_compression-devel

Obsoletes: ros-iron-rosbag2-compression < 0.22.6-1

%description
Compression implementations for rosbag2 bags and messages.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.22.6-1
- Update to latest release
