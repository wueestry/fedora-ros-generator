# Meta Package
Name:           ros-jazzy-navigation2
Version:        1.3.5
Release:        1%{?dist}
License:        Apache-2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-navigation2 and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-navigation2
Requires:       ros2-jazzy-navigation2-devel

Obsoletes: ros-jazzy-navigation2 < 1.3.5-1

%description
ROS2 Navigation Stack

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.5-1
- Update to latest release
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.4-1
- Update to latest release
* Wed Nov 20 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.3-1
- Update to latest release
* Mon Aug 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.2-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.1-1
- Update to latest release
