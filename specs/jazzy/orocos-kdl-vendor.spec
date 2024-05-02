# Meta Package
Name:           ros-jazzy-orocos-kdl-vendor
Version:        0.5.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-orocos_kdl_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-orocos_kdl_vendor
Requires:       ros2-jazzy-orocos_kdl_vendor-devel

Obsoletes: ros-jazzy-orocos-kdl-vendor < 0.5.0-1

%description
Wrapper around orocos_kdl, providing nothing but a dependency on
orocos_kdl on some systems. On others, it fetches and builds
orocos_kdl locally.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.5.0-1
- Update to latest release
