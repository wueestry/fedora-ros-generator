# Meta Package
Name:           ros-iron-rmw-connextdds-common
Version:        0.14.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rmw_connextdds_common and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rmw_connextdds_common
Requires:       ros2-iron-rmw_connextdds_common-devel

Obsoletes: ros-iron-rmw-connextdds-common < 0.14.1-1

%description
Common source for RMW implementations built with RTI Connext DDS
Professional and RTI Connext DDS Micro.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.14.1-1
- Update to latest release
