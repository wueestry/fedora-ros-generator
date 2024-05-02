# Meta Package
Name:           ros-iron-rosbag2-storage-mcap
Version:        0.22.6
Release:        1%{?dist}
License:        Apache-2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rosbag2_storage_mcap and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rosbag2_storage_mcap
Requires:       ros2-iron-rosbag2_storage_mcap-devel

Obsoletes: ros-iron-rosbag2-storage-mcap < 0.22.6-1

%description
rosbag2 storage plugin using the MCAP file format

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.22.6-1
- Update to latest release
