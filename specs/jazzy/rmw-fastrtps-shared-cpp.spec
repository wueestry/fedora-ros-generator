# Meta Package
Name:           ros-jazzy-rmw-fastrtps-shared-cpp
Version:        8.4.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rmw_fastrtps_shared_cpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rmw_fastrtps_shared_cpp
Requires:       ros2-jazzy-rmw_fastrtps_shared_cpp-devel

Obsoletes: ros-jazzy-rmw-fastrtps-shared-cpp < 8.4.2-1

%description
Code shared on static and dynamic type support of rmw_fastrtps_cpp.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 05 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.8.4.2-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.8.4.1-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.8.4.0-1
- Update to latest release
