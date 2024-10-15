# Meta Package
Name:           ros-humble-sick-scan-xd
Version:        3.5.0
Release:        1%{?dist}
License:        Apache-2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-sick_scan_xd and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-sick_scan_xd
Requires:       ros2-humble-sick_scan_xd-devel

Obsoletes: ros-humble-sick-scan-xd < 3.5.0-1

%description
ROS 1 and 2 driver for SICK scanner

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.5.0-1
- Update to latest release
