# Meta Package
Name:           ros-jazzy-rmw-dds-common
Version:        3.1.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rmw_dds_common and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rmw_dds_common
Requires:       ros2-jazzy-rmw_dds_common-devel

Obsoletes: ros-jazzy-rmw-dds-common < 3.1.0-1

%description
Define a common interface between DDS implementations of ROS
middleware.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.1.0-1
- Update to latest release
