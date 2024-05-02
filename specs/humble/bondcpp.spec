# Meta Package
Name:           ros-humble-bondcpp
Version:        3.0.2
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/wiki/bondcpp
Summary:        Meta package for ros2-humble-bondcpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-bondcpp
Requires:       ros2-humble-bondcpp-devel

Obsoletes: ros-humble-bondcpp < 3.0.2-1

%description
C++ implementation of bond, a mechanism for checking when another
process has terminated.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.0.2-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.0.2-1
- update to latest upstream release
* Mon Apr 10 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.0.2-1
- update to latest upsteam
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.1.8.6-1
- update to latest release
