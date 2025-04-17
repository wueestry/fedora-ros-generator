# Meta Package
Name:           ros-jazzy-rosbag2-storage-mcap
Version:        0.26.6
Release:        1%{?dist}
License:        Apache-2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rosbag2_storage_mcap and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rosbag2_storage_mcap
Requires:       ros2-jazzy-rosbag2_storage_mcap-devel

Obsoletes: ros-jazzy-rosbag2-storage-mcap < 0.26.6-1

%description
rosbag2 storage plugin using the MCAP file format

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.26.6-1
- Update to latest release
* Tue Oct 15 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.26.5-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.26.4-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.26.3-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.26.2-1
- Update to latest release
