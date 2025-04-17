# Meta Package
Name:           ros-jazzy-rosbag2-compression
Version:        0.26.6
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rosbag2_compression and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rosbag2_compression
Requires:       ros2-jazzy-rosbag2_compression-devel

Obsoletes: ros-jazzy-rosbag2-compression < 0.26.6-1

%description
Compression implementations for rosbag2 bags and messages.

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
