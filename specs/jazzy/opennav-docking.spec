# Meta Package
Name:           ros-jazzy-opennav-docking
Version:        1.3.2
Release:        1%{?dist}
License:        Apache-2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-opennav_docking and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-opennav_docking
Requires:       ros2-jazzy-opennav_docking-devel

Obsoletes: ros-jazzy-opennav-docking < 1.3.2-1

%description
A Task Server for robot charger docking

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.2-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.1-1
- Update to latest release
