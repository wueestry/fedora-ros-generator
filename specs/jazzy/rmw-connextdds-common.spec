# Meta Package
Name:           ros-jazzy-rmw-connextdds-common
Version:        0.22.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rmw_connextdds_common and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rmw_connextdds_common
Requires:       ros2-jazzy-rmw_connextdds_common-devel

Obsoletes: ros-jazzy-rmw-connextdds-common < 0.22.1-1

%description
Common source for RMW implementations built with RTI Connext DDS
Professional and RTI Connext DDS Micro.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 05 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.22.1-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.22.0-1
- Update to latest release
