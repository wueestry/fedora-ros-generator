# Meta Package
Name:           ros-humble-orocos-kdl-vendor
Version:        0.2.5
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-orocos_kdl_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-orocos_kdl_vendor
Requires:       ros2-humble-orocos_kdl_vendor-devel

Obsoletes: ros-humble-orocos-kdl-vendor < 0.2.5-1

%description
Wrapper around orocos_kdl, providing nothing but a dependency on
orocos_kdl on some systems. On others, it fetches and builds
orocos_kdl locally.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.2.5-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.2.5-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.2.5-1
- Initial humble build
