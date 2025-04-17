# Meta Package
Name:           ros-jazzy-gz-math-vendor
Version:        0.0.8
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/gazebosim/gz-math
Summary:        Meta package for ros2-jazzy-gz_math_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-gz_math_vendor
Requires:       ros2-jazzy-gz_math_vendor-devel

Obsoletes: ros-jazzy-gz-math-vendor < 0.0.8-1

%description
Vendor package for: gz-math7 7.5.2 Gazebo Math : Math classes and
functions for robot applications

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.8-1
- Update to latest release
* Wed Nov 20 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.7-1
- Update to latest release
* Wed Jul 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.6-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.5-1
- Update to latest release
