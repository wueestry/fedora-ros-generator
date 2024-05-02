# Meta Package
Name:           ros-iron-orocos-kdl-vendor
Version:        0.3.4
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-orocos_kdl_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-orocos_kdl_vendor
Requires:       ros2-iron-orocos_kdl_vendor-devel

Obsoletes: ros-iron-orocos-kdl-vendor < 0.3.4-1

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
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.3.4-1
- Update to latest upstream
