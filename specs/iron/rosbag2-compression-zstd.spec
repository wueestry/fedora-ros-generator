# Meta Package
Name:           ros-iron-rosbag2-compression-zstd
Version:        0.22.6
Release:        1%{?dist}
License:        Apache 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rosbag2_compression_zstd and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rosbag2_compression_zstd
Requires:       ros2-iron-rosbag2_compression_zstd-devel

Obsoletes: ros-iron-rosbag2-compression-zstd < 0.22.6-1

%description
Zstandard compression library implementation of rosbag2_compression

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.22.6-1
- Update to latest release
