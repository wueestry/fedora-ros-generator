# Meta Package
Name:           ros-humble-rmw-connextdds-common
Version:        0.11.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-rmw_connextdds_common and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rmw_connextdds_common
Requires:       ros2-humble-rmw_connextdds_common-devel

Obsoletes: ros-humble-rmw-connextdds-common < 0.11.2-1

%description
Common source for RMW implementations built with RTI Connext DDS
Professional and RTI Connext DDS Micro.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.11.2-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.11.2-1
- update to latest upstream release
* Tue Aug 08 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.11.2-1
- update to latest upstream
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.11.1-1
- Initial humble build
