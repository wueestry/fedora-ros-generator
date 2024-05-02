# Meta Package
Name:           ros-iron-console-bridge-vendor
Version:        1.6.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/ros/console_bridge
Summary:        Meta package for ros2-iron-console_bridge_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-console_bridge_vendor
Requires:       ros2-iron-console_bridge_vendor-devel

Obsoletes: ros-iron-console-bridge-vendor < 1.6.0-1

%description
Wrapper around console_bridge, providing nothing but a dependency on
console_bridge, on some systems. On others, it provides an
ExternalProject build of console_bridge.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.6.0-1
- Update to latest release
