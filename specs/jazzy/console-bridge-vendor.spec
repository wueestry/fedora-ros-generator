# Meta Package
Name:           ros-jazzy-console-bridge-vendor
Version:        1.7.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/ros/console_bridge
Summary:        Meta package for ros2-jazzy-console_bridge_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-console_bridge_vendor
Requires:       ros2-jazzy-console_bridge_vendor-devel

Obsoletes: ros-jazzy-console-bridge-vendor < 1.7.1-1

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
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.7.1-1
- Update to latest release
