# Meta Package
Name:           ros-humble-console-bridge-vendor
Version:        1.4.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/ros/console_bridge
Summary:        Meta package for ros2-humble-console_bridge_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-console_bridge_vendor
Requires:       ros2-humble-console_bridge_vendor-devel

Obsoletes: ros-humble-console-bridge-vendor < 1.4.1-1

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
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.4.1-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.4.1-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.4.1-1
- Initial humble build
