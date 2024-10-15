# Meta Package
Name:           ros-jazzy-rosbag2-compression-zstd
Version:        0.26.4
Release:        1%{?dist}
License:        Apache 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rosbag2_compression_zstd and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rosbag2_compression_zstd
Requires:       ros2-jazzy-rosbag2_compression_zstd-devel

Obsoletes: ros-jazzy-rosbag2-compression-zstd < 0.26.4-1

%description
Zstandard compression library implementation of rosbag2_compression

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.26.4-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.26.3-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.26.2-1
- Update to latest release
