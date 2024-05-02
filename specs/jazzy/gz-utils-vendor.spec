# Meta Package
Name:           ros-jazzy-gz-utils-vendor
Version:        0.0.4
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/gazebosim/gz-utils
Summary:        Meta package for ros2-jazzy-gz_utils_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-gz_utils_vendor
Requires:       ros2-jazzy-gz_utils_vendor-devel

Obsoletes: ros-jazzy-gz-utils-vendor < 0.0.4-1

%description
Vendor package for: gz-utils2 2.2.0 Gazebo Utils : Classes and
functions for robot applications

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.4-1
- Update to latest release
