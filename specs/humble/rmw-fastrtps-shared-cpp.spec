# Meta Package
Name:           ros-humble-rmw-fastrtps-shared-cpp
Version:        6.2.6
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-rmw_fastrtps_shared_cpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rmw_fastrtps_shared_cpp
Requires:       ros2-humble-rmw_fastrtps_shared_cpp-devel

Obsoletes: ros-humble-rmw-fastrtps-shared-cpp < 6.2.6-1

%description
Code shared on static and dynamic type support of rmw_fastrtps_cpp.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Feb 12 2024 Tarik Viehmann - humble.6.2.6-1
- update to latest release
* Wed Dec 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.6.2.5-1
- update to latest upstream
* Wed Sep 27 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.6.2.4-1
- update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.6.2.3-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.6.2.3-1
- update to latest upstream release
* Thu Jul 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.6.2.3-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.6.2.2-1
- Initial humble build
